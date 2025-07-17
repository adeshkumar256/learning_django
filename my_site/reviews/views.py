from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
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


class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "all_reviews"

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gte=3)
        return data

    # def get_context_data(self, **kwargs):
    #     all_reviews = Review.objects.all()
    #     context = super().get_context_data(**kwargs)
    #     context['all_reviews'] = all_reviews
    #     return context


class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review
    context_object_name = "review"

    ? need to change the param name to ** pk ** in urls so that it can search by primary key

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     review_id = kwargs["id"]
    #     review = Review.objects.get(pk=review_id)
    #     context['review'] = review
    #     return context

# class SingleReviewView(TemplateView):
#     template_name = "reviews/single_review.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review_id = kwargs["id"]
#         review = Review.objects.get(pk=review_id)
#         context['review'] = review
#         return context

    # Now not needed as we have used generetic templateview class
    # def get(self, request):
    #     return render(request, "reviews/thank_you.html")
