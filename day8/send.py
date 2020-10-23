import sys
import requests
from formatting import format_msg
from datetime import datetime


def send(name, website):
    msg = format_msg(myname=name, mywebsite=website)
    r = requests.get("http://httpbin.org/json")
    print(r.status_code)
    if r.status_code == 200:
        return r.json()
    else:
        return "there was an error"


if __name__ == "__main__":
    print(sys.argv)
    name = "unknown"
    if len(sys.argv) > 1:
        name = sys.argv[1]
    response = send(name, "aldianu.com")
    print(response)
