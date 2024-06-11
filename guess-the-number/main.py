from random import randint

class GuessTheNumber:
    def __init__(self, min_value, max_value, max_attempts=5):
        self.min_value = min_value
        self.max_value = max_value
        self.max_attempts = max_attempts
    
    def generate_random_number(self):
        return randint(self.min_value, self.max_value)
    
    def get_user_guess(self):
        while True:
            try:
                guess = int(input(f"Guess the number between {self.min_value} and {self.max_value}: "))
                if self.min_value <= guess <= self.max_value:
                    return guess
                else:
                    print(f"Please enter a number between {self.min_value} and {self.max_value}.")
            except ValueError:
                print("Invalid input. Please enter an integer.")
    
    def check_guess(self, random_number, user_guess):
        if random_number < user_guess:
            print("You guessed too high!")
        elif random_number > user_guess:
            print("You guessed too low!")
        else:
            return True
        return False

    def play(self):
        random_number = self.generate_random_number()
        print(f"Welcome to the game! Guess the number between {self.min_value} and {self.max_value}. You have {self.max_attempts} attempts.")
        
        attempts = 0
        while attempts < self.max_attempts:
            user_guess = self.get_user_guess()
            attempts += 1
            if self.check_guess(random_number, user_guess):
                print(f"Congratulations! You guessed the right number {random_number} in {attempts} attempts!")
                return
            else:
                print(f"You have {self.max_attempts - attempts} attempts left.")
        
        print(f"Sorry, you've used all your attempts. The correct number was {random_number}.")

def main():
    game = GuessTheNumber(1, 100, 5)
    while True:
        game.play()
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != 'y':
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
