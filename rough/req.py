import requests
import json

requests.post("http://127.0.0.1:8080/notify",json.dumps({"name":"love"}))
print("done")