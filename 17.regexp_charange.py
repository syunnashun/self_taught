# 第17章のチャレンジ
# http://tinyurl.com/jmlkvxm

import re

with open("zen.txt", "r") as h:
    zen = h.read()
    print(zen)

m = re.findall("Dutch", zen, re.IGNORECASE)
print(m)

stings = "Arizona 479, 501, 870. California 209, 213, 650."
m = re.findall("\d", stings, re.IGNORECASE)
print(m)

line = "The ghost that says boo haunts the loo"
m = re.findall(".oo", line, re.IGNORECASE)
print(m)