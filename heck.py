import os
import platform
import getpass

y = "y"
Y = "Y"
n = "n"
N = "N"
def createNewConnection(name, SSID, key):
    config = """<?xml version=\"1.0\"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>"""+name+"""</name>
    <SSIDConfig>
        <SSID>
            <name>"""+SSID+"""</name>
        </SSID>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>auto</connectionMode>
    <MSM>
        <security>
            <authEncryption>
                <authentication>WPA2PSK</authentication>
                <encryption>AES</encryption>
                <useOneX>false</useOneX>
            </authEncryption>
            <sharedKey>
                <keyType>passPhrase</keyType>
                <protected>false</protected>
                <keyMaterial>"""+key+"""</keyMaterial>
            </sharedKey>
        </security>
    </MSM>
</WLANProfile>"""
    if platform.system() == "Windows":
        command = "netsh wlan add profile filename=\""+name+".xml\""+" interface=Wi-Fi"
        with open(name+".xml", 'w') as file:
            file.write(config)
    elif platform.system() == "Linux":
        command = "nmcli dev wifi connect '"+SSID+"' password '"+key+"'"
    os.system(command)
    if platform.system() == "Windows":
        os.remove(name+".xml")

def connect(name, SSID):
    if platform.system() == "Windows":
        command = "netsh wlan connect name=\""+name+"\" ssid=\""+SSID+"\" interface=Wi-Fi"
    elif platform.system() == "Linux":
        command = "nmcli con up "+SSID
    os.system(command)

def displayAvailableNetworks():
    if platform.system() == "Windows":
        command = "netsh wlan show networks interface=Wi-Fi"
    elif platform.system() == "Linux":
        command = "nmcli dev wifi list"
    os.system(command)

try:
    displayAvailableNetworks()
    option = input("New connection (y/N)? ")
    if option == n or option == N:
        name = input("Name: ")
        connect(name, name)
        print("If you aren't connected to this network, try connecting with correct credentials")
    elif option == y or option == Y:
        name = input("Name: ")
        key = getpass.getpass("Password: ")
        createNewConnection(name, name, key)
        connect(name, name)
        print("If you aren't connected to this network, try connecting with correct credentials")
except KeyboardInterrupt as e:
    print("\nExiting...")
You have to enter the password yourself in this script.
In this line

key = getpass.getpass ("Password:")
I should switch "Password:" with variable that the script would try to search for until it is successful...
I found a script to find the password and completed it. The only problem is that in this script the program knows the value of the password. With each attempt, he can check if it matches the correct password.

import itertools
import string

def guess_password(real):
    chars = string.ascii_lowercase + string.digits
    attempts = 0
    for password_length in range(8, 9):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            if guess == real:
                return 'password is {}. found in {} guesses.'.format(guess, attempts)
            print(guess, attempts)

print(guess_password('abc'))
