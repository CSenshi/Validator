import requests as req

URL = "http://127.0.0.1:5000/register/?first_name=Jon&last_name=Doe&age=100&mail=jon.doe@g"

resp = req.get(URL)

print(resp.text)
