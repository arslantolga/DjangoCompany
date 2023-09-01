from django.shortcuts import render
from django.http import HttpResponse
from random import randint

# Create your views here.

FAKE_DB_PROJECTS = []
for i in range(0,8):
    id = randint(50,150)
    FAKE_DB_PROJECTS.append(f"https://picsum.photos/id/{id}/100/100")

FAKE_DB_CAROUSEL = [
    f"https://picsum.photos/id/{id}/1200/400" for id in range(90,93)
]

def home_view(request):
    page_title = "Home"
    context = dict(
        page_title=page_title,
        fake_db_projects = FAKE_DB_PROJECTS,
        FAKE_DB_CAROUSEL = FAKE_DB_CAROUSEL,
    )
    return render(request, "pages/home.html", context)

def vision_view(request):
    page_title = "Vision"
    context = dict(
        page_title=page_title,
        fake_db_projects = FAKE_DB_PROJECTS,
    )
    return render(request, "pages/vision.html", context)

def about_view(request):
    page_title = "About"
    context = dict(
        page_title=page_title,
        fake_db_projects = FAKE_DB_PROJECTS,
    )
    return render(request, "pages/about.html", context)

def contact_view(request):
    page_title = "Contact"
    context = dict(
        page_title=page_title,
        fake_db_projects = FAKE_DB_PROJECTS,
    )
    return render(request, "pages/contact.html", context)