import math
# Exceptional Weather Forecast

def f_to_c_conversion(num):
    try:
       num = (num - 32) * 5 / 9
    except ValueError:
         print("Sorry, the temperture can only be a numerical input.")
    else:
        return num

print("What's the weather in your area at the moment?")

try:
    user_f_temp= int(input("Type your temperture here: "))
except ValueError:
    print("Sorry, the temperture can only be a numerical input.")
else:
    user_temp = f_to_c_conversion(user_f_temp)
    print(f"In Celsius, the current temperture in your area is about {math.ceil(user_temp)} degrees!")
finally:
    print("Thank you for interacting with me! Have a good day.")
