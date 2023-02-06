binary_string = input ("Enter 8-bit binary number:\n")
power = 7
decimal_number = 0
i = 0
while i < len(binary_string):
    if binary_string[i] == "1":
        decimal_number += (2**power)
    power -= 1
    i += 1
print ("Decimal:", decimal_number)