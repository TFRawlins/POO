import requests

def meaning(url):
    answer =requests.get(f'{url}')
    answer=answer.json()
    return answer

class definition:
    def __init__(self):
        self.url='https://api.dictionaryapi.dev/api/v2/entries/en/'

    def get_definition(self,word):
        answer=meaning(f'{self.url+word}')
        if type(answer)==list:
            page=answer[0]
            meanings=page['meanings']
            variables=meanings[0]
            definitions=variables['definitions']
            definition=definitions[0]
            last_def=definition['definition']
            last_def=last_def.split(";")
            print(f'\n ==== {word} ==== \n{last_def[0]}\n')
        else:
            print(f'\n ==== {word} ==== \nWe didnt find a definition for this word\n')