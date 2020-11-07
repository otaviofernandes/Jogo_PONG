import game
import score

loop = True

while loop:
    result, score1, score2 = game.game()
    loop = score.show_score(result, score1, score2)
