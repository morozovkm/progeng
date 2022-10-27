csvfile = open('data.csv','r')

for line in csvfile:
    split_line = line.split(';')

    print(f'Мое имя: {split_line[0]}, фамилия - {split_line[1]} и телефон - {split_line[2]}')
