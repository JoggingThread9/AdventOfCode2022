data = []
with open("day7_data_test") as data_file:
    for line in data_file:
        data.append(line.rstrip("\n"))
        commands =

# $ calls a command

########## commands ##########
# cd : changes directory
    # cd x : finds x directory in current directory and makes x directory the current directory
    # cd .. : moves out of current directory into the previous directory
    # cd / : makes the current directory the outermost directory
# ls : prints out all the files and directories contained in the current directory
##############################

# 123 abc means the current directory contains a file named abc with size 123
# dir xyz means the current directory contains a directory xyz

files = {}

# files.__setitem__(key, definition)

curr_dir = None

for line in data:
    pass







