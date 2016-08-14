# This program creates a table of the integers from 1 to 100 in ten rows

#init
counter = 1
colummn = 1
column_width = 3
blank_char = ' '

print()
while counter <= 100:
    if counter < 10:        # one-digit number print
        print(format(blank_char, '2') + str(counter), end='')
    elif counter < 100:     # two-digit number print
        print(format(blank_char, '1') + str(counter), end='')
    else:                   # three-digit number print
        print(str(counter), end='')

    if colummn < 10:        # to get return to new row for next ten
        colummn = colummn + 1
    else:
        colummn = 1
        print()

    counter = counter + 1

print()
