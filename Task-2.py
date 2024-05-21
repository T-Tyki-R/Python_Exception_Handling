# The Recipe Ratio

def calculate_adjustment(num1, num2):
    quo = 1
    try:
        quo /= num1 / num2
    except ZeroDivisionError:
        print("Zero cannot be divided... please pick numbers greater than 0")
    else:
        return quo

user_recipe = input("What recipe are you going to make?: ")
print (f"What is the original amount {user_recipe.lower()} serves?: ")
try:
    user_orginal_amount = int(input("The amount is: "))
except ValueError:
    print("The serving amount must be a number")
else:
    try:
        user_serve_amount = int(input("What amount are you trying to serve? "))
    except ValueError:
        print("The serving amount must be a number")
    else:
        try:
            adjust_recipe = calculate_adjustment(user_orginal_amount, user_serve_amount)  
        except: 
            pass
        else:
            if adjust_recipe != None:
                print(f"The serving amount you'd want is about {adjust_recipe:.1f} per person.")
            else:
                print("The recipe's serving size per person shouldn't be zero or less.")
    finally:
        print("Glad I was able to help you with your recipe! Have a great time cooking.")

