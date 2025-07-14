from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


def review(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        return HttpResponseRedirect(f"/reviews/thank-you?username={username}&email={email}")
    return render(request, "reviews/review.html")


def thank_you(request):
    username = request.GET.get('username', '')
    email = request.GET.get('email', '')
    return render(request, "reviews/thank_you.html", {
        "username": username,
        "email": email
    })
