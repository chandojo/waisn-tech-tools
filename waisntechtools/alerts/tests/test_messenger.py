from unittest.mock import patch, mock_open, Mock
from django.test import TestCase

from alerts.messenger import Messenger, Message
from alerts.models import Subscriber

# TODO: Create Messenger test to return file name and file contents

class MessengerTestCase(TestCase):
    def setUp(self):
        self.mock_client = Mock()
        self.mock_subscriber = Mock()
        self.mock_subscriber.phone_number = "+11234567890"

    def test_messenger(self):
        message_list = ['./alerts/assets/eng/welcome_msg.txt', './alerts/assets/eng/follow_up.txt']
        send_message = Messenger(self.mock_client).send(self.mock_subscriber, message_list)


class MessageTestCase(TestCase):
    def setUp(self):
        self.mocked_response = mock_open(read_data='The test has completed')

    def test_message(self):
        with patch('builtins.open', self.mocked_response, create=True) as f:
            read_message = Message(self.mocked_response).contents()
        self.assertEqual(read_message, 'The test has completed')

    def tearDown(self):
        self.mocked_response = None
