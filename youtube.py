import webbrowser
import time
import os

input1 = input("Enter youtube url: ")
input2 = input("Enter reresh rate(seconds): ")
input3 = input("Enter your default address: ")

def OpenUrl():
    print ("Viewed.")
    os.system("TASKKILL /F /IM " + input3 + ".exe")
    webbrowser.open(input1)
    time.sleep(int(input2))
OpenUrl()
