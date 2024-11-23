from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

monthly_challenges = {
    "january": "run",
    "february": "eat",
    "march": "cook",
    "april": "code",
    "may": "learn",
    "june": "eat",
    "july": "run",
    "august": "exercise",
    "september": "run",
    "october": "jump",
    "november": "drive",
    "december": "drink",
}


def monthly_challenge_by_number(request, month):
    return HttpResponse(month)


def monthly_challenge(request,  month):
    try:
        text = monthly_challenges[month]
        return HttpResponse(text)
    except:
        return HttpResponseNotFound("Not found")
