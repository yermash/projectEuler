found = set()

for i in range(2, 101):
    for j in range(2, 101):
        found.add(i**j)

print(len(found))