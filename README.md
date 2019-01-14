# mlb-statistics
Django and MySQL Powered Database for Major League Baseball Statistics

## About Sports Plug/mlb-statistics
mlb-statistics is our Major League Baseball Database which is originally powered by [Sean Lehman's Baseball Database](http://www.seanlahman.com/) which included a ton of information about players and teams from 1871 to 2017. Lehman's database is originally in Microsoft AccessDB, but we were able to convert it into a MySQL Database for use with Django.
This webpage started as a project but is being developed as a personal project into a community for sports fans to be able to not only talk amongst eachother but have access to a variety of unique and useful web applications that any sports fan would want at the tip of their fingers while browsing and talking to other fans. This web page, even conceptually, is still very much a work in progress.
On the more techincal side of things, mlb-statistics is a Django and MySQL database project using Django versions 2.1 and up along with Python versions 3.5 and up. Follow along with the `How To Contribute` section below for more details on how the project is built and what you will need to do if you want to help out.

## How To Contribute
* First and foremost, you must have installed a version of Python on your computer version 3.5 or greater. This is because you will be installing and using Django version 2.1 or greater for collaborating on this project. If you are really just getting started, it would be very beneficial to follow [this guide](https://docs.djangoproject.com/en/2.1/topics/install/) on installing Django from their official documentation. It will walk you through each and every step from installing a virtual environment to even building your first app, but clearly you need not go that far into the tutorial if your interest lies in collaborating on a Sports Plug project.
* After you have installed the required prerequisites for a Django project, simply fork this repo and clone it.
* For the clearest and most painless contributions, you should have an `origin` remote linking to your fork and an `upstream` remote linking to this repo. Effective use of branches will also make pull requests clearer but is not as necessary as the previous step.
* MySQL Database schema and related files will be provided upon request.

## Quick-Start
Currently, the only portion of the web application that is up and being worked on is the MLB Statistics portion. There should always be various issues to work on in the issue cue open to work on.
All code related to the MLB Statistics page is in the `polls` directory.
When you are ready to test a change you have made to the server, in cmd type the following in the root directory of the project:
* `python manage.py runserver`
