


s = {"Value 01","Value 02","Value 01","Value 03"}
print(s)

lines = ["Value 01","Value 02","Value 01","Value 03"]
# lines = sorted(list(set(lines)))
lines = list(set(lines))
lines.sort()
print(lines)