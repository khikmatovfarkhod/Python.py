vowels= "HELLOarq3raQWERQI"
name = "WorldQ2EQEQIS"
result = '' #empty string

for letter in name:
    if letter in vowels:
        result += letter
    print("the result is:", result)
