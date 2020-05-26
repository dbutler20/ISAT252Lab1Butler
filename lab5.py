"""
Lab 5
"""
#3.1
alien_color= 'green'
if alien_color == 'green':
    print('You just earned 5 points')
    
#3.2
alien_color='green'
if alien_color == 'green':
    print('You got 5 points')
else: 
    print('You got 10 points')

#3.3
favorite_fruits=['Oranges','Peaches','Pineapples']
if 'Oranges' in favorite_fruits:
    print('You really like oranges!')
if 'Peaches' in favorite_fruits:
    print('You really like peaches!')
if 'Pineapples' in favorite_fruits:
    print('You really like pineapples!')
if 'Apples' in favorite_fruits:
    print('You really like apples!')
if 'Cherries' in favorite_fruits:
    print('You really like cherries!')

#3.4
age=70
if age<=10:
    print('You are a kid')
elif age>=10 and age<=20:
    print('You are a teenager')
elif age>=20 and age<=65:
    print('You are an adult')
else:
    print('You are an elder')
    
    