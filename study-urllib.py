import json
from urllib import request
import logging

request_body = json.dumps({
    "custid": "21",
    "uuid": "ef30e1ca-9888-451d-a328-08bfc6a7d482",
    "token": "Encrypted Payload"
})
headers = {"content-type": "application/json"}
req = request.Request(
    url="http://localhost:3000/createCase1",
    headers=headers,
    data=request_body.encode("utf-8")
)

try:
    res = request.urlopen(req)
    print(res.read().decode("utf-8"))
except Exception as e:
    logging.error(e)
