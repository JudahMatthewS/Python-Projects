a=input("Enter Celsius or Fahrenheit: ")

if a == "c":
    val = float(input("Enter Celsius: "))
    formula = (9/5*(val))+32
    print("Fahrenheit: ",formula)
else:
    val = float(input("Enter Fahrenheit: "))
    formula = 5/9*(val-32)
    print("Celsius: ",formula)
