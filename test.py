l = [
    "001101",
    "010110",
    "001011",
    "111001",
    "011100",
    "101000"
]

# OLD
print(*[int(s,2)for s in l])

# PROPOSED
print(*map(int($,2),l))

# ============================
print()
# ============================

# OLD
print(max(l, key=lambda x:x.count('1')))

# PROPOSED
print(max(l, key=str.count($,'1')))

# ============================
print()
# ============================


names = [
    "Stephen",
    "Harry Potter",
    "Hermoine",
    "Ron Weasley",
    "Dumbledore",
    "Snape",
    "Filch"
]

indexes = range(len(names))

# OLD
d = {n: i for i, n in enumerate(names)}
print(*map(d.get, sorted(d)))

# PROPOSED
print(*sorted(indexes, key=names[$]))
