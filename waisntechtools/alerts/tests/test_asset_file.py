import os.path

from django.test import TestCase

from alerts.asset_files import *
from alerts.languages import Language


class AssetExistenceTestCase(TestCase):
    def test_eng_asset_existence(self):
        lang = Language.ENGLISH
        self._test_lang_specific_files(lang)
        self._test_eng_only_files(lang)

    def test_default_asset_existence(self):
        lang = Language.DEFAULT_LANGUAGE
        self._test_lang_specific_files(lang)
        self._test_eng_only_files(lang)

    def test_spa_asset_existence(self):
        self._test_lang_specific_files(Language.SPANISH)

    def test_cmn_asset_existence(self):
        self._test_lang_specific_files(Language.MANDARIN)

    def test_kor_asset_existence(self):
        self._test_lang_specific_files(Language.KOREAN)

    def test_vie_asset_existence(self):
        self._test_lang_specific_files(Language.VIETNAMESE)

    def _test_lang_specific_files(self, lang):
        self.assertTrue(os.path.isfile(AssetFiles(lang).confirmation_file()))
        self.assertTrue(os.path.isfile(AssetFiles(lang).error_file()))
        self.assertTrue(os.path.isfile(AssetFiles(lang).unsubscribe_file()))
        self.assertTrue(os.path.isfile(AssetFiles(lang).action_alert_file()))
        self.assertTrue(os.path.isfile(AssetFiles(lang).follow_up_file()))

    def _test_eng_only_files(self, lang):
        self.assertTrue(os.path.isfile(AssetFiles(lang).lang_select_file()))
        self.assertTrue(os.path.isfile(AssetFiles(lang).subscribe_help_file()))
        self.assertTrue(os.path.isfile(AssetFiles(lang).unsupported_lang_file()))
        self.assertTrue(os.path.isfile(AssetFiles(lang).welcome_file()))
