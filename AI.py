vBoard = [" ", "x", "x"]

vList = []

for i in vBoard:
    if i in " ":
        vList.append("Space")
    else:
        vList.append("NotSpace")

print(vList)
