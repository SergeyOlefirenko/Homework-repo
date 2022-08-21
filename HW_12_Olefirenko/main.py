# #Задание 1
f1 = open('file1.txt', mode='w',  encoding = 'utf-8')
f2 = open('file2.txt', mode='w', encoding='utf-8')
f1.write('миранда коля петя')
f2.write('василиса инокентий коля петя')
f1.close()
f2.close()
uncommonNames = []
with open('file1.txt', encoding="utf8") as f1:
    text1 = f1.readline()
    names1 = text1.split()
    print(names1)
with open('file2.txt', encoding="utf8") as f2:
    text2 = f2.readline()
    names2 = text2.split()
    print(names2)
for name in names1:
    if name not in names2 :
        uncommonNames.append(name)
for name in names2:
    if name not in names1:
        uncommonNames.append(name)
print(uncommonNames)
# Задание 2
reader = open('textfile.txt', mode='r', encoding='UTF-8')
text = reader.readlines()
reader.close()
print(text)
symbol_counter = 0
vowels_counter = 0
consonants_counter = 0

for line in text:
    symbol_counter += len(line)

line_counter = len(text)

print('Symbol_counter: ', symbol_counter)
print('line counter: ', line_counter)

vowels = ['a', 'o', 'i', 'e', 'u', 'y']
elements_counter = 0
digit_counter = 0
for line in text:
    for symbol in line:
        if symbol.lower() in vowels:
            vowels_counter += 1
        elif symbol.lower().isdigit():
            digit_counter += 1
        elif symbol.lower() not in [' ', ',', '.']:
            consonants_counter += 1
        elif symbol.lower() in [' ', ',', '.']:
            elements_counter += 1

print("vowels - ", vowels_counter)
print("consonants - ", consonants_counter)
print("elements - ", elements_counter)
print('digit_counter: ', digit_counter)

writer = open('newfile.txt', mode='w', encoding='UTF-8')
writer.write("vowels - " + str(vowels_counter)+'\n')
writer.write("consonants - " +str(consonants_counter)+'\n')
writer.write("elements - " + str(elements_counter)+'\n')
writer.write('digit_counter: ' + str(digit_counter)+'\n')

# Задание 3
reader = open('textfile.txt', mode='r', encoding='UTF-8')
text = reader.readlines()
reader.close()
print(text)
lines = []
line_counter = len(text)
for line in text[:-1]:
        lines.append(line)
print(lines)
writer = open('newfile.txt', mode='w', encoding='UTF-8')
writer.write(str(lines))
writer.close()
#Задание 4
reader = open('textfile.txt', mode='r', encoding='UTF-8')
text = reader.readlines()
reader.close()
print(text)
def funk_maxLine(textfile): #Не понимаю почему textfile светится серым
    with open('textfile.txt', 'r') as textfile:
        funk_maxLine = max((line.strip() for line in textfile))
    return funk_maxLine
print('Самая длинная строка в файле textfile.txt: ', (funk_maxLine('textfile.txt')))
#Задание 5
reader = open('textfile.txt', mode='r',  encoding = 'utf-8')
reader.close()
counter = 0
word = input('Input word: ')
with open('textfile.txt', encoding="utf8") as reader:
    for text in reader:
        names = text.lower().split()
        for text in names:
            if text == word:
                counter += 1
print('Quantity of words in text:',(counter))
#Задание 6
reader = open('textfile.txt', mode='r',  encoding = 'utf-8')
reader.close()
word = input('Input word: ')
word1 = input('Input word: ')
with open('textfile.txt', encoding="utf8") as reader:
    for arraytext in reader:
        names = arraytext.lower().split()
        for text in names:
            if text == word.lower():
                arraytext = arraytext.lower().replace(word, word1)
        print('Output:',(arraytext) , end='')



