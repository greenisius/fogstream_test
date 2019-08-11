'''
До текущего момента не сталкивался с web разработкой.
По этой причине совершенно не понимаю полезность тестов и писать их не умею.
Здесь они представлены только формально.
'''

from django.test import TestCase
from django.urls import reverse

import json
import urllib.request

from mytestapp.models import UserMessage

class UserMessageTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        UserMessage.objects.create(email='spam@spam.spam', text='Hello Admin')
    
    def test_email_label(self):
        msg=UserMessage.objects.get(id=1)
        field_label = UserMessage._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email')

    def test_email_max_length(self):
        msg=UserMessage.objects.get(id=1)
        max_length = msg._meta.get_field('email').max_length
        self.assertEquals(max_length, 40)

class ViewsTest(TestCase):
    #@classmethod
    def access_without_authentication(self):
        resp = self.client.get(reverse('test_form'))
        self.assertEqual(resp.status_code, 200)

    def web_data_is_available(self):
        web_data = urllib.request.urlopen('http://jsonplaceholder.typicode.com/users').read().decode('utf-8')
        web_data = json.loads(web_data)
        res_data = ''
        for data_unit in web_data:
            if 'Sincere@april.biz' == data_unit['email']:
                res_data = json.dumps(data_unit)
        assertTrue(res_data != '')