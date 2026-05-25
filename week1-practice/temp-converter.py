#welcome user to convertor 
#ask for name 
#say hello name 
# ask user for degrees in celcius 
#convert to Fahrenheit and store 
# print answer in Fahrenheit 

print("Hello! Welcome to our temperature converter")
name = input("Before we get started what's your name? ")
print("Welcome " + name + " Let's get started!")
celsius = float(input("What temperature would you like to convert? "))
c = str(celsius)
fahrenheit = str((celsius * 1.8) + 32)
print(c + " degrees celsius is = " + fahrenheit + " fahrenheit")
