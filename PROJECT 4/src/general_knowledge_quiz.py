def main():
    score = 0

    print("=" * 40)
    print("       GENERAL KNOWLEDGE QUIZ")
    print("=" * 40)

    # Question 1
    print("\nQuestion 1: What is the capital of France?")
    answer = input("Your answer: ").strip().lower()

    if answer == "paris":
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The correct answer is Paris.")

    # Question 2
    print("\nQuestion 2: Which planet is known as the Red Planet?")
    answer = input("Your answer: ").strip().lower()

    if answer == "mars":
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The correct answer is Mars.")

    # Question 3
    print("\nQuestion 3: How many days are there in a week?")
    answer = input("Your answer: ").strip().lower()

    if answer == "7" or answer == "seven":
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The correct answer is 7.")

    # Final score
    print("\n" + "=" * 40)
    print(f"Your final score is: {score}/3")
    print("=" * 40)


if __name__ == "__main__":
    main()
    
