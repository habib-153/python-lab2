jerseys = input().split()
j_numbers = [int (x) for x in jerseys]
duplicate = []
not_dupli = []
for i in j_numbers:
    if i in not_dupli:
        if i not in duplicate:
            duplicate.append(i)
    else:
        not_dupli.append(i)
if duplicate:
    for j in duplicate:
        print(f"Duplicate jersey numbers: {j}", end=" ")
    print()
else:
    print("No duplicate")