from file_utils import read_input_file

GAME_CONFIG = {
    "rock": {"opponent": "A", "strategy": "X", "score": 1},
    "paper": {"opponent": "B", "strategy": "Y", "score": 2},
    "scissors": {"opponent": "C", "strategy": "Z", "score": 3},
}


def main():
    guess_list = strip_newlines(read_input_file("resources/day_2_actual.txt"))
    total = sum_with_choice(guess_list)

    print(total)


def choose_option(opponent_key, strategy):
    # 0 = lost, 1 = draw, 2 = win
    win_conditions = {"X": 0, "Y": 1, "Z": 2}
    for choice in GAME_CONFIG.items():
        my_choice = choice[1].get("strategy")
        if win(guess(opponent_key), choice) == win_conditions[strategy]:
            return my_choice


def sum_with_choice(guess_list):
    total = 0
    for line in guess_list:
        opponent, strategy = split_guess_lines(line)
        my_choice = choose_option(opponent, strategy)
        total += score(opponent, my_choice)
    return total


def sum_scores(guess_list):
    total = 0
    for line in guess_list:
        opponent, me = split_guess_lines(line)
        total += score(opponent, me)
    return total


def strip_newlines(lines):
    clean = []
    for line in lines:
        clean.append(line.strip("\n"))
    return clean


def split_guess_lines(line):
    return line[0], line[2]


def score(opponent_key, strategy_key):
    total_score = 0
    opponent_guess = guess(opponent_key)
    my_guess = guess(strategy_key)
    # handle draws - needs refactor
    if win(opponent_guess, my_guess) == 2:
        total_score += 6
    if win(opponent_guess, my_guess) == 1:
        total_score += 3
    total_score += my_guess[1]["score"]
    return total_score


def guess(key):
    for option in GAME_CONFIG.items():
        if key == option[1]["opponent"]:
            return option
        if key == option[1]["strategy"]:
            return option


# 0 = lost, 1 = draw, 2 = win
def win(opponent, strategy):
    diff = opponent[1]["score"] - strategy[1]["score"]
    # badly handle wraparound
    if diff == -2:
        return 0
    # badly handle wraparound in other direction
    if diff < 0 or diff == 2:
        return 2
    if diff == 0:
        return 1
    return 0


if __name__ == "__main__":
    main()
