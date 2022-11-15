def censor(text, word):
    words = text.split()
    final = []
    for i in words:
        if i == word:
            final.append("*"*len(word))
        else:
            final.append(i)
    return " ".join(final)
