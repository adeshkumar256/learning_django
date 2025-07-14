from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ReviewForm

# Create your views here.


def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user_name = form.cleaned_data.user_name
            email = form.cleaned_data.email
            return HttpResponseRedirect(f"/reviews/thank-you?user_name={user_name}&email={email}")
    else:
        form = ReviewForm()

    return render(request, "reviews/review.html", {
        "form": form
    })


def thank_you(request):
    user_name = request.GET.get('user_name', '')
    email = request.GET.get('email', '')
    return render(request, "reviews/thank_you.html", {
        "user_name": user_name,
        "email": email
    })
