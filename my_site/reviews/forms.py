
from django import forms


class ReviewForm(forms.Form):
    user_name = forms.CharField(min_length=8, label="User name", error_messages={
        "required": "Your name must not be empty!"
    })
    email = forms.EmailField(label="Please enter your email", error_messages={
        "required": "Email cannot be empty!"
    })
