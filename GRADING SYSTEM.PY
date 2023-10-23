def calculate_grade(score):
    if score >= 70 and score <= 100:
        return "A"
    elif score >= 60 and score <= 69:
        return "B"
    elif score >= 50 and score <= 59:
        return "C"
    elif score >= 40 and score <= 49:
        return "D"
    else:
        return "E (Fail)"

def main():
    try:
        score = float(input("Enter the student's score: "))
        if score < 0 or score > 100:
            print("Invalid input. Score should be between 0 and 100.")
        else:
            grade = calculate_grade(score)
            print(f"The student's grade is: {grade}")
            if grade == "E (Fail)":
                print("The student needs to take a supplementary examination.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()
