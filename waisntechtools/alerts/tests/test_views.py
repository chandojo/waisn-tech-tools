from django.core.management import call_command
from django.core.management.commands import flush
from django.test import TestCase
from django.urls import reverse

from alerts.tests.fakes import SubscriberFactory


class IndexViewTests(TestCase):
    def setUp(self):
        call_command(flush.Command(), interactive=False)

    def tearDown(self):
        call_command(flush.Command(), interactive=False)

    def test_list_length(self):
        num_subscribers = 10
        for _ in range(0, num_subscribers):
            SubscriberFactory.create()

        response = self.client.get(reverse('alerts:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "WAISN")
        self.assertEqual(len(response.context['subscribers']), 10)

