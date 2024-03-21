import random
def generate():
  number = ''
  for i in range(0,10):
      number += str(random.randint(0,9))
  return number

def menu():
  ch = 'y'
  while ch == 'y':
    print('\n1)Take phone number')
    print('2)delete phone number')
    choice = int(input('Enter your choice: '))
    if choice == 1:
        name = input('\nEnter your name: ')
        given = phone_numbers.pop(-1)
        print('Your number is ', given)
        name_tup = (name, given)
        given_numbers.append(name_tup)
    elif choice == 2:
        num = int(input('\nEnter your number: '))
        phone_numbers.append(num)
        print('Deleted')
    print('\nGiven number: ', given_numbers)
    ch = input('Do you want to continue(y/n): ')

phone_numbers = []
given_numbers = []
for i in range(10):
  num = generate()
  phone_numbers.append(num)
#print(phone_numbers)
menu()
