# =========================================================
# STUDENT GRADE ANALYZER - VERSION 3
# =========================================================

# Store the raw comma-separated records.
raw_records = [
    "Ana,88,92,90",
    "Ben,70,72,74",
    "Cara,95,91,94",
    "Dan,78,80,76",
    "Ella,85,89,87",
    # --- Part F test records (invalid/incomplete records) ---
    "Fred,90,85",         # missing one score -> only 3 fields
    "Gina",               # only a name, no scores -> only 1 field
    "Henry,90,eighty,85", # non-numeric score -> triggers ValueError
    "Ivy,",               # empty score field(s) -> triggers ValueError
    "Milo,abc,50,60"      # "abc" isn't a number, should trigger the ValueError skip
]

# Store the passing average.
PASSING_GRADE = 75

# Create the dictionary that will map names to score lists.
student_scores = {}

# =========================================================
# PART A: Parse and organize the records.
# =========================================================
for record in raw_records:
    # Split the record into fields using split(").
    fields = record.split(",")

    # Guardian condition: a valid record must have exactly 4 fields
    # (name + 3 scores). Skip anything that doesn't match.
    if len(fields) != 4:
        print(f"Skipped invalid record: {record}")
        continue

    # Store the student's name (first field).
    name = fields[0]

    # Convert the score fields (everything after the name) to numbers safely.
    try:
        # List slicing: fields[1:] grabs every field except the name.
        scores = [int(score) for score in fields[1:]]
    except ValueError:
        print(f"Skipped invalid record: {record}")
        continue

    # Add the name and scores to student_scores.
    student_scores[name] = scores


# =========================================================
# PART B: Display records alphabetically.
# =========================================================
print("\nORGANIZED STUDENT RECORDS")

# Sort the names alphabetically before displaying (don't rely on dict order).
for name in sorted(student_scores.keys()):
    scores = student_scores[name]
    print(f"{name}: {scores}")


# Create a list for result tuples.
ranking = []

# Create counters for the class summary.
passed_count = 0
failed_count = 0
sum_of_averages = 0

# =========================================================
# PART C: Calculate the student results.
# =========================================================
for name, scores in student_scores.items():
    # Guard against an empty score list (avoids division by zero).
    if len(scores) == 0:
        print(f"Skipped {name}: no scores to calculate.")
        continue

    # Calculate total, average, highest, and lowest using built-ins.
    total = sum(scores)
    average = total / len(scores)
    highest_score = max(scores)
    lowest_score = min(scores)

    # Determine the student's remark.
    if average >= PASSING_GRADE:
        remark = "Passed"
    else:
        remark = "Failed"

    # Update the passed or failed counter.
    if remark == "Passed":
        passed_count += 1
    else:
        failed_count += 1

    # Add the average to sum_of_averages for the class average later.
    sum_of_averages += average

    # Create and append the result tuple.
    result_tuple = (average, name, highest_score, lowest_score, remark)
    ranking.append(result_tuple)


# =========================================================
# PART D: Sort and display the ranking.
# =========================================================
# Sort ranking from highest to lowest average (tuple's first item).
ranking.sort(key=lambda record: record[0], reverse=True)

print("\nSTUDENT GRADE REPORT")
print("Rank  Name       Average  Highest  Lowest  Remark")

# Use enumerate() and tuple unpacking to display the ranking.
for rank, (average, name, highest_score, lowest_score, remark) in enumerate(ranking, start=1):
    print(f"{rank:<5} {name:<10} {average:<8.2f} {highest_score:<8} {lowest_score:<7} {remark}")


# =========================================================
# PART E: Display the class summary.
# =========================================================
total_students = len(ranking)

# Calculate the class average safely (avoid division by zero).
if total_students > 0:
    class_average = sum_of_averages / total_students
else:
    class_average = 0

print("\nCLASS SUMMARY")
print(f"Number of Students: {total_students}")
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")
print(f"Class Average: {class_average:.2f}")

# Use ranking[0] and ranking[-1] safely (ranking is already sorted).
if total_students > 0:
    top_average, top_name, _, _, _ = ranking[0]
    bottom_average, bottom_name, _, _, _ = ranking[-1]
    print(f"Highest: {top_name} - {top_average:.2f}")
    print(f"Lowest: {bottom_name} - {bottom_average:.2f}")
else:
    print("Highest: N/A")
    print("Lowest: N/A")