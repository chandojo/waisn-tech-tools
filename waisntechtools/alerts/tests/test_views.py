from bs4 import BeautifulSoup
from django.contrib.staticfiles import finders
from django.core.management import call_command
from django.core.management.commands import flush
from django.test import TestCase, override_settings
from django.urls import reverse

from alerts.tests.fakes import SubscriberFactory


@override_settings(WAISN_AUTH_DISABLED=True, DEBUG=True)
class IndexViewTests(TestCase):
    _STATIC_PREFIX = '/static/'

    def test_home_page_static_content(self):
        response = self.client.get(reverse('alerts:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'WAISN')

        static_imgs = [
            img['src'][len(IndexViewTests._STATIC_PREFIX):]
            for img in BeautifulSoup(response.content, 'html.parser').find_all("img")
            if IndexViewTests._is_static_resource(img['src'])
        ]

        for static_img in static_imgs:
            self.assertIsNotNone(finders.find(static_img))

    @staticmethod
    def _is_static_resource(resource):
        return resource.startswith(IndexViewTests._STATIC_PREFIX)


@override_settings(WAISN_AUTH_DISABLED=True, DEBUG=True)
class DebugViewTests(TestCase):
    def setUp(self):
        call_command(flush.Command(), interactive=False)

    def tearDown(self):
        call_command(flush.Command(), interactive=False)

    def test_list_length(self):
        num_subscribers = 10
        for _ in range(0, num_subscribers):
            SubscriberFactory.create()

        response = self.client.get(reverse('alerts:debug'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['subscribers']), 10)        
