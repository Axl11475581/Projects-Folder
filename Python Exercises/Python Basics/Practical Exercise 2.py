
our_password = "pass 123"
your_answer = ""
tries = 0
max_tries = 5
max_T_output = "Not Reached"

while your_answer != our_password and max_T_output != "Reached":
    if tries > max_tries:
        your_answer: input("What is the password?")
        tries = tries + 1
    else:
        max_tries = "Reached"

    if max_tries == "Reached":
        print("Account blocked")
    else:
        print("Acces granted")
