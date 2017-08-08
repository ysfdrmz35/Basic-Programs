text_content = ""
count = 0
opened = False
keyword = ""
try:
    file_name = input("Please enter the text file's name : ")
    textfile = open(file_name + ".txt", "r")
    text_content = str(textfile.read())
    opened = True
except FileNotFoundError:
    print("Can't find the file")

if opened:
    keyword = input("Please enter the word that you're looking for in the text : ")

    text_content_list = list(text_content)
    for char in text_content_list:
        if char == ".":
            text_content_list[text_content_list.index(char)] = ""
    text_content = ""
    for x in text_content_list:
        text_content += str(x)

    word_list = text_content.split(" ")

    for word in word_list:
        if word == keyword:
            count += 1
    print(count)