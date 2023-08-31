data = [i.strip() for i in open("adventofcode2022_day_4_data")]
data = list(data)
data = [i.split(",") for i in data]

print(data)
contains = 0


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

    if num1 <= num3 and num4 <= num2 or num3 <= num1 and num2 <= num4:
        contains += 1

print(contains)




