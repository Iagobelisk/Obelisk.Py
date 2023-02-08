import random

def get_choices():
    player_choice = input("Faça uma escolha entre (pedra, papel ou tesoura): ")
    options = ["pedra", "papel", "tesoura"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"Você escolheu {player}, o computador escolheu {computer}")
    if player == computer:
        return "é um empate!"

    elif player == "pedra":
        if computer == "tesoura":
            return "Pedra esmaga tesoura! Você venceu! "
        else:
            return "Papel cobre pedra! Você perdeu. "

    elif player == "tesoura":
        if computer == "papel":
            return "Tesoura corta papel! Você ganhou! "
        else:
            return "Pedra esmaga tesoura! Você perdeu. "

    elif player == "papel":
        if computer == "pedra":
            return "Papel cobre pedra! Você ganhou! "
        else:
            return "Tesoura corta papel! Você perdeu."

choices = get_choices()
result = check_win(choices["player"], choices["computer"])

print(result)
