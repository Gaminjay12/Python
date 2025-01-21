#!/usr/bin/env python

import os
os.system("clear")

print("====================================")
print("=         UTILITY                 =")
print("====================================")
while True:
    
    user_input = input("> ")
    if user_input == "exit":
        break
    if user_input == "help":
        import os
        os.system("nvim -mR /usr/local/share/utility.txt")
    