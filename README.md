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

(commits are done.. whenever i feel like it. Code is often fiddled with for the website on the URL when something needs to be changed, or a bug appears.)

