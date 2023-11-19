# 8. Write a function that converts Celsius to Fahrenheit and vice versa.

def C_to_F(temp,reverse=False):
    if reverse:
        return (temp-32)*(5/9)
    return (9/5)*temp+32

temp_C = -40.0
print(f"{temp_C}°C ==> {C_to_F(temp_C)}°F")

temp_F = 98.6
print(f"{temp_F}°F ==> {C_to_F(temp_F,reverse=True)}°C")