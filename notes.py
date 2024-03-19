#!usr/bin/env python3

class Note:
    def __init__(self, content):
        self.content = content

    def match(self, search_text):
        return search_text in self.content

    def __str__(self):
        return self.content
