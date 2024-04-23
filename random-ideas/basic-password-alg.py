"""
Connor Finlay
Basic password program
"""
password = " "
valid_password = "false"
pin = 0
valid_pin = "false"



while valid_password == "false":
      print("What is the password?")
      password = str(input())

      if password == "Password17":
            valid_password = "true"
            print("Access Granted")

      else:
            valid_password = "false"
            print("Access Denied, please enter the correct password")
   
while valid_pin == "false":
      print("What is the pin?")

      pin = int(input())

      if pin == 1234 :
            valid_pin = "true"

            print("Access Granted, you are allowed into the computer")

      else:
            valid_pin == "false"
            print("Access Denied, the pin  must be 4 characters long")


