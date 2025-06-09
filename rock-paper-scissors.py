#Rock-Paper-Scissors
import random
print("Let's play Rock-Papers-Scissors-Lizard-Spock. Inspired from Big Bang Theory!")
print("You pick a number from 1 to 5.")
print("1 is Rock ✊, 2 is Paper ✋, 3 is Scissors ✌️, 4 is Lizard 🦎 and 5 is Spock 🖖") 
choice = {1: "Rock ✊", 2: "Paper ✋", 3: "Scissors ✌️", 4: "Lizard 🦎", 5: "Spock 🖖"}
print("Before we start let's explain the rules of the game.")

print("Scissors cut Paper.\n" +
      "Paper covers Rock.\n" +
      "Rock crushes Lizard.\n" +
      "Lizard poisons Spock.\n" +
      "Spock smashes Scissors.\n" +
      "Scissors beat Lizard.\n" +
      "Lizard eats Paper.\n" +
      "Paper disproves Spock.\n" +
      "Spock vaporizes Rock.\n" +
      "Rock breaks Scissors.\n")

player_score = 0
cpu_score = 0

def rock_paper_scissor():
    global player_score, cpu_score
    while True:
        try:
            player = int(input("Pick a number (1-5): "))
            if player not in choice:
                print("Invalid choice. Try again")
                continue
        except ValueError:
            print("Please enter a number.")
            continue

        cpu = random.randint(1, 5)

        print(f"You chose {choice[player]}")
        print(f"CPU chose {choice[cpu]}")

        if player == cpu:
            print("Tie!")
        elif (player == 1 and cpu == 3) or (player == 2 and cpu == 1) or (player == 3 and cpu == 2) or (player == 1 and cpu == 4) or (player == 4 and cpu == 5) or (player == 5 and cpu == 3) or (player == 3 and cpu == 4) or (player == 4 and cpu == 2) or (player == 2 and cpu == 5) or (player == 5 and cpu == 1):
            print("You Win!")
            player_score += 1
        else:
            print("You Lose!")
            cpu_score += 1
        break

while True:
    rock_paper_scissor()
    print(f"The score is Player: {player_score} - CPU: {cpu_score}")
    rematch = input("Wanna play again? Type (Y/N)").lower()
    if rematch not in ("y", "yes"):
        print("Thank you for playing!")
        break