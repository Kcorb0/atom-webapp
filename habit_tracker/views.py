from django.shortcuts import render
from django.http import HttpResponse
from .models import Habit
from .utils.dates import datelist

habits_example = [
    {
        'creation_date': '2/3/2021',
        'category': 'Mental Health',
        'title': 'Meditation for 5+ Minutes',
        'tracking': {'07/03/2021': True, '06/03/2021': True, '05/03/2021': False, '04/03/2021': True, '03/03/2021': False}
    },
    {
        'creation_date': '2/3/2021',
        'category': 'Fitness',
        'title': 'Skipping 30 Minutes before 10:00',
        'tracking': {'07/03/2021': True, '06/03/2021': True, '05/03/2021': True, '04/03/2021': False, '03/03/2021': False}
    },
    {
        'creation_date': '2/3/2021',
        'category': 'Study',
        'title': 'Programming for 3+ Hours',
        'tracking': {'07/03/2021': True, '06/03/2021': True, '05/03/2021': True, '04/03/2021': True, '03/03/2021': True}
    }
]


def home(request):
    context = {
        'title': 'Home',
        'habits': habits_example,
        'dates_list': datelist(13)
    }
    return render(request, 'habit_tracker/home.html', context)


def app_help(request):
    context = {
        'title': 'Help',
    }
    return render(request, 'habit_tracker/help.html', context)
