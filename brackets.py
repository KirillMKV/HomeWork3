brackets_string = input('Input string of brackets: ')
stack = []
correct_sequence = True

# CHECK: does string consist of brackets only?
for character in brackets_string:
    if character not in '()[]{}':
        print('String should contain brackets only!')
        correct_sequence = False
        break

for char in brackets_string:
    if char in "([{":
        stack.append(char)
    elif char in ")]}":
        if not stack:
            good_sequence = False
            break
        open_bracket = stack.pop()
        if open_bracket == '(' and char == ')':
            continue
        if open_bracket == '[' and char == ']':
            continue
        if open_bracket == '{' and char == '}':
            continue
        correct_sequence = False
        break
if correct_sequence == True and len(stack) == 0:
    print('Bracket sequence is correct')
else:
    print('Bracket sequence is wrong')