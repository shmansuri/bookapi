import requests
import json

URL ="http://127.0.0.1:8000/"

data = {
    'title':'python',
    'Author':'manish ',
    'desc':'This Programming Language Python Tutorial is very well suited for beginners and also for experienced programmers.',
    'cover_img':'',
    'rating':4.5
}
json_data = json.dumps(data)
r= requests.post(url=URL,data=json_data)
return_data = r.json()
print(return_data)

