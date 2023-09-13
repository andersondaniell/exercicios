# Print a message once the condition is false.

i = 1
while i < 6:
    print(i)
    i += 1
    if i == 6:
        break
else:
    print("I is no longer less than 6")