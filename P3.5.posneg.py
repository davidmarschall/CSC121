# This program counts the number of user-supplied positive and negative integers
# terminate and empty_string to terminate program
terminate = False
empty_str = ''
# init
pos_count = 0
neg_count = 0

print()
while not terminate:
    user_num = input('Enter any integer, positive or negative, except zero: ')

    if user_num == empty_str:
        print()
        print('You have entered', pos_count, 'positive integers.')
        print('You have entered', neg_count, 'negative integers.')
        terminate = True

    # I'm sure I'll learn a better way to eliminate non-integers
    elif float(user_num) % 1 != 0 or int(user_num) == 0:
        print('INVALID INPUT')

    elif int(user_num) > 0:
        pos_count = pos_count + 1

    else:
        neg_count = neg_count + 1

print()
print('Bye')
print()
