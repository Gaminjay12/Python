import os
os.system("clear")
print("==================================")
print("=    JTool Manager               =")
print("==================================")
while True:
    user_input = input("> ")
    if user_input == "!install jutil":
        import os
        os.system("sudo cp jutil/jutil.py /usr/bin/jutil")
        os.system("sudo cp jutil/jutil.txt /etc/jutil.txt")
    if user_input == "!remove jutil":
        import os
        os.system("sudo rm /usr/bin/jutil")
        os.system("sudo rm /etc/jutil.txt")
    if user_input == "!exit":
        break
    if user_input == "!download/install jutil":
        print("Downloading Jutil")
        import os
        os.system("git clone https://github.com/Gaminjay12/BaseFiles")
        os.system("sudo mv BaseFiles/Python/Jtools/jutil/jutil.py /usr/bin/jutil")
        os.system("sudo mv BaseFiles/Python/Jtools/jutil/jutil.txt /etc/jutil.txt")
        os.system("rm -rf BaseFiles/")
        os.system("sudo chmod +x /usr/bin/jutil
    if user_input == "help":
        import os
        os.system("vim -mR help.txt")
        
