#This cod is some function print( '' .format())



prof = ('She', 'nurse', 'He', 'builder')



print('{0[0]} is a {0[1]}.'.format(prof))

print('{0[2]} is a {0[3]}.'.format(prof))

print()

print('{0[0]:>20} is a {0[1]}.'.format(prof))

print('{0[2]} is a {0[3]:-<20}.'.format(prof))

print()



number = ( 33, 55, 77)



print('int: {0[0]} --> bin: {0[0]:b}'.format(number))

print('int: {0[1]} --> oct: {0[1]:o}'.format(number))

print('int: {0[2]} --> hex: {0[2]:x}'.format(number))

print('percent: {0[1]}/{0[2]} --> {1:.2%}'.format(number,number[1]/number[2]))
