# Santiago | Lab 4 | Intro to Python
# Ticket 1 
# PREDICT: I predict that it woudl allowed acces to 17, 25 and 3. 
# It would not allowed to 11,9.
ages = [17, 11, 25, 13, 9]
for age in ages: 
    if age >= 13:
        print(f"{age}-Access granted✅")
    else:
        print(f"{age}-Access denied❌")
    # EXPLAIN: The Var ages holds the age that was listed on line 5.
    # Ticket 2
    # I predict that if the user says no, then no loop will happen. 
    keep_checking = "yes"
while keep_checking == "yes":
    age = int(input("Enter an age: "))
    if age >= 13:
        print("Access granted✅")
    else:
        print("Too young")
    keep_checking = input("Check another age? (yes/no): ")
    # EXPLAIN: The while loop is better than the for loop for this due to the user being able to change their age.
    # Ticket 3
    # PREDICT: If the the break was never added, then the loop would keep going.
while True:
    age = input("Enter an age or type 'stop': ")
    if age == "stop":
        break
    age = int(age)
    if age >= 13:
        print("Access granted✅")
    else:
        print("Too young❌")
# EXPLAIN: The difference between the ticket 2 loop and this one is the break which makes the loop stop at any moment the user wants.
# Ticket 4 
# PREDICT: The output is the same just that it would be checked by a function.
def can_access(age):
    if age >= 13:
        return True
    else:
        return False

ages = [17, 11, 25, 13, 9]

for age in ages:
    if can_access(age):
        print(f"{age} — Access granted ✅")
    else:
        print(f"{age} — Too young ❌")
# EXPLAIN: Using a function can be recalled at any time making the code more efficient and easier to read.
# Ticket 5
# PREDICT:
# --- StreamPass Signup Report ---
# Signup #1 | Age 17 — Access granted ✅
# Signup #2 | Age 11 — Too young ❌
# Signup #4 | Age 25 — Access granted ✅
# Signup #5 | Age 13 — Access granted ✅
# Signup #6 | Age 9 — Too young ❌
# Approved: 3 out of 5

def signup_report(age_list):
    approved = 0
    print("--- StreamPass Signup Report ---")
    for number, age in enumerate(age_list, start=1):
        if can_access(age):
            print(f"Signup #{number} | Age {age} — Access granted ✅")
            approved += 1
        else:
            print(f"Signup #{number} | Age {age} — Too young ❌")
    print(f"Approved: {approved} out of {len(age_list)}")
signups = [22, 10, 15, 8, 19, 13]
signup_report(signups)
# EXPLAIN: I used functions, loops, conditionals and lists on this code.