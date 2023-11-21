def main():
    print("* * The Wizard Game * *")
    num_questions = input("How many Questions do you want to ask the Wizard? ")
   
    if num_questions.isdigit():
        processQuestions(int(num_questions))
    else:
        print("That's not a number. The Wizard wants you to go away now!")
        print("END OF PROGRAM")
                
def processQuestions(num_questions):
    for i in range(num_questions):
        question = input("What's your question? ").strip().lower()
       
        if question == "bye":
            print("END OF PROGRAM")
            break
       
        answer = getAnswer(question)
        print(str(i + 1) + ". The Wizard Answers: " + answer)
        
    else:  
        print("You may not ask any more questions!")
        print("END OF PROGRAM")
              
def getAnswer(question):
    if question.startswith("who"):
        return "Who, Who... isn't that a sound an owl makes?"
    elif question.startswith("what"):
        return "What is the meaning of life?"
    elif question.startswith("how"):
        return "How do you do?"
    else:
        return "I don't know"

if __name__ == "__main__":
    main()      