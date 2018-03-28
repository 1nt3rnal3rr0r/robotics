class Message:
    def __init__(self, language, content):
        self._language = language
        self._content = content

    def get_content(self):
        return self._content

    def get_language(self):
        return self._language
