name = input("what is your name: ")
score = int(input("what is your score: "))

if score >=70 and score <= 100:
    print(f"Hello {name}, your grade is A")
if score >=60 and score <= 69:
    print(f"Hello {name}, your grade is B")
if score >= 50 and score <= 59:
    print(f"Hello {name}, your grade is C")
if score >= 40 and score <= 49:
    print(f"Hello {name}, your grade is D")
if score >= 0 and score <= 39:
    print(F"hello {name}, your grade is F")
else:
    print("invalid score")