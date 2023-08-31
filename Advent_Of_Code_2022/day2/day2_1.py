opponent = {"A": "rock",
            "B": "paper",
            "C": "scissors"}

me = {"X": "rock",
      "Y": "paper",
      "Z": "scissors"}

shape = {"rock": 1,
         "paper": 2,
         "scissors": 3}

outcome = {"lost": 0,
           "draw": 3,
           "win": 6}

data = [lst.strip() for lst in open("adventofcode2022_day2_data")]
data = list(data)
length = len(data)


# column 1 is opponent
# column 2 is me

# total points = sum of round scores
# round scores = outcome + shape played


def rock(shape1):
    if shape1 == "scissors":
        return "win"
    else:
        return "lost"


def paper(shape1):
    if shape1 == "rock":
        return "win"
    else:
        return "lost"


def scissors(shape1):
    if shape1 == "paper":
        return "win"
    else:
        return "lost"


def decide(shape1, shape2):
    # shape1 = opponent
    shape1 = opponent[shape1]
    # shape2 = me
    shape2 = me[shape2]

    if shape1 == shape2:
        return outcome["draw"]
    elif shape2 == "rock":
        return outcome[rock(shape1)]
    elif shape2 == "paper":
        return outcome[paper(shape1)]
    else:
        return outcome[scissors(shape1)]


round_scores = []

for row in range(length):
    shape1 = data[row][0]
    shape2 = data[row][2]
    round_scores.append(decide(shape1, shape2) + shape[me[data[row][2]]])

print(sum(round_scores))
