import random


def coin_toss(coin_tosses = 1000000):
    head_count = 0
    tail_count = 0


    for x in range(coin_tosses):
        toss = random.choice(["H", "T"])
        if toss == "H":
            head_count = head_count + 1
        else:
            tail_count = tail_count + 1

    print(f"Heads: {head_count}")
    print(f"Tails: {tail_count}")