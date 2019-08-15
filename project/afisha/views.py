from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
import json
import hashlib
from afisha.forms import NameForm
from django.shortcuts import redirect
from datetime import datetime
# Create your views here.

def indexRender(request):
    with open(r'templates/temp.json', encoding='utf-8') as feedsjson:
        database = json.load(feedsjson)
    if request.method == 'POST':
        cinemaid = request.POST.get("cinemaid")
        temp = database['cinema'][cinemaid]
        database.update({"current":temp})
        literallyDump(database)
        return redirect('cinema')

    else:
        form = NameForm()
    kekus = database
    kekus.update({'form': form})
    return render(request, 'afisha/index.html', database)

def cinema(request):
    with open(r'templates/temp.json', encoding='utf-8') as feedsjson:
        database = json.load(feedsjson)
    return render(request, 'afisha/cinema.html', database)


def exit(request):
    with open(r'templates/temp.json', encoding='utf-8') as feedsjson:
        database = json.load(feedsjson)
    if request.method == 'POST':
        database['temp']['name'] = ""
        database['temp']['password'] = ""

        literallyDump(database)

        return redirect(indexRender)
    return render(request, 'afisha/exit.html', database)



def adminpanel(request):
    with open(r'templates/temp.json', encoding='utf-8') as feedsjson:
        database = json.load(feedsjson)
    if (database['temp']['name'] in list(database['admin'].keys())):
        return render(request, 'afisha/adminpanel.html', database)
    else:
        return render(request, 'afisha/index.html', database)

def moderpanel(request):
    with open(r'templates/temp.json', encoding='utf-8') as feedsjson:
        database = json.load(feedsjson)
    if (database['temp']['name'] in list(database['moder'].keys())):
        if request.method == 'POST':
            cinemaid = request.POST.get('cinemaid')
            database.update({"cinemaschedule":database['cinema'][cinemaid]})
            literallyDump(database)
            return redirect('newschedule')
        else:
            form = NameForm()
        kekus = database
        kekus.update({'form': form})
        return render(request, 'afisha/moderpanel.html', kekus)
    else:
        return render(request, 'afisha/index.html', database)

def userpanel(request):
    with open(r'templates/temp.json', encoding='utf-8') as feedsjson:
        database = json.load(feedsjson)
    if (database['temp']['name'] in list(database['users'].keys())):
        if request.method == 'POST':
            cinemaid = request.POST.get('cinemaid')
            day = request.POST.get('day')
            cinemaname = database['cinema'][cinemaid]['cinemaname']
            if (day =="Вся неделя"):
                database.update({"dayschedule": {"cinemaname":cinemaname,"cinemaid":cinemaid,  "schedule":database['cinema'][cinemaid]['schedule']}})
                literallyDump(database)
                return redirect('allschedule')
            else:
                database.update({"dayschedule": {"cinemaname":cinemaname,"cinemaid":cinemaid,  "schedule":database['cinema'][cinemaid]['schedule'][day]}})
                literallyDump(database)
            return redirect('schedule')
        else:
            form = NameForm()
        kekus = database
        kekus.update({'form': form})
        return render(request, 'afisha/userpanel.html', kekus)

    else:
        return render(request, 'afisha/index.html', database)


def literallyDump(database):
    with open(r'templates/temp.json', mode='w+', encoding='utf-8') as f:
        json.dump(database, f, indent=4, ensure_ascii=False)


def signinDump(database, login, password):
    with open(r'templates/temp.json', mode='w+', encoding='utf-8') as f:
        database["temp"]["name"] = str(login)
        database["temp"]["password"] = str(password)
        json.dump(database, f, indent=4, ensure_ascii=False)

def afisha(request):
    with open(r'templates/temp.json', encoding='utf-8') as feedsjson:
        database = json.load(feedsjson)
    return render(request, 'afisha/afisha.html', database)

