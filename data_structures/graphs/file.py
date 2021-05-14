with open('no_of_islands.py') as fh:
    count = 0
    text = fh.read()
    for character in text:
        if character.isupper():
            count += 1
    print(count)