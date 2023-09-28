seetbed = [4, 1, 1, 4]
max_berry = 0
if len(seetbed) < 4:
    max_berry = sum(seetbed)
else:
    for i in range(-1, len(seetbed) - 1):
        berry = seetbed[i - 1] + seetbed[i] + seetbed[i + 1]
        if max_berry < berry:
            max_berry = berry
print(max_berry)
