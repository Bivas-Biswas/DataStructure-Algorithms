def cretelps(p):
    lps = [0] * len(p)
    prefix = 0
    curr = 1
    while curr < len(p):
        if p[curr] == p[prefix]:
            lps[curr] = prefix + 1
            curr += 1
            prefix += 1
        else:
            if prefix == 0:
                lps[curr] = 0
                curr += 1
            else:
                prefix = lps[prefix - 1]
    return lps


def kmp(s, p):
    n, m = len(s), len(p)
    lps = cretelps(p)
    # print("lps", lps)
    sp, pp = 0, 0
    while sp < n:
        # print(sp, pp)
        if s[sp] == p[pp]:
            sp += 1
            pp += 1
        else:
            if pp == 0:
                sp += 1
            else:
                pp = lps[pp - 1]
        if pp == m:
            print("pattern found starting at ", sp - pp)
            print("pattern found starting at ", sp)
            pp = lps[pp - 1]


text = "pqerpqespqrpqespqespqef"
print(len(text))
pattern = "pqespqef"
kmp(text, pattern)
