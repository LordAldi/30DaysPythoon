
msg_template = """
Hello {name},
thanks for joining {website}. We are very happy
to have you with us
"""


def format_msg(myname="justin", mywebsite="cfe.net"):
    mymsg = msg_template.format(name=myname, website=mywebsite)
    print(mymsg)
    return mymsg
