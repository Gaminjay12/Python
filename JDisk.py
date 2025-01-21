

print("JDisk (V0.1A)")
while True:
    user_input = input("> ")
    if user_input == "q":
        break
    if user_input == "l":
        import os
        os.system("lsblk")
