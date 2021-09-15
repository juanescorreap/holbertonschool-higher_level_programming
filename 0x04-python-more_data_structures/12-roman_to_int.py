#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) == False or roman_string == None:
        return(0)
    else:
        roman_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 100}
        sum = 0
        for i in range(len(roman_string) - 1):
            if roman_n[roman_string[i]] < roman_n[roman_string[i + 1]]:
                    sum = sum - roman_n[roman_string[i]]
            else:
                    sum = sum + roman_n[roman_string[i]]
        sum = sum + roman_n[roman_string[-1]]
        return(sum)
