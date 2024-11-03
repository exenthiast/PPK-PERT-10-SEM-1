def transform_word(word):
    uppercase_count = 0
    lowercase_count = 0
    
    for c in word:
        if c.isupper():
            uppercase_count += 1
        elif c.islower():
            lowercase_count += 1
    
    if uppercase_count > lowercase_count:
        return word.upper()
    elif lowercase_count > uppercase_count:
        return word.lower()
    else:
        return word.upper() if word[-1].isupper() else word.lower()

def transform_sentence(sentence):
    words = sentence.split()
    transformed_words = [transform_word(word) for word in words]
    return ' '.join(transformed_words)


kalimat = input("Masukkan kalimat: ")
tranformasi = transform_sentence(kalimat)
print("Kalimat setelah transformasi:", tranformasi)
