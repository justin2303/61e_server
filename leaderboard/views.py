from django.shortcuts import render
import json
from .models import Player, Regiments
# Create your views here.
def index(request):
    players = Player.objects.all()
    total_kills = sum(Player.kills for Player in players)
    kills_61e = sum(Player.kills for Player in players if "61e" in Player.user_name)
    percent_kill=kills_61e/total_kills * 100
    total_attend=Player.objects.all().count()
    total_61 = (Player.objects.filter(user_name__regex=r'61e')).count()
    player_week = (Player.objects.order_by('-kills').first()).user_name
    regiment_list=Regiments.objects.all()
    list_61_att = {(Regiments.reg_61e / Regiments.total) for Regiments in Regiments.objects.all()}
    return render (request, "leaderboard/index.html",{
        "Players": Player.objects.order_by('-kills'),
        "Regiment_list": regiment_list,
        "total_kills": total_kills,
        "kills_61e": kills_61e,
        "percent_kill": percent_kill,
        "numbers": total_attend,
        "total_61": total_61,
        "POW": player_week,
        "list_att": list_61_att,
        
    })

