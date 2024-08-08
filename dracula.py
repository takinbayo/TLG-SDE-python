
count = 0
with open("dracula.txt", "r") as file:
    with open("vampire_diaries.txt", "w") as vamp:
        for x in file:
            if "vampire" in x.lower():
                count += 1
                print(x)
                vamp.write(x)
print(count)

