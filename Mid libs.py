def get_input(word_type):
    user_input = input(f"Enter a {word_type}:")
    return user_input

noun1 = get_input("Noun")
verb1 = get_input("Verb")
noun2 = get_input("Noun")
verb2 = get_input("Verb")

para = f"""
Once upon a time, there was a {noun1} who loved to {verb1}.
One day, the {noun1} met a {noun2}, and together they decided to {verb2}.
It was the beginning of a very unusual adventure!
"""

print("Here is your mad lib story: ")
print(para)