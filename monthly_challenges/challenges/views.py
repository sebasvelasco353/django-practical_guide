from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse

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
    "december": None,
}


def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {"months": months})


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        raise Http404()

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(
            request,
            "challenges/challenge.html",
            {"text": challenge_text, "month": month},
        )
    except:
        raise Http404()
