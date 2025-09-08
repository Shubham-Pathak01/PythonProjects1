import textwrap
from tkinter.font import names

name = input("Enter your name: ")
profession = input("Enter your profession: ")
passion = input("Enter your passion: ")
emoji = input("Enter your favorite emoji: ")
website = input("Enter your website: ")

print("\n Choose your style: ")
print("1. simple lines")
print("2. vertical flairs")
print("3. Emoji sandwich")

style = input("Enter 1 2 or 3: ")

def generate_bio(style):
    if style == "1":
        return f"{emoji} {name} | {profession} \n {passion} \n {website}"
    elif style == "2":
        return f"{emoji} {name}\n {profession} \n {passion} \n {website}"
    elif style == "3":
        return f"{emoji * 3}\n {name} - {profession}\n {passion} \n {website} \n {emoji * 3}"

bio = generate_bio(style)

print("\n Your stylish bio:\n ")
print("*" * 50)
print(textwrap.dedent(bio))
print("*" * 50)

save = input("Do you want to save your bio to a text file? (y/n): ").lower()

if save == "y":
    filename = f"{name.lower().replace(' ', '_')}_bio.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(bio)
    print("File saved!")



