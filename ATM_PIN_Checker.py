Pin = 1234

for i in range(3):
    Password = int(input("Enter your Pin: "))

    if Password == Pin:
        print("Access Granted, Welcome!!")
        break
    else:
        print("Wrong Pin (Attempt", i + 1, "/3)")

if Password != Pin:
    print("Account is Locked after 3 Attempts")
