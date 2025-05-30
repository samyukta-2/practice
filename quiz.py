def run_quiz(questions):
    score = 0
    for idx, q in enumerate(questions, start=1):
        print(f"\nQuestion {idx}: {q['question']}")
        for option in q['options']:
            print(option)
        answer = input("Your answer (A/B/C/D): ").strip().upper()

        if answer == q['answer']:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect! The correct answer was {q['answer']}.")

    print(f"\n🎉 Quiz completed! Your final score is {score} out of {len(questions)}.")

quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. London", "C. Paris", "D. Madrid"],
        "answer": "C"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["A. Python", "B. JavaScript", "C. Java", "D. All of the above"],
        "answer": "D"
    },
    {
        "question": "Who developed the theory of relativity?",
        "options": ["A. Newton", "B. Einstein", "C. Tesla", "D. Curie"],
        "answer": "B"
    }
]

run_quiz(quiz_questions)
nice questions but very tuff
