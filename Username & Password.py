a=input("Enter Username : ")
b=int(input("Enter Pin : "))
if a=="Judah@123":
    print("Please Enter Your Passcode To Continue Mr",a)
    if b==2495:
        print("Welcome ! Mr.",a)
    else:
        print("Incorrect Passcode : ",b)
else:
    print("Invalid Username : ",b)