def rhyme(txt):
    ph = str.lower(txt).split()
    vowels = ['а','о','э','ы','у','я','ё','е','и','ю']
    vowels_count = []
    for i in ph:
        count = 0
        for k in i:
            for j in vowels:
                if j == k:
                    count += 1
        vowels_count.append(count)
    return len(set(vowels_count)) == 1

text = input("Введите фразу: ")
if rhyme(text):
    print('Парам пам-пам')
else:
    print('Пам парам')