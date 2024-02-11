primaries = ['red', 'yellow', 'blue']
answer = input('Enter a primary color:').lower().strip()
if answer in primaries:
    print('You entered', answer1)
else:
    while answer1 not in primaries:
        print("Sorry, that's not a primary color. Please try again.")
        answer1 = input('Enter a primary color:').lower() .strip()
    print('You entered', answer1)

answer2 = input('Enter a second primary color:').lower().strip()
while answer2 == answer1 or answer1 not in primaries:
    if answer2 not in primaries:
        print("Sorry, that's not a primary color. Try again.")
        answer2 = input('Enter another primary').lower() .strip()
    else:
        print('That was the same color as before. Please try again')
        answer2 = input('Enter a different primary color.').lower() .strip()
if answer2 in primaries:
    print('You entered', answer2)

mixture = answer1 + answer2

secondaries = {
    'redyellow' : 'orange',
    'yellowred' : 'orange',
    'redblue' : 'purple',
    'bluered' : 'purple',
    'yellowblue' : 'green',
    'blueyellow' : 'green'
}

print(answer1, 'mixed with', answer2, 'turns into', secondaries[mixture])
