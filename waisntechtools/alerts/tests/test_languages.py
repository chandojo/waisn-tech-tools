from django.test import TestCase

from alerts.languages import Language, UnknownLanguageId, MessagePhraseConditions


class LanguagesTestCase(TestCase):
    def test_supported_language_index(self):
        iso_code = Language.language_code("1")
        self.assertEqual(iso_code, "eng")

    def test_unsupported_language_index(self):
        try:
            Language.language_code("100")
            self.fail()
        except UnknownLanguageId:
            pass


class MessageContentTestCase(TestCase):
    def test_eng_join(self):
        msg = "join"
        self.assertTrue(MessagePhraseConditions(msg).is_join_msg())
        self.assertFalse(MessagePhraseConditions(msg).is_change_lang_msg())
        self.assertFalse(MessagePhraseConditions(msg).is_leave_msg())

    def test_spa_change_lang(self):
        msg = "cambio de lengua"
        self.assertFalse(MessagePhraseConditions(msg).is_join_msg())
        self.assertTrue(MessagePhraseConditions(msg).is_change_lang_msg())
        self.assertFalse(MessagePhraseConditions(msg).is_leave_msg())

    def test_spa_leave(self):
        msg = "abandonar"
        self.assertFalse(MessagePhraseConditions(msg).is_join_msg())
        self.assertFalse(MessagePhraseConditions(msg).is_change_lang_msg())
        self.assertTrue(MessagePhraseConditions(msg).is_leave_msg())

    def test_garbage(self):
        msg = "garbage"
        self.assertFalse(MessagePhraseConditions(msg).is_join_msg())
        self.assertFalse(MessagePhraseConditions(msg).is_change_lang_msg())
        self.assertFalse(MessagePhraseConditions(msg).is_leave_msg())
