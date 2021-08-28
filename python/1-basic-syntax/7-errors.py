while False:
    try:
        x=int(input('Please enter a valid number:'))
        break
    except ValueError:
        print("Oops a number wasn't entered!")


raise NameError("Hi There")