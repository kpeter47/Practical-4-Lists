import random

# Define constants
MIN_NUMBER = 1
MAX_NUMBER = 45

# Function to generate a single quick pick
def generate_quick_pick():
    quick_pick = []
    while len(quick_pick) < 6:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in quick_pick:
            quick_pick.append(number)
    quick_pick.sort()
    return quick_pick

# Ask the user how many quick picks they want
try:
    num_quick_picks = int(input("How many quick picks? "))
except ValueError:
    print("Please enter a valid number.")
    exit(1)

# Generate and display the quick picks
for _ in range(num_quick_picks):
    quick_pick = generate_quick_pick()
    print(" ".join(map(str, quick_pick)))
