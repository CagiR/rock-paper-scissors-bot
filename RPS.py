import random

def player(prev_play, opponent_history=[]):
    # Simpan history langkah lawan
    if prev_play != "":
        opponent_history.append(prev_play)

    # Dua langkah pertama: random (biar tidak ketebak)
    if len(opponent_history) < 2:
        return random.choice(["R", "P", "S"])

    # Hitung frekuensi langkah lawan
    counts = {
        "R": opponent_history.count("R"),
        "P": opponent_history.count("P"),
        "S": opponent_history.count("S")
    }

    # Cari langkah yang paling sering dipakai lawan
    most_common = max(counts, key=counts.get)

    # Counter move
    counter = {
        "R": "P",  # Rock dikalahkan Paper
        "P": "S",  # Paper dikalahkan Scissors
        "S": "R"   # Scissors dikalahkan Rock
    }

    return counter[most_common]
