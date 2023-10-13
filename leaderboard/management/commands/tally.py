from django.core.management.base import BaseCommand
from leaderboard.models import Player, Regiments # Import your model
import matplotlib.pyplot as plt
import os


class Command(BaseCommand):
    help = 'Create user profiles from a text file'

    def add_arguments(self, parser):
        parser.add_argument('my_argument', type=str, help='A string argument')

    def handle(self, *args, **options):
        date = options['my_argument']
        print(f'You provided the argument: {date}')
        count_61=(Player.objects.filter(user_name__regex=r'61e')).count()
        print(count_61)
        count_CSC=(Player.objects.filter(user_name__regex=r'CSC')).count()
        count_GIB=(Player.objects.filter(user_name__regex=r'GIB')).count()
        count_ERB=(Player.objects.filter(user_name__regex=r'ERB')).count()
        count_84=(Player.objects.filter(user_name__regex=r'84th')).count()
        count_85=(Player.objects.filter(user_name__regex=r'85th')).count()
        count_BAS=(Player.objects.filter(user_name__regex=r'BAS')).count()
        count_total=Player.objects.count()
        count_pubs=Player.objects.count()
        count_pubs=count_pubs-count_61-count_CSC-count_GIB-count_ERB-count_84-count_85-count_BAS
        y_vals= [count_61, count_CSC, count_GIB, count_ERB, count_84,count_85,count_BAS,count_pubs]
        x_titles=["61e","CSC", "1aGIB", "ERB", "84th", "85th","BAS","No_Reg"]
        x_vals=[1,2,3,4,5,6,7,9]

        # Create a basic line plot
        plt.bar(x_vals, height=y_vals, tick_label=x_titles)
        # Add labels and a title
        plt.xlabel('Regiments who attended the 61e Saturday event')
        plt.ylabel('People Brought')
        plt.title('Attendence Plot')
        plt.savefig('home/static/home/att_plot.png', format='png')
        Regiments.objects.create(date = date,reg_61e=count_61, reg_CSC=count_CSC, reg_84th=count_84, reg_85th=count_85, reg_ERB=count_ERB, 
                                 reg_1aGIB=count_GIB, reg_pubs=count_pubs, reg_BAS=count_BAS, total = count_total)
        """
        X_tit=[]
        x_s=[]
        y=[]
        for x in Regiments.objects.all():
            X_tit.append(Regiments.objects.name(id=x))
            x_s.append(x*2)
            y.append(Regiments.objects.get(id=x).total)

        x_titles=["61e","CSC", "1aGIB", "ERB", "84th", "85th","BAS","No_Reg"]
        x_vals=[1,2,3,4,5,6,7,9]

        # Create a basic line plot
        plt.bar(x_s, height=y, tick_label=X_tit)
        # Add labels and a title
        plt.xlabel('Attendance over time')
        plt.ylabel('Total Attendance')
        plt.title('Evento America Attendance')
        plt.savefig('home/static/home/total_plot.png', format='png')
        """

