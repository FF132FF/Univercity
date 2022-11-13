from Unique_word_counter import Read_Save_Files as rsf


rsf.read_file()
FFFFFF = rsf.save_file('data.txt', rsf.read_file())
count = FFFFFF[0]
words = FFFFFF[1]
words = ' '.join(words)
words = words.replace(" ", "\n")
text_to_write = count, words
new_text = open("count.txt", mode = 'w+')
new_text.write(str(count))
new_text.write(str("\n===========\n"))
new_text.write(str(words))
