from django.test import TestCase
from django.core.urlresolvers import reverse


class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)


class ResultTest(TestCase):
    def test_result_view_status_code(self):
        url = reverse('result')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
