terminate = False
empty_str = ''
pos_count = 0
neg_count = 0

while not terminate:
    user_num = input('Enter any integer, positive or negative, except zero: ')

    if user_num == empty_str:
        print('You have entered', pos_count, 'positive integers.')
        print('You have entered', neg_count, 'negative integers.')
        terminate = True

    elif float(user_num) % 1 != 0 or int(user_num) == 0:
        print('INVALID INPUT')

    elif int(user_num) > 0:
        pos_count = pos_count + 1

    else:
        neg_count = neg_count + 1

print('Bye')
