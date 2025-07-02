from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
monthly_challenges = {
    "january": "Read a new book.",
    "february": "Exercise every day.",
    "march": "Learn a new programming language.",
    "april": "Start a daily journal.",
    "may": "Cook a new recipe each week.",
    "june": "Go for a walk every morning.",
    "july": "Take a photo every day.",
    "august": "Try meditation.",
    "september": "Write a short story.",
    "october": "Volunteer for a cause.",
    "november": "Practice gratitude daily.",
    "december": None
}


def challenges(request):
    month_keys = list(monthly_challenges.keys())
    return render(
        request, "challenges/index.html", {"months": month_keys})
    # list_items = ""
    # for x in month_keys:
    #     redirect_path = reverse("month-challenge", args=[x])
    #     list_items += f"<li><a href={redirect_path}>{x.capitalize()}</a></li>"
    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)


def monthly_challenge_int(requst, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    # for redirecting
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        # response_data = f"<h3>{challenge_text}</h3>"
        # use appname/template name for app recongnisation else django will consider 2 templates same having same name
        # response_data = render_to_string("challenges/challenge.html")
        return render(request, "challenges/challenge.html", {
            "challenge": challenge_text,
            "month": month
        })  # render automatically return 200
    except:
        raise Http404()  # it will automatically search for 404.html file in root folder
    # DEBUG=True aways set in dev mode
        # return HttpResponseNotFound(f"<h1>This month ({month}) is not supported!</h1>")
