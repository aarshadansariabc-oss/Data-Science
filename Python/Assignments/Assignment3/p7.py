word = "hello how are you"
count = 0
for w in word:
    if w == ' ':
        count += 1

print(f"Total number of space in you string is {count}")

print(f"Total number of space in you string is {word.count(" ")}")
