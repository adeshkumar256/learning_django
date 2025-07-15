from django import forms
from .models import Review


# class ReviewForm(forms.Form):
#     user_name = forms.CharField(min_length=8, label="User name", error_messages={
#         "required": "Your name must not be empty!"
#     })
#     email = forms.EmailField(label="Please enter your email", error_messages={
#         "required": "Email cannot be empty!"
#     })
#     rating = forms.IntegerField(
#         min_value=1,
#         max_value=5,
#         label="Rating",
#         widget=forms.NumberInput(attrs={
#             'type': 'range',
#             'min': '1',
#             'max': '5',
#             'step': '1',
#             'oninput': 'this.nextElementSibling.value = this.value',
#         }),
#         error_messages={"required": "Please select a rating!"}
#     )


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user_name', 'email', 'rating']
        labels = {
            "user_name": "User name",
            "email": "Enter email",
            "rating": "Your Rating"
        }
        error_messages = {
            "user_name": {
                "required": "Your name must not be empty!"
            },
            "email": {
                "required": "Email cannot be empty!"
            },
            "rating": {"required": "Please select a rating!"}
        }
        widgets = {
            "rating": forms.NumberInput(attrs={
                'type': 'range',
                'min': '1',
                'max': '5',
                'step': '1',
                'oninput': 'this.nextElementSibling.value = this.value',
            })
        }
