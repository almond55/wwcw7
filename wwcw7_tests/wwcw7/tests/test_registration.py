import sys, os, json, string
from datetime import date, timedelta
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from httmock import urlmatch, HTTMock
from allauth.account.models import EmailAddress

class TestRegistrationViews(TestCase):
    def test_register(self):
    """
    Test register a new user
    """
    url = reverse('account_signup')
    post_data = {
        'email'       : 'testuser@test.com',
        'password1'   : '123123',
        'password2'   : '123123',
    }

    resp = self.client.post(url, post_data)

    print(resp.content)
