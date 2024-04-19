from django.core.management.base import BaseCommand
from leaderboard.models import Player  # Import your model
import os

def find_user(str1):
    #str1="19:10:59 - Town_Drunkard has joined the game with ID: 468062"
    str2=""
    check_str=""
    for x in range(11,len(str1)):#skip the time
        if(str1[x]=='h'):
            check_str=str1[x+1]+str1[x+2]+str1[x+3]+str1[x+4]
            if(check_str=="as j"):
                break
        #else continue
        str2+=str1[x]

    return str2.replace(" ","")


def find_ID(str1):
    #str1="18:31:40 - 95th_Rfm_Hyun has joined the game with ID: 525977 and has administrator rights. "
    check_str=""
    ID=""
    y=11
    for x in range(11,len(str1)):#skip the time
        check_str+=str1[x]
        if ("with ID: ") in check_str:
            y=x
            break

    for x in range(y+1,len(str1)):
        if (str1[x].isspace()):
            break
        ID+=str1[x]

    print(f"ID of {ID} found")

    return ID.replace(" ","")

def find_TK(str1):
    #str1="19:11:31 - C8C_SPC_Preacher teamkilled 61e_Yorkist. "
    check_str=""
    tk_name=""
    y=11
    for x in range(11,len(str1)):#skip the time
        check_str+=str1[x]
        if ("teamkilled") in check_str:
            y=x-10
            break
    for x in range(11, y):
        tk_name+=str1[x]

    return tk_name.replace(" ", "")

def find_death(str1):
    y=11
    str2=""
    for x in range(11,len(str1)):
        if(str1[x]=='>'):
            y=x
            break

    for x in range(y,len(str1)):
        str2+=str1[x]


    return str2.replace(" ","")

def find_kill(str1):
    str2=""
    for x in range(11,len(str1)):
        if(str1[x]=='<'):
            break

        str2+=str1[x]


    return str2.replace(" ", "")

class Command(BaseCommand):
    help = 'Create user profiles from a text file'

    def handle(self, *args, **options):
        current_directory = os.path.dirname(os.path.abspath(__file__))

        file_path = os.path.join(current_directory,'logp.txt')
        Player.objects.all().delete()

        with open(file_path, 'r') as file:
            line = file.readline()
            cond1=("Has reset the Map.") in line and ("[SERVER]") in line and line.startswith(" 19:")

            while(not cond1):
                if("has joined the game with ID:") in line:
                    print(f"{line}")
                    username=find_user(line)
                    guid=find_ID(line)
                    temp_bool=0
                    try:
                        player = Player.objects.get(user_name=username)
                        temp_bool=1#duplicate username
                    except Player.DoesNotExist:#then move on
                        print(f"player with username: {username} doesn't exist yet.")
                        temp_bool=0
                    if(temp_bool == 1):
                        try:
                            player = Player.objects.get(user_name=username)
                            player.delete()
                            Player.objects.create(user_name=username,GUID=guid)

                        except Player.DoesNotExist:#then move on
                            print(f"player with username: {username} doesn't exist yet.")

                    else:
                        try:
                            print(f"Checking player with GUID: {guid} and username: {username}")
                            player = Player.objects.get(GUID=guid)
                            print(f"player with ID: {guid} already exists, updating username")
                            player.user_name = username
                            player.save()
                    # You can now work with the 'player' object
                        except Player.DoesNotExist:#then create the player
                            print(f"player with ID: {guid} doesn't exist yet, creating user {username}")
                            Player.objects.create(user_name=username,GUID=guid)
                line = file.readline()
                cond1=("Has reset the Map.") in line and ("[SERVER]") in line and line.startswith(" 19:") #redefine condition
            #now the event started, we can do kill counts, typically starts at 7-7:15PM EST
            print("NOW THE SECOND ONE STARTS!!!!")
            cond2=("ty all") in line and ("K-Macbeth") in line
            while(not cond2):#when both are in line, then event is over.
                if("has joined the game with ID:") in line:
                    print(f"{line}")
                    username=find_user(line)
                    guid=find_ID(line)
                    temp_bool=0
                    try:
                        player = Player.objects.get(user_name=username)
                        temp_bool=1#duplicate username
                    except Player.DoesNotExist:#then move on
                        print(f"player with username: {username} doesn't exist yet.")
                        temp_bool=0
                    if(temp_bool == 1):
                        try:
                            player = Player.objects.get(user_name=username)
                            temp_kills = player.kills
                            player.delete()
                            Player.objects.create(user_name=username,GUID=guid, kills = temp_kills)
                        except Player.DoesNotExist:#then move on
                            print(f"player with username: {username} doesn't exist yet.")

                    else:
                        try:
                            print(f"Checking player with GUID: {guid} and username: {username}")
                            player = Player.objects.get(GUID=guid)
                            print(f"player with ID: {guid} already exists, updating username")
                            player.user_name = username
                            player.save()
                    # You can now work with the 'player' object
                        except Player.DoesNotExist:#then create the player
                            print(f"player with ID: {guid} doesn't exist yet, creating user {username}")
                            Player.objects.create(user_name=username,GUID=guid)
                #checked for incoming player
                elif ("<img=ico_") in line:
                    print(f"{line}")
                    username=find_kill(line)
                    print(f"Checking player with name: {username} and updating kills")
                    try:
                        player = Player.objects.get(user_name=username)
                        print(f"player with name:{username}, incrementing kills")
                        player.kills+=1
                        player.save()
                        print("incremented by 1")
                    except Player.DoesNotExist:#probably a suicide then or some weird shit
                        print("player not found, probably a suicide")
                elif ("teamkilled") in line:#penalize TK's
                    username=find_TK(line)
                    print(f"{line}")
                    print(f"Checking teamkills for {username} and updating them")
                    try:
                        player= Player.objects.get(user_name=username)
                        player.kills-=1
                        player.save()
                        print("teamkill found")
                    except Player.DoesNotExist:#how... we'll see if this ever happens.
                        print("what...")
                line = file.readline()
                cond2=("ty all") in line and ("K-Macbeth") in line
            #typicaly ends when king macbeth 61e says "ty all for coming" or some permutation of that...

        try:
            serv_player = Player.objects.get(user_name="SERVER")#some reason server gets detected somehow..
            serv_player.delete()
            # You can now work with the 'player' object
        except Player.DoesNotExist:#then create the player
            print("server player doesnt exist")

        print("filtering names...")
        for x in Player.objects.all():
            original_username = x.user_name
            lower_username = original_username.lower()
            lower_username = lower_username.replace("nigg", "friend")
            lower_username = lower_username.replace("aryan", "buddy")
            lower_username = lower_username.replace("fag", "flower")
            lower_username = lower_username.replace("jew", "bud")
            lower_username = lower_username.replace("fuck", "potato")
            lower_username = lower_username.replace("shit", "soil")
            lower_username = lower_username.replace("bitch", "rose")
            lower_username = lower_username.replace("rape", "rope")
            lower_username = lower_username.replace("rapi", "violet")
            lower_username = lower_username.replace("pussy", "cat")
            lower_username = lower_username.replace("penis", "tree")
            #this looks bad but it's better than getting cancelled.
            if lower_username != original_username.lower():
                #its imperfect but i dont want to store capitals location and then remap them here. It's not my fault you
                #decided to have a name that offends people who are good at complaining. If it was up to me I'd just delete it.
                #but for the sake of tallying how well regiments performed, I'll keep at least the kills info correct.
                x.user_name = lower_username
                x.save()
