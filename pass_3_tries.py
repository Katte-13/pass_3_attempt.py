"""Log in 3 tries only!  """

correct_password = 'Senat'
name = input("Enter your name: ")
surname = input("Enter your surname: ")
password = input('Enter the pass: ')

for tries in range(1,4):  # set-up 3 rounds of trying
    if correct_password != password:
        if tries <=2 :
                     password = input("That password is incorect. Try again: ")
        else:
            message1 = ('%s %s, you entered an incorrect password three times in a row, you are blocked!' % (name, surname))
            print (message1)
    elif correct_password == password:
         message = ('Hi, %s %s you are logged in.' % (name, surname))
         print (message)
         break
    
                    

