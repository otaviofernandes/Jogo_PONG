import game
import menu
import score

loop = menu.show_menu()

while loop:
    result, score1, score2 = game.game()
    loop = score.show_score(result, score1, score2)
