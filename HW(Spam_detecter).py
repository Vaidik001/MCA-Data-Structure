"""
h1) - The Spam Detector (Search in Stream) – linear search

A cybersecurity intern at a startup is building a basic spam filter.
 Incoming emails are checked against a blacklist of known spam sender IDs.
 The blacklist has no order.
"""

#linear search

blacklist = ["scam99@gmail.com",
            "skim33@gmail.com",
            "abc@yahoo.com",
            "duplicate@gmail.com",
            "win@lottery.com"]

#method for spam detecter
def spam_det(email):
    for i in blacklist:
        if i==email:
            print(email, "is a Spam Sender.")
            return
    print(email, "is Not a Spam Sender.")

#Dry Run
spam_det("win@lottery.com")