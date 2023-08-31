data = [i.strip() for i in open("adventofcode2022_day_4_data")]
data = list(data)
data = [i.split(",") for i in data]

overlap = 0


for line in data:
    nums = []
    for elf in line:
        idx = elf.index("-")
        nums.append(int(elf[0:idx]))
        nums.append(int(elf[idx+1:len(elf)]))

    num1 = nums[0]
    num2 = nums[1]
    num3 = nums[2]
    num4 = nums[3]

    if set(range(num1, num2 + 1)) & set(range(num3, num4 + 1)):
        overlap += 1



print(overlap)
