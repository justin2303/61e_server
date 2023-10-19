# 61e_server
This is website i made for a gaming commmunity called the 61e, they are a mount and blade: napoleonic wars regiment.
Made using Django, the project is organized into 4 modules, project61 is the main module, it doesn't have much edits from the original django create app template other than what is required to run the other modules.
The other modules are:
1. home
2. leaderboard
3. send

  
home:
Consists of the templates to render for the homepage, and the events page.

  
leaderboard:
Consists of the template for the leaderboards page, the SQL models for the leaderboards database,
and the scripts for filling in, deleting, and plotting the leaderboards database (you can find these in /leaderboard/management/commands/).

  
send:
Consists of the code required to run an async newsletter email server using celery.

  
You can check out the server now using the url: https://jc0323.pythonanywhere.com/
the leaderboards page is updated every Saturday after the Line battle hosted by 61e, as that is when the server logs are available for parsing. 
It is both a way for 61e members to track their kills (and also non-61e) but also going to be a part of my next React.js project, which is going to be
both a card trading webapp for 61e, and also a rewards system that gives members chances to get cards and badges based on attendance and kills, show them off, and trade.


