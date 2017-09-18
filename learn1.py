# -*- coding:utf-8 -*-  

import copy
import pyperclip
import sys
import re

spam = ["H", "G", "F", "E", "D", "C", "B"]
cheese = copy.copy(spam)
cheese[1] = "A"
temp = cheese[1]
del cheese[1]

print(spam)
print(cheese)


phoneNumRe = re.compile(r"([0-9-]+)")

mo = phoneNumRe.search("My number is 415-555-4242.415-333-4242.415-222-4242.")
print(mo.group(1))