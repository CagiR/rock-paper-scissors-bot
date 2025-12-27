import random

def play(player1, player2, num_games, verbose=False):
    p1_score = 0
    p2_score = 0
    tie = 0

    p1_prev_play = ""
    p2_prev_play = ""

    for _ in range(num_games):
        p1_play = player1(p2_prev_play)
        p2_play = player2(p1_prev_play)

        if p1_play == p2_play:
            tie += 1
            if verbose:
                print("Tie.")
        elif (p1_play == "R" and p2_play == "S") or \
             (p1_play == "S" and p2_play == "P") or \
             (p1_play == "P" and p2_play == "R"):
            p1_score += 1
            if verbose:
                print("Player 1 wins.")
        else:
            p2_score += 1
            if verbose:
                print("Player 2 wins.")

        p1_prev_play = p1_play
        p2_prev_play = p2_play

    games = p1_score + p2_score + tie

    if verbose:
        print(f"Final results: Player 1: {p1_score}, Player 2: {p2_score}, Ties: {tie}")

    return p1_score / games * 100


def quincy(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
    return random.choice(["R", "P", "S"])


def abbey(prev_play, opponent_history=[]):
    if not prev_play:
        return random.choice(["R", "P", "S"])
    opponent_history.append(prev_play)
    most_common = max(set(opponent_history), key=opponent_history.count)
    return {"R": "P", "P": "S", "S": "R"}[most_common]


def kris(prev_play):
    return random.choice(["R", "P", "S"])


def mrugesh(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
    if len(opponent_history) < 10:
        return random.choice(["R", "P", "S"])
    most_common = max(set(opponent_history[-10:]), key=opponent_history[-10:].count)
    return {"R": "P", "P": "S", "S": "R"}[most_common]
