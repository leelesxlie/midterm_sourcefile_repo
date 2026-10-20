#Student Grade Analyzer

scores= [72, 79, 98, 85, 89]

print("Student Scores: ")
for score in scores:
    print(score)    

print ()

passed_count = 0
failed_count = 0

for index, score in enumerate (scores, start=1):
    if score < 75:
        result = "Failed"
        failed_count += 1
    else:
        if score >= 90:
            grade = "Excellent"
        elif score >= 80:
            grade = "Very Good"
        else: 
            grade = "Good"
        result = f"{grade} - Passed"
        passed_count += 1

    print (f"Student {index}: {score} - {result}") 

print()

total_score = sum(scores)
average_score = total_score / len(scores)
highest_score = max(scores)
lowest_score = min(scores)

print(f"Total Score: {total_score}")
print(f"Average Score: {average_score:.0f}")
print(f"Highest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")

