min_freq = Counter(words[0])
        for word in words:
            min_freq &= Counter(word)
        return list(min_freq.elements())
