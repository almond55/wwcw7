import sys, os, json, string
from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
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

        assert resp.status_code == 302, resp.status_code
        
        assert EmailAddress.objects.get(email=post_data['email']) is not None

        assert EmailAddress.objects.all()[0].email == post_data['email']
