geniuses = ["Jaden", "EJ", "Joseph", "Xavier"]

for genius in geniuses:
    print(genius)

answer = input("Do you want me to print the list again? Y/N")
while answer == "Y":
    for genius in geniuses:
        print(genius)
    answer = input("Do you want me to print the list again? Y/N")