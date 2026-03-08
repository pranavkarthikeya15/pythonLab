import os

file_name = "mala_tracker.txt"

# Step 1: Read previous total if exists
if os.path.exists(file_name):
    with open(file_name, 'r') as f:
        total = int(f.read())
else:
    total = 0

print(f"Total malas recited so far: {total}\n")

# Step 2: Loop to add today’s malas
while True:
    malas = input("Enter the number of malas today (or 'q' to quit): ")
    
    if malas.lower() == 'q':
        break
    
    try:
        total += int(malas)
    except ValueError:
        print("Please enter a valid number or 'q' to quit.\n")
        continue
    
    # Show progress after each entry
    print(f"Total malas recited so far: {total}")
    print(f"Malas remaining to reach 1,00,000: {100000 - total}")
    print(f"Percentage of malas completed: {total / 100000 * 100:.2f}%\n")

# Step 3: Save total back to file
with open(file_name, 'w') as f:
    f.write(str(total))

print("Sree Gurubhyo Namaha! Keep up the good work! 🙏")
