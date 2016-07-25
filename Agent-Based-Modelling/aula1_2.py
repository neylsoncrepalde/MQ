#Programming a max function
def my_max(a, b):
    print("Which number is bigger?")
    if a > b:
        print(a)
    elif a == b:
        print("They're equal.")
    else:
        print(b)

def ball():
    print("Do you have the ball? y or n")
    yes = input()
    if yes == "y":
        has_ball = True
    else:
        has_ball = False
    print("Are you tall? y or n")
    yes = input()
    if yes == "y":
        is_tall = True
    else:
        is_tall = False
    print("Are you a girl? y or n")
    yes = input()
    if yes == "y":
        is_girl = True
    else:
        is_girl = False

    if has_ball == True:    
        if is_tall == False:
            if is_girl==True:
                print("She has a ball")
            else:
                print("He has a ball")
        else:
            if is_girl==True:
                print("Tall girl has a ball")
            else:
                print("Tall boy has a ball")
    else:
        print("...")