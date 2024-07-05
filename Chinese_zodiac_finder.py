zs = ['MONKEY', 'ROOSTER', 'DOG', 'PIG', 'RAT', 'OX', 'TIGER', 'RABBIT', 'DRAGON', 'SNAKE', 'HORSE', 'SHEEP']  # zs--zodiac sign
zc = ['Fun & Active', 'Independent & Practical', 'Faithful & Kind', 'Loving & Tolerant', 'Quick-witted & Smart',
      'Patient & Kind', 'Authoritative & Emotional', 'Popular & Compassionate', 'Energetic & Fearless',
      'Generous & Smart', 'Energetic & Independent', 'Shy & Kind']  # zc--zodiac character
print('*' * 25)
print('-' * 20)
name_input = input('Please enter your name: ')
print('-' * 20)
print(f'Hey {name_input}, welcome to the Chinese Zodiac Finder!')
print('*' * 25)
while True:
    user_input = input('Enter your year of birth or Q to quit: ')    
    if user_input.lower() == 'q':
        print('*' * 30)
        print(f'再见, {name_input}!')
        print('*' * 30)
        break    
    try:
        yob = int(user_input)        #yob--year of birth
        if len(str(yob)) <= 4:
            cz = yob % 12           #cz--chinese zodiac
            print(f'Your birth year is ***{yob}***')
            print(f'Your Chinese zodiac number is: ***{cz}***')
            print(f'Your Chinese zodiac sign is: ***{zs[cz]}***')
            print(f'Your Chinese zodiac character is: ***{zc[cz]}***')
            print(f'{name_input}, you have such an amazing Chinese character!')
            print('*' * 25)
        else:
            print('!!!!Enter your year of birth in digits and less than or equal to 4 digits!!!!')
    except ValueError:
        print('!!!!Enter your year of birth as a valid number!!!!')
