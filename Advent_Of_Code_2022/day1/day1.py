data = [lst.strip() for lst in open("adventofcode20222_day1_data.csv")]
totals, total = [], 0
for calories in data:
    if calories == "":
        totals.append(total)
        total = 0
    else:
        total += int(calories)
totals = sorted(totals)
print(totals[-1], totals[-1] + totals[-2] + totals[-3])
