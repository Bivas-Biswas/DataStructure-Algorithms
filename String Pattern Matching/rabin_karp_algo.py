


def search(pattern, text, q):
    m = len(pattern)
    n = len(text)
    p = 0  # hash value for pattern
    t = 0  # hash value for txt
    h = 1
    i = 0
    j = 0
    d = 10
    # the value of h would be "pow(d, M-1) % q"
    for i in range(m - 1):
        h = (h * d) % q
    print(h)

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    # print(p)
    # print(t)

    for i in range(n-m+1):
        if p == t:
            for j in range(m):
                if text[i+j] != pattern[j]:
                    break
            j += 1
            if j == m:
                print("Pattern is found at position: " + str(i))

        if i < n-m:
            t = (d*(t-ord(text[i])*h) + ord(text[i+m])) % q
            if t < 0:
                t = t+q


text = "mississippi"

# print(len(text))
pattern = "mississippi"
q = 13
search(pattern, text, q)
