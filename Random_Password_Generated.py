# To Generate to Random paswword way using python

import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "{}()?/@#$%^&*<>|"

all = lower + upper + number + symbols
length = 8

# password = "".join(random.sample(all,length))

for i in range(5):
    password = "".join(random.sample(all,length))
    print("Password:",password)