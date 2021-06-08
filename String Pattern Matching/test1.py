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


s = "babbb"
ele = cretelps(s)
print(ele)
ans = {}
for i in range(len(ele)):
    if ele[i] != 0:
        ans += s[i]

print(ans)
