from django import forms
from allauth.account.models import EmailAddress

class UserSignupForm(forms.Form):
    _AGREEMENT_ERRORS = {
        'required': 'You need to agree to the terms to register',
    }
    fullname = forms.CharField(max_length = 50)
    agreement = forms.BooleanField(error_messages=_AGREEMENT_ERRORS)
