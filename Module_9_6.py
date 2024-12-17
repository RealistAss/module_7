def all_variants(text):
    for i in range(1, len(text) + 1):
        for n in range(len(text) - i + 1):
            yield text[n:n + i]


a = all_variants("abc")

for n in a:

    print(n)