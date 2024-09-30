from collections import Counter
import re

def ngrams(n, text):
    for i in range(len(text) - n + 1):
        if not re.search(r'\s', text[i:i+n]):
            yield text[i:i+n]

def decrypt(text, key):
    result = []
    for char in text:
        if char.upper() in key:
            result.append(key[char.upper()].lower())
        else:
            result.append(char)
    return ''.join(result)

substitution_key = {
    'N': 'E',
    'Y': 'T',
    'V': 'A',
    'T': 'H',
    'X': 'O',
    'U': 'N',
    'H': 'R',
    'B': 'F',
    'Q': 'S',
    'I': 'L',
    'M': 'I',
    'R': 'G',
    'P': 'D',
    'C': 'M',
    'S': 'K',
    'Z': 'U',
    'A': 'C',
    'D': 'Y',
    'K': 'X',
    'L': 'W',
    'E': 'P',
    'G': 'B',
    'F': 'V',
    'J': 'Q',
    'O': 'Z'
}


with open('ciphertext.txt') as f:
    text = f.read()

TOP_K = 20
N_GRAM = 1
for N in range(N_GRAM):
    print("-------------------------------------")
    print("{}-gram (top {}):".format(N+1, TOP_K))
    counts = Counter(ngrams(N+1, text))       
    sorted_counts = counts.most_common(TOP_K)  
    for ngram, count in sorted_counts:                  
        print("{}: {}".format(ngram, count))   

decrypted_text = decrypt(text, substitution_key)

print("\nDecrypted Text:\n")
print(decrypted_text)
