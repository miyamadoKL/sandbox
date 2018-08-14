# repeat
start = 'Na ' * 4 + '\n'
middle = 'Hey ' * 3 + '\n'
end = 'Goodbye.'
print(start + start + middle + end)

# extract char
letters = "".join([chr(i) for i in range(ord('a'), ord('z') + 1)])
print(letters == "abcdefghijklmnopqrstuvwxyz")
print(letters[1]) #=> b
print(letters[-3]) #=> x
print(letters[20:]) #=> uvwxyz
print(letters[12:15]) #=> mno
print(letters[-3:]) #=> xyz
print(letters[1:18:5]) #=> bglq
print(letters[-1::-1]) #=> zyx....cba

# replace
name = 'Mario brothers'
print(name.replace('Mario', 'Luigi'))
