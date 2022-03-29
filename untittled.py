
import requests
#mouthy funciona
url='https://api.dictionaryapi.dev/api/v2/entries/en/mouthy'
answer =requests.get(f'{url}')
answer=answer.json()
if type(answer)==list:
    page=answer[0]
    meanings=page['meanings']
    variables=meanings[0]
    definitions=variables['definitions']
    definition=definitions[0]
    last_def=definition['definition']
    last_def=last_def.split(";")
    print(last_def[0])
else:
    print("We didn't find a definition for this word")
