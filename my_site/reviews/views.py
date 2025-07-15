from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from django.views import View

# Create your views here.


class ReviewView(View):

    def get(self, request):
        form = ReviewForm()

        return render(request, "reviews/review.html", {
            "form": form
        })

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
        # print(form.cleaned_data)
        # user_name = form.cleaned_data.user_name
        # email = form.cleaned_data.email
            return HttpResponseRedirect(f"/reviews/thank-you")
        else:
            return render(request, "reviews/review.html", {
                "form": form
            })


def thank_you(request):
    return render(request, "reviews/thank_you.html")
