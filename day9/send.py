import sys
import requests
from formatting import format_msg
from datetime import datetime
from send_mail import send_mail

def send(name, website=None, to_email = None, verbose=False):
    assert to_email != None
    if website != None:
        msg = format_msg(myname=name, mywebsite=website)
    else:
        msg = format_msg(myname=name)
    if verbose:
        print(name, website, to_email)
    #send mail
    try:
        send_mail(text=msg, to_emails=[to_email], subject="test", html=None)
        send=True
    except:
        send=False
    
    return send


if __name__ == "__main__":
    print(sys.argv)
    name = "unknown"
    if len(sys.argv) > 1:
        name = sys.argv[1]
    email = None
    if len(sys.argv)>2:
        email=sys.argv[2]
    response = send(name, to_email=email, verbose=True)
    print(response)
