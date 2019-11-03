colors = {}
colors["R"] = 0
colors["B"] = 1
colors["Y"] = 2
colors["G"] = 3

colorsRet = ["G", "B", "Y", "G"]


# @function nextColor
# Get the next color based on turn color
def nextColor(turn):
    return colorsRet[((colors[turn] + 1) % 4)]
