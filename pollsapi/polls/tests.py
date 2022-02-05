from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

from urllib import request
from django.test import TestCase
from rest_framework.test import APITestCase, APIRequestFactory

from polls import apiviews

class TestPoll(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = apiviews.PollViewSet.as_view({'get': 'list'})
        self.url = '/polls'
        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        self.token.save()

    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user(
            'test',
            email='testuser@test.com',
            password = 'test'
        )


    def test_list(self):
        requests = self.factory.get(self.url, HTTP_AUTHORIZATION='Token {}'.format(self.token.key))
        request.user = self.user
        response = self.view(request)
        self.assertEqual(response.status_code, 200, 'Expected Response COde 200, received {0} instead.'.format(response.status_code))
