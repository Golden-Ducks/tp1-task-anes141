#Djelili Anes Abdessamad
num2word = {
    "0": "zero", "1": "one", "2": "two", "3": "three", "4": "four",
    "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine", "10": "ten"
}


def normalize_text(text):

    text = text.lower()

    words = text.split()

    normalized_words = []
    for w in words:

        if w.isdigit() and w in num2word:
            normalized_words.append(num2word[w])
        else:
            normalized_words.append(w)


    return " ".join(normalized_words)



D1 = "Today she cooked 4 bourak. Later, she added two chamiyya and 1 pizza."
D2 = "Five pizza were ready, but 3 bourak burned!"
D3 = "We only had 8 chamiyya, no pizza, and one tea."
D4 = "Is 6 too much? I ate nine bourak lol."

docs = [D1, D2, D3, D4]

for i, d in enumerate(docs, 1):
    print(f"D{i} normalized: {normalize_text(d)}")
