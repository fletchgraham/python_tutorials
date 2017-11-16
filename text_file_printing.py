import os

with open("my_text.txt", mode="w", encoding="utf-8") as my_file:
    my_file.write("random random text text\nLorem Ipsum Pipsum Snipsum\nData data lalala")

with open("my_text.txt", encoding="utf-8") as my_file:
    line_num = 1
    while line_num >= 1:
        my_line = my_file.readline()

        if not my_line:
            break

        words = my_line.split()
        letter_count = 0
        for i in words:
            letter_count += len(i)

        av_word_len = letter_count / len(words)

        print("{} : {} : {} : {}".format(line_num, my_line[:-1], len(words), av_word_len))

        line_num += 1

