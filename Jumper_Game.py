import random

class jumper:
    def __init__(self, line):
        self.line = line
        
    def display_jumper(self):
        print(self.line)

# class guess_letter:
#     def __init__(self, word, guess):
#         self.word = word
#         self.guess = guess
#     def verify_guess(self):
#         number = 0
#         for element in range(self.word):
#             number += 1
#             if element == self.guess:


    
# class guess_lines:
#     def __init__(self, ):

def main():
    print("_ _ _ _ _")
    print()

    first_dash = "_ "
    second_dash = "_ "
    third_dash = "_ "
    fourth_dash = "_ "
    fifth_dash = "_ "

    first_line = jumper(" ___")
    second_line = jumper("/___\\")
    third_line = jumper("\   /")
    fourth_line = jumper(" \ /")
    fifth_line = jumper("  O")
    sixth_line = jumper(" /|\\")
    last_line = jumper(" / \\")


    first_line.display_jumper()
    second_line.display_jumper()
    third_line.display_jumper()
    fourth_line.display_jumper()
    fifth_line.display_jumper()
    sixth_line.display_jumper()
    last_line.display_jumper()
    print()
    print("^^^^^^^")
    print()
    random_word = word_generator()
    wrong_guess = 0
    lost = 1
    while wrong_guess < 4 or lost == 0:
        
        letter_guessed = input("Guess a letter [a-z]: ")
        print()
        
        number = 0

        for x in random_word:
            number += 1
            if x == letter_guessed and number == 1:
                first_dash = letter_guessed
            if x == letter_guessed and number == 2:
                second_dash = letter_guessed
            if x == letter_guessed and number == 3:
                third_dash = letter_guessed
            if x == letter_guessed and number == 4:
                fourth_dash = letter_guessed
            if x == letter_guessed and number == 5:
                fifth_dash = letter_guessed
        if letter_guessed not in random_word:
                wrong_guess += 1

        bool_one = first_dash.isalpha()
        bool_two = second_dash.isalpha()
        bool_three = third_dash.isalpha()
        bool_four = fourth_dash.isalpha()
        bool_five = fifth_dash.isalpha()

        if bool_one == 1 and bool_two == 1 and bool_three == 1 and bool_four == 1 and bool_five == 1:
            lost = 0
        
        print(first_dash, " ", second_dash, " ", third_dash, " ", fourth_dash, " ", fifth_dash)
        print()

        if wrong_guess == 1:
            second_line.display_jumper()
            third_line.display_jumper()
            fourth_line.display_jumper()
            fifth_line.display_jumper()
            sixth_line.display_jumper()
            last_line.display_jumper()
        if wrong_guess == 2:
            third_line.display_jumper()
            fourth_line.display_jumper()
            fifth_line.display_jumper()
            sixth_line.display_jumper()
            last_line.display_jumper()
        if wrong_guess == 3:
            fourth_line.display_jumper()
            fifth_line.display_jumper()
            sixth_line.display_jumper()
            last_line.display_jumper()
        if wrong_guess == 4:
            fifth_line = jumper("  X")
            fifth_line.display_jumper()
            sixth_line.display_jumper()
            last_line.display_jumper()
        print()
        print("^^^^^^^")
        print()

            

    


    

def word_generator():
    words = ["Stive", "Drone", "Sharp", "Touch", "Chair", "Young", "Perch", "Infix", "Guess", "Ideal", "Props", "Elong", "Stank"]
    word = random.choice(words)
    return word.lower()

if __name__ == "__main__":
    main()