def register(request):
    if request.method == 'POST':
        login = request.POST.get('name')
        password = request.POST.get('password')
        password = hashlib.md5(password.encode()).hexdigest()

        with open(r'templates/temp.json', encoding='utf-8') as feedsjson:
            database = json.load(feedsjson)
        database['users'].update({login:{"name": login, "pass": password}})

        literallyDump(database)

        return HttpResponseRedirect('/')
    else:
        form = NameForm()

    return render(request, 'afisha/register.html', {'form': form})

def signin(request):

    if request.method == 'POST':

        login = request.POST.get('name')
        password = request.POST.get('password')
        password = hashlib.md5(password.encode()).hexdigest()

        sessiontime = datetime.now()
        with open(r'templates/temp.json', encoding='utf-8') as feedsjson:
            database = json.load(feedsjson)

        for i in database["admin"]:
            if ((login == database["admin"][i]["name"]) and (password == database["admin"][i]["pass"])):
                database["admin"][login].update({"sessiontime": str(sessiontime)})
                literallyDump(database)
                signinDump(database, login, password)
                return redirect('adminpanel')
        else:
            for i in database["moder"]:
                if ((login == database["moder"][i]["name"]) and (password == database["moder"][i]["pass"])):
                    database["moder"][login].update({"sessiontime": str(sessiontime)})
                    literallyDump(database)
                    signinDump(database, login, password)
                    return redirect('moderpanel')
            else:
                for i in database["users"]:
                    if ((login == database["users"][i]["name"]) and (password == database["users"][i]["pass"])):
                        database["users"][login].update({"sessiontime": str(sessiontime)})
                        literallyDump(database)
                        signinDump(database, login, password)
                        return redirect('userpanel')

                else:
                    return redirect('signin')

    else:
        form = NameForm()

    return render(request, 'afisha/signin.html', {'form': form})


def newmoder(request):
    with open(r'templates/temp.json', encoding='utf-8') as feedsjson:
        database = json.load(feedsjson)
    if (database['temp']['name'] in list(database['admin'].keys())):

        if request.method == 'POST':

            login = request.POST.get('name')
            password = request.POST.get('password')
            password = hashlib.md5(password.encode()).hexdigest()
            database['moder'].update({login:{"name": login, "pass": password}})
            literallyDump(database)

            return redirect('adminpanel')

        else:
            form = NameForm()
        return render(request, 'afisha/newmoder.html', {'form': form})
    else:
        return render(request, 'afisha/index.html', database)

def newschedule(request):
    with open(r'templates/temp.json', encoding='utf-8') as feedsjson:
        database = json.load(feedsjson)
    if request.method == 'POST':

        moviename = request.POST.get('moviename')
        if moviename != None:
            realmoviename = list((moviename.split('###')))[0]
            jenre = list((moviename.split('###')))[1]
            dimension = list((moviename.split('###')))[2]
            year = list((moviename.split('###')))[3]
            timing = list((moviename.split('###')))[4]
            cinemaid = list((moviename.split('###')))[5]

            time = request.POST.get('time')
            price = request.POST.get('price')
            day = request.POST.get('day')
            database['cinema'][cinemaid]['schedule'][day].update({"day":day,realmoviename:{"moviename": realmoviename, "jenre": jenre, "dimension": dimension,"timing": timing , "year": year, "time": time, "price": price}})
            literallyDump(database)
            return redirect('moderpanel')
        else:
            form = NameForm()

    else:
        form = NameForm()
    with open(r'templates/temp.json', encoding='utf-8') as feedsjson:
        database = json.load(feedsjson)
    kekus = database
    kekus.update({'form': form})
    return render(request, 'afisha/newschedule.html', kekus)

def schedule(request):
    with open(r'templates/temp.json', encoding='utf-8') as feedsjson:
        database = json.load(feedsjson)
    if request.method == 'POST':

        day = request.POST.get('day')
        return HttpResponse(day)


    else:
        form = NameForm()
    with open(r'templates/temp.json', encoding='utf-8') as feedsjson:
        database = json.load(feedsjson)
    kekus = database
    kekus.update({'form': form})
    return render(request, 'afisha/schedule.html', kekus)

