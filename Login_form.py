# simple console based login form using Python
----------------------------------------------

def login_form(username,password):
  # Here ,username and password match it returns the Valid.
    if username == "bhargav" and password == "12345":
        return "Valid"
    else:
      # username and password not matche it retuns the Invalid username and password.
        if username !='bhargav' and password !='12345':
            return 'Invalid username and password'
        elif username !='bhargav':    # username not matched it returns the Invalid username.
            return 'Invalid username'
        elif password !='12345':       # username not matched it returns the Invalid Password.
            return 'Invalid password'
username = str(input("Enter your user name :").lower().strip())
password = input("Enter your password :").strip()    
print(login_form(username,password))

#------------------------------------------------------------------------------------------------
@ strip - strip method is used to remove the spaces from both sides i.e[left and right].
  -----
@ if yoù want to remove only from left side -lstrip().

@ if yoù want to remove only from left side -rstrip().

@ lower()-lower method is used to convert the uppercase into lowercase.
