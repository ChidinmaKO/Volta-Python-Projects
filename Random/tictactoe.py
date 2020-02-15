import itertools
from colorama import Fore, Back, Style, init
init()

def wins(current_game):

	def all_same(l):
		if l.count(l[0]) == len(l) and l[0] != 0:
			return True
		else:
			return False

	# horizontal wins
	for row in current_game:
		print(row)
		if all_same(row):
			print(f"Player {row[0]} is the winner horizontally (-)")
			return True

	# vertical wins
	for col in range(len(current_game)):
		col_index = []
		for row in current_game:
			col_index.append(row[col])
		if all_same(col_index):
			print(f"Player {col_index[0]} is the winner vertically (|)")
			return True

	# diagonal wins
	diags = []
	for row, col in enumerate(reversed(range(len(current_game)))):
		diags.append(current_game[row][col])
	if all_same(diags):
		print(f"Player {diags[0]} is the winner diagonally (/)")
		return True

	diags = []
	for i in range(len(current_game)):
		diags.append(current_game[i][i])
	if all_same(diags):
		print(f"Player {diags[0]} is the winner diagonally (\\)")
		return True
	return False


def game_board(game_map, player=0, row=0, col_index=0, display=False):

	index = "   " + "  ".join([str(i) for i in range(len(game_map))])

	# error handling with try/except
	try:
		if game_map[row][col_index] != 0:
			print("Choose another position. This is taken")
			return game_map, False
		print(index)

		if not display:
			game_map[row][col_index] = player
		
		# using colorama
		for count, row in enumerate(game_map):
			colored_row = ""
			# print (count , row)
			for item in row:
				if item == 0:
					colored_row += "   "
				elif item == 1:
					colored_row += Fore.MAGENTA + ' X ' + Style.RESET_ALL
				elif item == 2:
					colored_row += Fore.RED + ' O ' + Style.RESET_ALL
			print(count, colored_row)
		return game_map, True

	except IndexError as e:
		print(e, ": Make sure you input the row/col_index as 0,1 or 2.")
		return game_map, False
	except Exception as err:
		print(err, ": Something went wrong Sis.")
		return game_map, False

play = True
players = [1, 2]
while play:

	# dynamic game size
	game_size = int(input("Pick the game size: "))
	game = [[0 for i in range(game_size)] for i in range(game_size)]

	game_won = False
	game_board(game, display=True)
	player_choice = itertools.cycle([1, 2])

	while not game_won:
		current_player = next(player_choice)
		# print(f"Current_player : { current_player }")
		played = False

		while not played:
			print(f"Current_player : { current_player }")

			choice_range = [int(i) for i in range(game_size)]
			row_choice = int(input(f"What row do you want to play? { choice_range }: "))
			column_choice = int(input(f"What column do you want to play? { choice_range }: "))

			played = game_board(game, current_player, row_choice, column_choice)

		# check if the game is won & ask if the user wants to play again
		if wins(game):
			game_won = True
			play_again = input("Game Over! Do you want to play again?: (y/n) ")
			if play_again.lower() == "y":
				print("Restarting! Welcome back.")
				play = True
			elif play_again.lower() == "n":
				print("So long. Farewell.")
				play = False
			else:
				print("Hey! That wasn't a valid response. Doei! 👋🏿")
				play = False

'''
TODO:
1. stop replicating the game_board
2. Randomize the first player
3. Python Tests & PEP 8
4. Check for when the player doesn't input an integer for row or column choice
'''
