
from django import forms


class ReviewForm(forms.Form):
    user_name = forms.CharField(min_length=8)
    email = forms.EmailField()
