def get_num_words(text):
    return len(text.split())


def get_letter_count(text):
    count = {}
    for c in text.lower():
        if count.get(c, None) == None:
            count[c] = 1
        else:
            count[c] += 1
    return count


def sort_letter_count(count: dict[str, int]):
    x = []
    for key, value in count.items():
        x.append({"char": key, "num": value})
    x.sort(key=lambda x: x["num"], reverse=True)
    return x
