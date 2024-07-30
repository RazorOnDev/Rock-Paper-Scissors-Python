# Importamos random
import random

# Lista de movimientos posibles (Piedra, Tijeras, Papel)
possible_movements = ["Rock", "Scissors", "Paper"]

# Función para obtener un movimiento válido del jugador
def get_player_movement():
    while True:
        print('Choose your movement:')
        print('1: Rock')
        print('2: Scissors')
        print('3: Paper')
        player_input = input()
        
        if player_input in ['1', '2', '3']:
            return possible_movements[int(player_input)-1]
        else:
            print("Invalid input. Please enter 1, 2, or 3.")

# Obtener el movimiento del jugador
player_1_movement = get_player_movement()

# Elegimos un movimiento random para el rival (player 2)
player_2_movement = random.choice(possible_movements)

# Condicionales de victoria, empate o derrota dependiendo de los enfrentamientos posibles
if player_1_movement == 'Rock':
    if player_2_movement == 'Scissors':
        print(f'{player_1_movement} VS {player_2_movement}, You Win.')
    elif player_2_movement == 'Rock':
        print(f'{player_1_movement} VS {player_2_movement}, Draft.')
    else:
        print(f'{player_1_movement} VS {player_2_movement}, You Lose.')
elif player_1_movement == 'Scissors':
    if player_2_movement == 'Paper':
        print(f'{player_1_movement} VS {player_2_movement}, You Win.')
    elif player_2_movement == 'Scissors':
        print(f'{player_1_movement} VS {player_2_movement}, Draft.')
    else:
        print(f'{player_1_movement} VS {player_2_movement}, You Lose.')
elif player_1_movement == 'Paper':
    if player_2_movement == 'Rock':
        print(f'{player_1_movement} VS {player_2_movement}, You Win.')
    elif player_2_movement == 'Paper':
        print(f'{player_1_movement} VS {player_2_movement}, Draft.')
    else:
        print(f'{player_1_movement} VS {player_2_movement}, You Lose.')
