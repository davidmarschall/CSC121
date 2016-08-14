# This program sums unlimited user-supplied integers between 1 and 100
# greeting
print()
print('This program sums integers between 1 and 100.\nEnter as many integers as you would like to sum,\nand then press Enter for the total.')
print()

#init
terminate = False
empty_str = ''
sum = 0

# while not terminate:
#     user_num = int(input('Enter an integer between 1 and 100: '))
#     if user_num < 1 or user_num > 100:
#             print('Invalid input -- Enter an integer between 1 and 100: ')
#     elif user_num >= 1 and user_num <= 100:
#             sum = sum + user_num
#     elif user_num == empty_str:
#             print('The total is ', sum)
#             terminate = True
# print('Done')


# while not terminate:
#     user_num = input('Enter an integer between 1 and 100: ')
#     if int(user_num) < 1 or int(user_num) > 100:
#             print('Invalid input -- Enter an integer between 1 and 100: ')
#     elif int(user_num) >= 1 and int(user_num) <= 100:
#             sum = sum + int(user_num)
#     elif user_num == empty_str:
#             print('The total is ', sum)
#             terminate = True
# print('Done')


# while not terminate:
#     user_num = input('Enter an integer between 1 and 100: ')
#     if user_num == empty_str:              # must come first; if "float" line comes first, cannot deal with empty string
#             print('The total is ', sum)
#             terminate = True
#     elif float(user_num) % 1 != 0 or int(user_num) < 1 or int(user_num) > 100:  # to eliminate non-integers, negative numbers, and numbers over 100
#             print('Invalid input')
#     elif int(user_num) >= 1 and int(user_num) <= 100:  # the adding part
#             sum = sum + int(user_num)


while not terminate:
    user_num = input('Enter an integer between 1 and 100: ')
    if user_num == empty_str:              # must come first; if "float" line comes first, cannot deal with empty string
            print('The total is ', sum)
            terminate = True
    elif float(user_num) % 1 != 0 or int(user_num) < 1 or int(user_num) > 100:  # to eliminate non-integers, negative numbers, and numbers over 100
            print('Invalid input')
    else:                                       # the adding part
            sum = sum + int(user_num)

print('Bye')
print()
