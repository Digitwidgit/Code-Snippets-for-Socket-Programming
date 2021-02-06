

def passwd():


    lgin = input("Please enter your password to login: ..")

    mypass = "Password"

    if lgin !=mypass:


        
        print("Bad password!")
        passwd()

    else:

        print("Welcome ... >")

passwd()
