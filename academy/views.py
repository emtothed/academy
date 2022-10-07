from django.shortcuts import render
from django.http import HttpResponse
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import *
from django.http import JsonResponse
from datetime import date
import json
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
# Create your views here.


def register(request):
    if request.method == "POST":
        
        fullname = request.POST["fullname"]
        username = request.POST["username"]
        email = request.POST["email"]

        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password != confirmation:
            return render(request, "academy/register.html", {
                "message": "Passwords doesn't match."
            })

        try:
            user = User.objects.create_user(username, email, password , fullname=fullname)
            user.save()
        except IntegrityError:
            return render(request, "academy/register.html", {
                "message": "Username is taken."
            })
        login(request, user)
        return redirect("index")
    else:
        return render(request, "academy/register.html")


def login_view(request):
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return render(request, "academy/login.html", {
                "message": "Invalid username and/or password, please try again."
            })
    else:
        return render(request, "academy/login.html")


def logout_view(request):
    logout(request)
    return redirect("index")


def index(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        courses = user.courses.all()
        passeds = user.passed.all()
        passedcount = user.passed.all().count()
        allcount = Course.objects.all().count()
        if passedcount == allcount:
            try:
                gradtuated = True
                img = Image.open(f"academy/static/academy/certificates/{user.fullname}certificate.png")
            except FileNotFoundError:
                gradtuated = True
                img = Image.open('academy/static/academy/images/certificate.png')
                I1 = ImageDraw.Draw(img)
                font = ImageFont.truetype('academy/static/academy/font/ARIALNB.TTF', 100)
                text = user.fullname
                I1.text((650, 680), text,font=font ,fill=(0, 0, 0) )
                img.save(f"academy/static/academy/certificates/{user.fullname}certificate.png")
            

        else:
            gradtuated = False


        return render(request, "academy/index.html", {
            'user': user,
            'courses': courses,
            'passeds': passeds,
            'passedcount': passedcount,
            'allcount': allcount,
            'today': date.today(),
            'gradtuated':gradtuated
        })
    else:
        return render(request, "academy/login.html")


def schedule(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        takencount = user.courses.all().count()

        if request.method == "POST":
            data = json.loads(request.body)
            if data.get("coursename") is not None:
                if takencount < 3:
                    course = Course.objects.get(title=data["coursename"])
                    user.courses.add(course)
                    return HttpResponse(status=204)

        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        hours = ['9AM', '10AM', '11AM', '12PM']
        courses = []
        for i in Course.objects.all():
            if i not in user.courses.all() and i not in user.passed.all():
                courses.append(i)

        return render(request, "academy/schedule.html", {
            'courses': courses,
            'taken': takencount,
            'weekdays': weekdays,
        'hours': hours
        })
    else:
        return render(request, "academy/login.html")


def scheduleget(request):
    user = request.user
    courses = user.courses.all()
    return JsonResponse([course.serialize() for course in courses], safe=False)


def exam(request, title):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = User.objects.get(username=request.user.username)
            course = Course.objects.get(title=title)

            quests = course.quests.all()
            score = 0
            data = json.loads(request.body)
            answers = data["answers"]

            for i in range(len(answers)):
                if answers[i] == quests[i].answer:
                    score = score + (10/len(quests))


            try:
                scores = user.scores.get(course=course)
                scores.score = round(score, 2)
                scores.save()

            except Scores.DoesNotExist:
                newscore = Scores(student=user, course=course, score=score)
                newscore.save()

            user.courses.remove(course)

            if score > 6:
                user.passed.add(course)

            return HttpResponse(status=204)

        else:
            return render(request, "academy/exam.html", {
                'title': title
            })
    else:
        return render(request, "academy/login.html")


def questsget(request, title):
    if request.user.is_authenticated:
        course = Course.objects.get(title=title)
        questions = []
        for quest in course.quests.all():
            questions.append(quest.question)
        return JsonResponse(questions, safe=False)
    else:
        return render(request, "academy/login.html")


def scores(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        scores = user.scores.all().order_by('-pk')
        return render(request,"academy/scores.html",{
            'scores':scores
        })
    else:
        return render(request, "academy/login.html")