from random import random


class Question:
    def __init__(self, text, options, answer):
        self.__text = text
        self.__options = options
        self.__answer =  answer


    def display_question(self):
        print(self.__text)
        for i, option in enumerate(self.__options):
            print(f"{i + 1}. {option}")

    def check_answer(self, user_answer):
        return user_answer == self.__answer

class Quiz:

    def __init__(self, questions):
        self.__questions = questions
        self.__score = 0

    def start(self):
     import random
     print("!!!!!!!!!!welcome to quiz practice!!!!!!!!!!!!!! ")
    
     random.shuffle(self.__questions)
     for question in self.__questions:
        question.display_question()

        while True:
          try:
            user_answer = int(input("Enter your answer (1-4): "))
            if user_answer < 1 or user_answer > 4:
                    print("Please enter a number between 1 and 4.")
                    continue
            if question.check_answer(user_answer):
                    print("Correct!")
                    self.__score += 1
                    break # sort de la boucle while pour passer a la question suivante
            else:
                print("Incorrect!")
                break

          except  ValueError: #si l user tape une valeur non numerique
            print("Please enter a valid number.")
          except Exception as e: #s il ya n importe quelles autres erreurs
            print(f"l'erreur est {e}  la reponse doit etre un nombre entre 1 et 4")
            break
    # Call final score display without extra metadata
     self.display_final_score()



    def display_final_score(self):
        print("Quiz completed!")
        print(f"Your final score is: {self.__score}/{len(self.__questions)}")

        while True:
             play_again=input("Do you want to play again? (yes/no): ")
             if play_again.lower() in ["yes",  "y", "oui", "o"]:
                     self.__score = 0
                     self.start()

             elif play_again.lower() in ["non", "n", "no"]:
                  print("thank you for playing! Goodbye!")
                  exit() 

             else:
                 print("la reponse doit etre (yes, no, non, oui, y, o)")
                 
                          
       
              

question1=Question("What is the capital of Guinea?", ["Conakry", "Accra", "Lagos", "Abidjan"], 1)
question2=Question("What is the largest city in Guinea?", ["Conakry", "Kindia", "N'Zerekore", "Dalaba"], 1) 
question3=Question("What is the official language of Guinea?", ["French", "English", "Spanish", "Portuguese"], 1)

Quiz([question1, question2, question3]).start()