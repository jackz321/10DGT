# ask user for width and loop until they
# enter a number that is more than zero

error = "please enter a number that is more than zero\n"
while true:

    Try:
        # ask the user for a number
        width = float(input("width: "))
    
        #check that the number is more than zero
        if width > 0:
            break
        else:
            print(error)

    expect value error:
        print(error)
        