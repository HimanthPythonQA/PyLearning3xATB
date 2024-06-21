score = int(input("enter the score\n"))
if score >= 90 and score <= 100:
    print("grade is A")
if score >= 80 and score <= 89:
    print("grade is B")
if score >= 70 and score <= 79:
    print("grade is C")
if score >= 60 and score <= 69:
    print("grade is D")
if score >= 0 and score <= 59:
    print("fail F")
else:
    print("invalid score")
