# Program to convert temperature into Celsius or Fahrenheit where Formula c/5 = (f-32)/9
# where c = temperature in Celsius and f = temperature in Fahrenheit

temp = input("Input the temperature you like to convert (e.g., 25C or 77F): ")
degree = int(temp[:-1])
i_convention = temp[-1]

if i_convention.upper() == "C":
    result = int(round((9 * degree) / 5 + 32))
    o_convention = "Fahrenheit"
elif i_convention.upper() == "F":
    result = int(round((degree - 32) * 5 / 9))
    o_convention = "Celsius"
else:
    print("Input proper convention (C for Celsius, F for Fahrenheit).")
    quit()

print("The temperature in", o_convention, "is", result, "degrees.")
