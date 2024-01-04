slowPlayback = input("Enter your sentence: ")
for x in slowPlayback:
    if x == " ":
        print("...", end = "")
    else:
        print(x, end = "")
print()
print(slowPlayback.replace(" ", "..."))