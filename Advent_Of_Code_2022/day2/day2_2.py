# total score still calculated the same
# first column being the opponent's move is the same
# second column now means what the outcome of the match should be

# opponent's move
column1 = {"A": "rock",
           "B": "paper",
           "C": "scissors"}

# what the outcome should be
column2 = {"X": "lose",
           "Y": "draw",
           "Z": "win"}

# points for each shape
shape_points = {"rock": 1,
                "paper": 2,
                "scissors": 3}

# points for each outcome
outcome_points = {"lose": 0,
                  "draw": 3,
                  "win": 6}

data = [lst.strip() for lst in open("adventofcode2022_day2_data")]
data = list(data)
length = len(data)


def draw(opponent):
    if opponent == "rock":
        return outcome_points["draw"] + shape_points["rock"]
    elif opponent == "paper":
        return outcome_points["draw"] + shape_points["paper"]
    else:
        return outcome_points["draw"] + shape_points["scissors"]


def lose(opponent):
    if opponent == "rock":
        return outcome_points["lose"] + shape_points["scissors"]
    elif opponent == "paper":
        return outcome_points["lose"] + shape_points["rock"]
    else:
        return outcome_points["lose"] + shape_points["paper"]


def win(opponent):
    if opponent == "rock":
        return outcome_points["win"] + shape_points["paper"]
    elif opponent == "paper":
        return outcome_points["win"] + shape_points["scissors"]
    else:
        return outcome_points["win"] + shape_points["rock"]


def decide(opponent, outcome):
    opponent = column1[opponent]

    outcome = column2[outcome]

    if outcome == "draw":
        return draw(opponent)
    elif outcome == "lose":
        return lose(opponent)
    else:
        return win(opponent)


round_scores = []

for row in range(length):
    opponent = data[row][0]
    outcome = data[row][2]

    round_scores.append(decide(opponent, outcome))

print(sum(round_scores))
