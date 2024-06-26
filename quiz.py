import random
#Question to be asked
quiz_data = [
    {
        "question": "What does HTML stand for?",
        "options": ["A. Hyperlink Text Markup Language", "B. Hyper Transfer Markup Language", "C. Hypertext Markup Language", "D. High-Level Text Markup Language"],
        "answer": "C"
    },
    {
        "question": "Which programming language is often used for web development?",
        "options": ["A. Python", "B. Java", "C. Ruby", "D. JavaScript"],
        "answer": "D"
    },
    {
        "question": "Nobel prize is awarded for which of the following disciplines?",
	    "options": ["A. Literature, peace and economics", "B. Medicine or Physiology", "C. Chemistry and Physics","D. All the above"],
        "answer": "D"
    },
    {
        "question": "Which state has Introduced new kin technology?",
	    "options": ["A. Assam", "B. Delhi", "C. Haryana", "D. Punjab"],
        "answer": "D"
    },
    {
        "question": "At the end of March 2019, what was the amount of India's external debt?",
	    "options": ["A. US $ 540 billion", "B. US $ 543 billion", "C. US $ 547 billion", "D. US $ 541 billion"],
         "answer": "B"
    },
    {
        "question": "Which Indian revolutionary leader is known as 'Bagha Jatin'?",
	    "options": ["A. Jatindranath Mukherjee", "B. Jatindranath Bannerjee", "C. Jatindranath Das", "D. Jatindranath bose"],
        "answer": "A"
    },
    {
        "question": "In Python, which keyword is used to define a function?",
        "options": ["A. define", "B. func", "C. def", "D. function"],
        "answer": "C"
    },
    {
        "question": "Entomology studies what?",
	    "options": ["A. Behavior of human beings","B. Insects","C. The origin and history of technical and scientific terms","D. The formation of rocks"],
        "answer": "B"
    },
    {
        "question": "Who is the father of geometry?",
	    "options": ["A. Aristotle","B. Euclid","C. Pythagoras","D. Kepler"],
        "answer": "B"
    },
    {
        "question": "Which data type in Python is used to represent a sequence of characters?",
        "options": ["A. int", "B. float", "C. str", "D. list"],
        "answer": "C"
    },
    {
        "question": "Which is the first search engine of the internet?",
	    "options": ["A. Yahoo","B. Wais","C. Archie","D. Mozilla"],
        "answer": "C"
    },
    {
        "question": "Who wrote the famous poem 'The Charge of the Light Brigade'?",
	    "options": ["A. Lord Alfred Tennyson","B. Christopher Marlowe","C. Johannes Gutenberg","D. Rene Descartes"],
        "answer": "A"
    },
    {
        "question": "What is the HTTP status code for a successful response?",
        "options": ["A. 200 OK", "B. 404 Not Found", "C. 500 Internal Server Error", "D. 302 Found"],
        "answer": "A"
    },
    {
        "question":  "The Indian, who holds the pride of beating the computers in mathematical wizard is?",
	    "options": ["A. Shakuntala Devi","B. Raja Ramanna","C. Ramanujam","D. Rina Panigrahi"],
        "answer": "A"
    },
    {
        "question": "Guru Gopi Krishna is popular for which form of Indian dance?",
	    "options": ["A. Bharatanatyam","B. Kuchipudi","C. Kathak","D. Manipuri"],
        "answer": "B"
    },
    {
        "question": "Which of the following is not a valid Python data type?",
        "options": ["A. int", "B. double", "C. list", "D. tuple"],
        "answer": "B"
    },
    {
        "question":  "Who is the current chief of the world bank group?",
	    "options": ["A. Donald Tusk","B. David Malpass","C. Christine Lagarde","D. Jim Yong Kim"],
        "answer": "B"
    },
    {
        "question": "Which programming language is often used for developing mobile applications?",
        "options": ["A. Java", "B. Python", "C. C#", "D. PHP"],
        "answer": "A"
    },
    {
        "question": "Headquater of International Olympic Committee is situated at?",
	    "options": ["A. Athens", "B. Lausanne", "C. Dubai", "D. None of the above"],
        "answer": "B"
    }
]
#displaying content
def ask_question(question_data):
    print(question_data["question"])
    for option in question_data["options"]:
        print(option)
    user_answer = input("Enter your answer (A,B,C,D): ").upper()
    if user_answer == question_data["answer"]:
        return True
    else:
        return False
#main body
if __name__=="__main__":
    score=0
    random.shuffle(quiz_data)
    for i in range(1,6):
        print(f'Question {i} of 5')
        if ask_question(quiz_data[i]):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {quiz_data[i]['answer']}.\n")

    print(f"Your score {score}/5.")