import random

consonants = "bcdfghjklmnpqrstvwxyz"
vowels = "aeiou"

def generate_japanese_sounding_word(word_length=5):
    word = ""
    for i in range(word_length):
        if i % 2 == 0:
            word += random.choice(consonants)
        else:
            word += random.choice(vowels)
    return word

# Generate 10 random Japanese-sounding words
for _ in range(10):
    print(generate_japanese_sounding_word())
