dungeon = ['&|&|&|&&&|&|||&&&|&&|||&||&||&|&&|||||&|&|&&&&||||&&&|&|&&||||&&&|&&|||&&|&&&|||', ' &&||&&&|&||&&&||&|||&&&|&||&&&|||||||&&&&|&&||&||&&|||&|&&&&&&|&|||&&||&|||&&|&|', '&|&|&&&&|&&&|&|||&&&||||||&&|&&&&|&&|&&&|&||&|&&|||&&&|&&&&&|&&&&&&||&|&&||&&|&&', '&|&&|||||&&&&||&&&||||&&&&|||||&||&|&|&|&||&|&&|&|&||||||&&||||||&|&&|&&&&&&||||', '&||&&||&|&||&|&|&&&&&||&&&&&&&||&&|&&||&|&|&|&&&&|&&|||||&&&||||&||&&&|||&&&|||&', ' &&&&|&&|&|&&&|||&&&||||&|&|&&|&&&|&&&|||&|&&&|&|&&&|&&|||&|&|&|&|&&|&&&&|&&|||||', '&&|&|&||||&||||&&|||&&&|||&&||&|&|||&||&&&||||&|&|&&|&&&|&&&|&&|&||&|&&&|&&&||||', '&&&||||&&&&&|&|&&&&||&&|&|||&&&||&&&&|&&&|&&|&||&|&&|&||||&|&|||&|&||&||&|&&&&||', '&&&|&&&||&||&||&|&|&||&&&|||||&|&&||&&&|||&|||||||&&|||&&||&|&|&|&|&&&&&&||&|&||', '&&||&&|&&|||||&&&||&|&|&|&|&||&|&||&&&&||||&|&|||||||&|&&&&|&&|||||&|&||&&&||&|&']

# split each item every time there is a slash and count number of keys

for i in range(len(dungeon)):
    levels = dungeon[i].split('|')
    keyCount = 0
    for j in range(len(levels)):
        keyCount += (len(levels[j]) - 1)
        if(keyCount < 0):
            print('0')
            break 
    if(keyCount > 0):
        print('1')

print(len(dungeon))


        