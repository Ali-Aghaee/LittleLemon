
with open('littlelemon/ab.txt', 'r') as inF:
    for line in inF:
        for i in line:
            if i != ' ' and i!='\n':
                try:
                    int(i)
                except:
                    print('yes:'+ i)