from math import floor

"""
File: coconuts.py
-----------------
Prompts the user for the ounces of birds that are carrying the coconuts,
prompts the user for the pounds of coconuts that there are, and  prints a 
message indicating whether the ounces of birds can carry the pounds of coconuts.
"""

class coconuts:

    def __init__(self):
        self.messages = ["Enter a rational number as a decimal or an integer, please!",
            "How many ounces of brids are carrying the coconuts? ",
            "How many pounds of coconuts are there? "]

    def getValue(self, index):
        while(True):
            try:
                value = float(input(self.messages[index]))
                return value
            except ValueError:
                print(error_message)

    def is_carrying_possible(self, ounces_of_birds, pounds_of_coconuts):
        if (ounces_of_birds / 5.5) >= pounds_of_coconuts:
            return "Yes! Carrying the coconuts is possible."
        else:
            return "No. Carrying the coconuts is impossible."

    def main(self):
        ounces_of_birds = self.getValue(1)
        pounds_of_coconuts = self.getValue(2)
        print(self.is_carrying_possible(ounces_of_birds, pounds_of_coconuts))

if __name__ == "__main__":
    coco = coconuts()
    coco.main()   
