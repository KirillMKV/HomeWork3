from pickle import NONE


def rom_to_dec(roman_number):
    # creating dictionary containing values of roman numerics in decimal system, ascending
    roman_numbers_values = {'I': 1, 'V': 5,
             'X': 10, 'L': 50,
             'C': 100, 'D': 500,
             'M': 1000}
    roman_number = roman_number.upper()
    
    # CHECK: is input roman number?
    for letter in roman_number.upper():
        if roman_numbers_values.get(letter) == None:
            return print ('You should enter roman number!' )

    ''' logics: if previous roman numeric has higher value then the next one, we should add it's value to result.
    if it has lower  - substract from result'''
    
    result = 0
    for i in range (len(roman_number) - 1):
        numeral = roman_number[i]
        next_numeral = roman_number[i+1]
        if roman_numbers_values[numeral] < roman_numbers_values[next_numeral]:
            result -= roman_numbers_values[numeral]
        else:
            result += roman_numbers_values[numeral]
    result += roman_numbers_values[roman_number[-1]]
    print (result)

roman = input("Enter roman number: ")
rom_to_dec(roman)