from math import floor

"""
File: cheese.py
-----------------
Welcome the user and prompt the user what they would like.
Based on their input, inform them that you do have the cheese,
you don't have the cheese, or the cheeses you have.
"""

class cheese:

    def __init__(self):
        self.cheeses = ["Muenster", "Cheddar", "Red Leicester"]
        self.messages = ["Good morning. Welcome to the National Cheese Emporium!", "What would you like? ", "We have {}, yessir.", "I'm afraid we don't have any {}.", "We have {} cheese(s)!"]

    def main(self):
        print(self.messages[0])
        while (True):
            if self.__prompt(input(self.messages[1])):
                break
    
    def __prompt(self, user_input):
        if user_input in self.cheeses:
            print(self.messages[2].format(user_input))
            return True
        elif user_input == "Have you in fact got any cheese here at all?":
            print(self.messages[4].format(len(self.cheeses)))
            for cheese in self.cheeses:
                print(cheese)
            return False
        else:
            print(self.messages[3].format(user_input))
            return False

if __name__ == "__main__":
    queso = cheese()
    queso.main()
