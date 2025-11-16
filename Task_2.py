# --------------------------------------------
# Student Grade Calculator
# --------------------------------------------

# Function to calculate grade based on marks
def calculate_grade(marks):
    if marks >= 90:
        return "A", "Excellent! You did a fantastic job! 🌟"
    elif marks >= 80:
        return "B", "Great work! Keep it up! 👍"
    elif marks >= 70:
        return "C", "Good effort! You can do even better! 🙂"
    elif marks >= 60:
        return "D", "Not bad! Try to focus a bit more next time. 💪"
    else:
        return "F", "Don't worry! Keep practicing and you'll improve. 🙌"

# Main program
print("---- Student Grade Calculator ----")

try:
    marks = float(input("Enter your marks (0–100): "))

    if marks < 0 or marks > 100:
        print("⚠️ Please enter marks between 0 and 100.")
    else:
        grade, message = calculate_grade(marks)
        print(f"\nYour Grade: {grade}")
        print(f"Message: {message}")

except ValueError:
    print("❌ Invalid input! Please enter a numeric value.")

print("\nThank you for using the Grade Calculator!")
