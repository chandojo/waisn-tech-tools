from os import path

from .languages import Language


class AssetFiles(object):
    _ASSET_DIR = "alerts/assets/"

    _CONFIRMATION_MSG_FILE = "confirmation_msg.txt"
    _LANG_SELECT_MSG_FILE = "language_selection_msg.txt"
    _SUBSCRIBE_HELP_MSG_FILE = "subscribe_help_msg.txt"
    _UNSUPPORTED_LANG_MSG_FILE = "unsupported_lang_msg.txt"
    _WELCOME_MSG_FILE = "welcome_msg.txt"
    _UNSUBSCRIBED_MSG_FILE = "unsubscribed_msg.txt"
    _ERROR_MSG_FILE = "error_msg.txt"
    _ACTION_ALERT_FILE = "action_alert.txt"
    _FOLLOW_UP_FILE = "follow_up.txt"

    def __init__(self, lang):
        self._lang = lang

    def confirmation_file(self):
        return self._asset_file(AssetFiles._CONFIRMATION_MSG_FILE)

    def lang_select_file(self):
        return self._asset_file(AssetFiles._LANG_SELECT_MSG_FILE)

    def subscribe_help_file(self):
        return self._asset_file(AssetFiles._SUBSCRIBE_HELP_MSG_FILE)

    def unsupported_lang_file(self):
        return self._asset_file(AssetFiles._UNSUPPORTED_LANG_MSG_FILE)

    def welcome_file(self):
        return self._asset_file(AssetFiles._WELCOME_MSG_FILE)

    def unsubscribe_file(self):
        return self._asset_file(AssetFiles._UNSUBSCRIBED_MSG_FILE)

    def error_file(self):
        return self._asset_file(AssetFiles._ERROR_MSG_FILE)

    def action_alert_file(self):
        return self._asset_file(AssetFiles._ACTION_ALERT_FILE)

    def follow_up_file(self):
        return self._asset_file(AssetFiles._FOLLOW_UP_FILE)

    def _asset_file(self, filename):
        lang_file = path.join(AssetFiles._ASSET_DIR, self._lang, filename)
        default_lang_file = path.join(AssetFiles._ASSET_DIR, Language.DEFAULT_LANGUAGE, filename)
        if path.isfile(lang_file):
            return lang_file
        else:
            return default_lang_file
