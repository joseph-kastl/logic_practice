#Joseph Kastl#
#10/15/2026#

#====================#
#Selection Structure#
#====================#

#Exercise: Voting eligibility#
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

#My example: Car rental eligibility (25 or older)#
renter_age = int(input("Enter your age to rent a car: "))
if renter_age >= 25:
    print("You can rent a car.")
else:
    print("Sorry, you must be at least 25 to rent a car.")

#=================================#
#Relational Comparison Operators#
#=================================#

#Exercise: Compare two numbers with all six operators#
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print(f"{num1} == {num2}: {num1 == num2}")
print(f"{num1} != {num2}: {num1 != num2}")
print(f"{num1} < {num2}: {num1 < num2}")
print(f"{num1} > {num2}: {num1 > num2}")
print(f"{num1} <= {num2}: {num1 <= num2}")
print(f"{num1} >= {num2}: {num1 >= num2}")

#My example: Compare tickets closed this week vs. last week#
this_week = int(input("How many tickets did you close this week? "))
last_week = int(input("How many tickets did you close last week? "))
print(f"Same as last week: {this_week == last_week}")
print(f"Different from last week: {this_week != last_week}")
print(f"Fewer than last week: {this_week < last_week}")
print(f"More than last week: {this_week > last_week}")
print(f"No more than last week: {this_week <= last_week}")
print(f"At least as many as last week: {this_week >= last_week}")

#==========#
#AND Logic#
#==========#

#Exercise: Pass the course#
score = float(input("Enter your test score: "))
attendance = float(input("Enter your attendance percentage: "))
if score >= 70 and attendance >= 80:
    print("You pass the course.")
else:
    print("You do not pass the course.")

#My example: Roller coaster#
height = int(input("Enter your height in inches: "))
rider_age = int(input("Enter your age: "))
if height >= 48 and rider_age >= 10:
    print("You can ride the roller coaster!")
else:
    print("Sorry, you can't ride this one.")

#========#
#OR Logic#
#========#

#Exercise: Library entry (student ID OR library card)#
has_student_id = input("Do you have a student ID? (yes/no): ").lower()
has_library_card = input("Do you have a library card? (yes/no): ").lower()
if has_student_id == "yes" or has_library_card == "yes":
    print("You may enter the library.")
else:
    print("Access denied. You need a student ID or library card.")

#My example: Free shipping (order $50 or more OR store member)#
order_total = float(input("Enter your order total: $"))
is_member = input("Are you a store member? (yes/no): ").lower()
if order_total >= 50 or is_member == "yes":
    print("You get free shipping!")
else:
    print("Shipping will be added to your order.")


#=========#
#NOT Logic#
#=========#

#Exercise: System access (NOT banned)#
is_banned = input("Are you banned from the system? (yes/no): ").lower()
if not is_banned == "yes":
    print("You may access the system.")
else:
    print("Access denied due to ban.")

#My example: Going outside (NOT raining)#

is_raining = input("Is it raining outside? (yes/no): ").lower()
if not is_raining == "yes":
    print("Go ahead and head outside!")
else:
    print("Better stay in or grab an umbrella.")


#================================#
#Combining AND/OR with Precedence#
#================================#

#Exercise: Scholarship#
gpa = float(input("Enter your GPA: "))
volunteer_hours = int(input("Enter your volunteer hours: "))
leadership = input("Do you hold a leadership role? (yes/no): ").lower()
if gpa >= 3.5 and (volunteer_hours >= 50 or leadership == "yes"):
    print("You qualify for the scholarship.")
else:
    print("You do not qualify for the scholarship.")

#My example: Varsity team#
team_gpa = float(input("Enter your GPA: "))
tryout_score = int(input("Enter your tryout score: "))
coach_rec = input("Do you have a coach's recommendation? (yes/no): ").lower()
if team_gpa >= 2.0 and (tryout_score >= 80 or coach_rec == "yes"):
    print("You made the varsity team!")
else:
    print("You did not make the varsity team this time.")