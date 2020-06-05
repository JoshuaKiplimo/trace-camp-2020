
'''
Playing with APIS - Open weather API

'''

import requests
import json
import os

api_1 = os.environ.get('API_1')
api_2 = os.environ.get('API_2')
payload ={'q': "Columbia", 'units': 'imperial', 'APPID': api_1}
json_data =requests.get('https://api.openweathermap.org/data/2.5/forecast?',params=payload).json()

#print(json_data)



'''
playing with APIS - news API

'''


url = ('http://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey'= api_2)
response = requests.get(url).json()
print(response)
