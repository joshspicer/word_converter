import sys


def replace_str_index(text, index=0, replacement=''):
    return '%s%s%s' % (text[:index], replacement, text[index+1:])


starting_word = sys.argv[1]
target_word = sys.argv[2]
intermediate_word = ""
alphabet = "abcdefghijklmnopqrstuvwxyz"

print("starting word is:", starting_word)
print("target word is:", target_word)

word_list_file = open("four_letter_words.txt", "r")
word_list = word_list_file.read()

# Start
intermediate_word = starting_word

while intermediate_word != target_word:
    for position in range(0, 4):
        for letter in alphabet:
            '''
            AALK
            BALK
            CALK
            DALK
            ...
            TALK
            ...
            ZALK
            '''

            # Grabs the target word's letter at the current position
            target_word_letter = target_word[position]

            wildcard_word = replace_str_index(
                intermediate_word, index=position, replacement=letter)

            if wildcard_word in word_list \
                    and letter == target_word_letter \
                    and wildcard_word != intermediate_word:
                print(intermediate_word, "->", wildcard_word)
                intermediate_word = wildcard_word
