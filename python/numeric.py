# division
print(9 / 5) #=> 1.8

# floor division
print(9 // 5) #=> 1

# ZeroDivisionError
try:
  print(5 / 0)
except ZeroDivisionError as e:
  print("ZeroDivisionError has occured.")

# two to the power of five
print(2 ** 5) #=> 32

# float
print(float(True)) #=> 1.0
print(float(False)) #=> 0.0
print(float('1.0e4')) #=> 10000.0

# float to int
print(int(98.6)) #=> 98
