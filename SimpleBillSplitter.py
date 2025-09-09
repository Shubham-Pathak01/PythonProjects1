num_people = int(input("How many people are there in group? "))
names = []

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

for i in range(num_people):
    name = input("What is name of person one? ").strip()
    names.append(name)

total_bill = get_float("Enter bill Amount in Number only: ")

share = round(total_bill / num_people, 2)

print("\n" + "*" * 40)
print(f"Total bill: {total_bill}")
print(f"Each person owes {share}")

for name in names:
    print(f" {name} owes {share} rupees")

print("\n" + "*" * 40)
