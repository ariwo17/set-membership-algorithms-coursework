import random
import string

NUM_WORDS = 50000
MIN_LENGTH = 1
AV_LOW_LENGTH = 2
AV_HIGH_LENGTH = 6
MAX_LENGTH = 12
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
VOWELS = 'aeiou'

output_file = "synthetic_data.txt"

SAMPLE_INTERVAL = 200
test_file = "../Archive(got from moodle)/testfiles/synthetic_test_search.txt"
test_words = set()

def generate_word(scarcity=0.05):
    limit = int(1 / scarcity)
    roulette = random.randint(0, int(1 / scarcity))
    if roulette == limit:
        length = random.randint(AV_LOW_LENGTH, AV_HIGH_LENGTH)
    else:
        length = random.randint(MIN_LENGTH, MAX_LENGTH)
    word = ''
    for i in range(length):
        if i % 2 == 1 or length == 1:
            word += random.choice(VOWELS)
        else:
            word += random.choice(CONSONANTS)
    return word

# Generate the words and write them to the output file
with open(output_file, 'w') as f:
    for i in range(NUM_WORDS):
        word = generate_word()
        f.write(word)
        if i % SAMPLE_INTERVAL == 0:
            test_words.add(word)
            test_words.add(generate_word())
        if i <= NUM_WORDS:
            f.write(' ')

test_words = list(test_words)
with open(test_file, 'w') as f:
    for i in range(len(test_words)):
        f.write(test_words[i])
        if i <= len(test_words):
            f.write('\n')

print(repr(test_words))
print(len(test_words))
