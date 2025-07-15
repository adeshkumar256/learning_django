from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from django.views import View
from django.views.generic.base import TemplateView
from .models import Review

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


class ThankView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Here is the message"
        return context


class ReviewListView(TemplateView):
    template_name = "reviews/review_list.html"

    def get_context_data(self, **kwargs):
        all_reviews = Review.objects.all()
        context = super().get_context_data(**kwargs)
        context['all_reviews'] = all_reviews
        return context

    # Now not needed as we have used generetic templateview class
    # def get(self, request):
    #     return render(request, "reviews/thank_you.html")