def allschedule(request):
    with open(r'templates/temp.json', encoding='utf-8') as feedsjson:
        database = json.load(feedsjson)
    if request.method == 'POST':

        day = request.POST.get('day')
        return HttpResponse(day)


    else:
        form = NameForm()
    with open(r'templates/temp.json', encoding='utf-8') as feedsjson:
        database = json.load(feedsjson)
    kekus = database
    kekus.update({'form': form})
    return render(request, 'afisha/allschedule.html', kekus)


def accounts(request):
    with open(r'templates/temp.json', encoding='utf-8') as feedsjson:
        database = json.load(feedsjson)
    if request.method == 'POST':
        name = request.POST.get('name')
        database['moder'].pop(name)
        literallyDump(database)
        return redirect(accounts)

    if (database['temp']['name'] in list(database['admin'].keys())):
        return render(request, 'afisha/accounts.html', database)
    else:
        return render(request, 'afisha/index.html', database)

def addcinema(request):
    with open(r'templates/temp.json', encoding='utf-8') as feedsjson:
        database = json.load(feedsjson)
    if (database['temp']['name'] in list(database['admin'].keys())):
        if request.method == 'POST':

            cinemaname = request.POST.get('cinemaname')
            cinemalocation = request.POST.get('cinemalocation')
            cinemaid = request.POST.get('cinemaid')
            monday = "Понедельник"
            tuesday = "Вторник"
            wednesday = "Среда"
            thursday = "Четверг"
            friday = "Пятница"
            saturday = "Суббота"
            sunday = "Воскресенье"
            database['cinema'].update({cinemaid:{"cinemaname": cinemaname, "cinemalocation": cinemalocation,
                                                 "cinemaid": cinemaid, "movie":{},
                                                 "schedule":{monday:{"day":monday},tuesday:{"day": tuesday},
                                                             wednesday:{"day":wednesday},
                                                             thursday:{"day":thursday},
                                                             friday:{"day":friday},
                                                             saturday:{"day":saturday},
                                                             sunday:{"day":sunday}}}})

            literallyDump(database)

            return redirect('adminpanel')

        else:
            form = NameForm()
        with open(r'templates/temp.json', encoding='utf-8') as feedsjson:
            database = json.load(feedsjson)
        kekus = database
        kekus.update({'form': form})
        return render(request, 'afisha/addcinema.html', kekus)
    else:
        return render(request, 'afisha/index.html', database)

def addmovie(request):
    with open(r'templates/temp.json', encoding='utf-8') as feedsjson:
        database = json.load(feedsjson)
    if (database['temp']['name'] in list(database['moder'].keys())):
        if request.method == 'POST':
            moviename = request.POST.get("moviename")
            jenre = request.POST.get("jenre")
            dimension = request.POST.get("dimension")
            timing = request.POST.get("timing")
            directors = request.POST.get("directors")
            actors = request.POST.get("actors")
            year = request.POST.get("year")
            cinemaid = request.POST.get("cinemaid")


            for i in database['cinema']:
                if i == cinemaid:
                    if jenre in list(database['cinema'][cinemaid]['movie']):
                        database['cinema'][cinemaid]['movie'][jenre].update({moviename:{"moviename": moviename, "jenre": jenre, "dimension": dimension, "timing": timing, "directors": directors, "actors": actors, "year": year, "cinemaid": cinemaid}})
                    else:
                        database['cinema'][cinemaid]['movie'].update({jenre: {moviename:{"moviename": moviename, "jenre": jenre, "dimension": dimension, "timing": timing, "directors": directors, "actors": actors, "year": year, "cinemaid": cinemaid}}})

            literallyDump(database)

            return redirect('moderpanel')

        else:
            form = NameForm()
        with open(r'templates/temp.json', encoding='utf-8') as feedsjson:
            database = json.load(feedsjson)
        kekus = database
        kekus.update({'form': form})
        return render(request, 'afisha/addmovie.html', kekus)
    else:
        return render(request, 'afisha/index.html', database)