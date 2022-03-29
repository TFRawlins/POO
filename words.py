
from tkinter import W
import requests

def random_words(url):
    answer =requests.get(f'{url}')
    return answer

class words:
    def __init__(self, language="en"):
        self.url="https://random-word-api.herokuapp.com/word?number=5&lang=en"
        self.language=language

    def get_words(self):
        answer=random_words(self.url)
        return answer

    def clean_word_list(self,lst):
        word_list=lst.json()
        return word_list


