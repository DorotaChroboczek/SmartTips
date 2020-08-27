with open('Tolkien', 'r') as f:
    file_content = f.read()

words = file_content.split(' ')
word_count = len(words)
print(words)
print(word_count)

    #menager kontestu