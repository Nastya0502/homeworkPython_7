def rhyme(words):
    my_list = words.split()
    result = []
    volwes = 'уеыаоэяию'
    for i in my_list:
        counter = 0
        for j in i:
            if j in volwes:
                counter += 1
        result.append(counter)
    result = set(result)
    if len(result)==1:
        print('Парам пам-пам')
    else:
        print('Пам парам')