import pymysql
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from polls.models import People, Teams, Pitching, Batting
from django.template import RequestContext
from django.core.paginator import Paginator
import operator
import re
import django.core.exceptions
from django.db.models import Q, Max
# from django.db.models import MAX
# Create your views here.

def index(request):
    return render(request, "index.html")
# def index(request):
#     """View function for home page of site."""

#     # fields = ['at_bats', 'runs', 'hits', 'number_2b', 'number_3b', 'hr', 'rbi', 'sb', 'cs', 'bb', 'so', 'ibb', 'hbp', 'sh', 'sf', 'gidp']


#     # batting_stat = request.GET.get('stat_leaders_batting')
#     # batting_stat_year = request.GET.get('stats_batting_year')
#     # if batting_stat or batting_stat_year:
#     #     b1 = Batting.objects.all()
#     #     b_max_v = b1.filter(Q(year_id=batting_stat_year)).aggregate(Max(batting_stat))
#     #     b_max = list(b_max_v.values())
#     #     print(b_max_v)

#         # Qr = None
#         # for field in fields:
#         #     q = Q(**{"%s__contains" % field: })
#         #     if Qr:
#         #         Qr = Qr | q  # or & for filtering
#         #     else:
#         #         Qr = q
#         # results = Batting.objects.get()
#         # print(int(b_max[0]))
#         # print(int(batting_stat_year))
#         # results = Batting.objects.raw("SELECT player_id as id, year_id, stint, '%s' FROM Batting where '%s'='%s' AND year_id='%s' " %(batting_stat, batting_stat, int(b_max[0]), int(batting_stat_year)))
#         results = ''
#         context = {
#             "results":results,
#         }
#         return render(request, "index.html", context)
#     else:
#         context = {}
#         return render(request, 'index.html', context=context)

def allplayers(request):
    """View function for allPlayers page of site."""

    # Generate counts of people object
    num_players = People.objects.count()
    players = People.objects.all()

    context = {
        'num_players': num_players,
        'players': players,
    }

    # Render the HTML template allPlayers.html w/ data in context variable
    return render(request, 'allPlayers.html', context=context)

def allteams(request):
    """View function for allTeams page of site."""

    # Generate counts of teams object
    num_teams = Teams.objects.count()
    oTeams = Teams.objects.all()
    teams = reversify(oTeams)
    context = {
        'num_teams': num_teams,
        'teams': teams,
    }

    # Render the HTML template allTeams.html w/ data in context variable
    return render(request, 'allTeams.html', context=context)

def search(request):
    """View function for search page of the site."""
    query = request.GET.get('p_name')
    query2 = request.GET.get('t_name')
    if query:
        querySize = len(query.split())
        if querySize <= 2 and querySize > 1:
            split = query.split()
            results = People.objects.filter(Q(name_first__icontains=split[0]) | Q(name_last__icontains=split[1]) |
                                            Q(name_first__icontains=split[1]) | Q(name_last__icontains=split[0]))
            context = {"results": results}
            return render(request, "search.html", context)
        elif querySize == 1:
            results = People.objects.filter(Q(name_first__icontains=query) | Q(name_last__icontains=query))
            context={"results":results}
            return render(request, "search.html", context)
        else:
            error = "You have entered an invalid name. Try either a first name and last name separated by a space or a " \
                    "first name on its own or a last name on its own."
            context = {"errorMessage":error}
            return render(request, "search.html", context)
    elif query2:
        query2Size = len(query2.split())
        if query2Size <= 3 and query2Size > 2:
            split = query2.split()
            t_results = Teams.objects.filter(Q(name__icontains=split[0]) | Q(name__icontains=split[1]) | Q(name__icontains=split[3]))
            context = {"t_results":t_results}
            return render(request, "search.html", context)
        elif query2Size <=2 and query2Size > 1:
            split = query2.split()
            t_results = Teams.objects.filter(Q(name__icontains=split[0]) | Q(name__icontains=split[1]))
            context = {"t_results": t_results}
            return render(request, "search.html", context)
        elif query2Size == 1:
            t_results = Teams.objects.filter(Q(name__icontains=query2) | Q(name__icontains=query2))
            context = {"t_results":t_results}
            return render(request, "search.html", context)
        else:
            error = "You have entered an invalid name. Try either a first name and last name separated by a space or a " \
                    "first name on its own or a last name on its own."
            context = {"t_errorMessage": error}
            return render(request, "search.html", context)
    else:
        context = {}
        return render(request, "search.html", context)

def player(request, pk=None):
    """ View for player information page"""
    if pk is not None:
      results = People.objects.get(player_id=pk)
      pitching = Pitching.objects.raw('''SELECT player_id as id,
                                       year_id, stint, team_id,
                                       league_id, W, L,
                                       G, GS, shutouts, saves, outs_pitched,
                                       H, ER, HR, BB, strikeouts, BAOpp, ERA, IBB,
                                       HBP, BK, R FROM Pitching WHERE player_id= %s''', [pk])

      batting = Batting.objects.raw('''SELECT player_id as id,
                                    year_id, stint, team_id, league_id, G, at_bats,
                                    runs, hits, 2B, 3B, HR, RBI, SB, CS, BB,
                                    SO, IBB, HBP, SH, SF, GIDP FROM Batting WHERE player_id= %s''', [pk])
      context = {
        "results": results,
        "pitching": pitching,
        "batting": batting,
      }
      return render(request, "playerInfo.html", context)
    else:
        return render(request, 'playerInfo.html')

def team(request,team_id=None,year_id=None):
    """View for individual team pages"""
    if team_id is not None:
      results = Teams.objects.get(team_id=team_id, year_id=year_id)
      context = {"results":results}
      return render(request, "teamInfo.html", context)
    else:
        return render(request, "teamInfo.html")

def reversify(queryset):
    """View for starting at the end of a queryset"""
    nQ = []
    i = 1
    for item in queryset:
        nQ.append(queryset[len(queryset) - i])
        i = i + 1
    return nQ


