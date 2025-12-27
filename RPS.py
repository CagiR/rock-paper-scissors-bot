import random

def player(prev_play, opponent_history=[]):
    if prev_play != "":
        opponent_history.append(prev_play)

    # First move: random
    if len(opponent_history) < 2:
        return random.choice(["R", "P", "S"])

    # Frequency analysis
    counts = {
        "R": opponent_history.count("R"),
        "P": opponent_history.count("P"),
        "S": opponent_history.count("S")
    }

    most_common = max(counts, key=counts.get)

    # Counter the most common move
    counter = {
        "R": "P",
        "P": "S",
        "S": "R"
    }

    return counter[most_common]
