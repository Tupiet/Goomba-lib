#file = open("course1_bgdatL0.bin", "rb")

def read_bgdat(file):
    # Read the whole file and save it in a variable
    data = file.read()

    # This is the index
    index = 0

    # Creates a dictionary to store the data
    objectDic = {'tilesetID':0, 'objectID':0, 'posX':0, 'posY':0, 'lenX':0, 'lenY':0}
    # Creates a list to store the diferent dictionaries
    byteInfo = []

    # This will loop through the whole file, and save the data in a dictionary
    # Then, when the dictionary is full, it will append it to the list
    for i in data:
        if index == 0:
            objectDic['tilesetID'] = i >> 4 # This is done because we only want the first bit
        elif index == 1:
            objectDic['objectID'] = i
        elif index == 3:
            objectDic['posX'] = i
        elif index == 5:
            objectDic['posY'] = i
        elif index == 7:
            objectDic['lenX'] = i
        elif index == 9:
            objectDic['lenY'] = i
            # Let's append the dictionary to the list
            byteInfo.append(objectDic) 
            # This will reset the dictionary, necessary to read the next object
            objectDic = {} 
        index += 1

        if index == 10:
            index = 0 # Resets the index, so it can start again
        
    return byteInfo, data, len(data) % 10