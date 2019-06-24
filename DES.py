PC1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3,
       60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37,
       29, 21, 13, 5, 28, 20, 12, 4]

PC2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52,
       31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

Rotations = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
expansionPermutation = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15,
                        16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28,
                        29, 28, 29, 30, 31, 32, 1]

IP = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 30, 22, 14,
      6, 64, 56, 48, 40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11,
      3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]
InIP = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10,
        50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]
straightPermutation = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14,
                       32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]
s_box = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
          [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
          [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
          [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13], ],
         [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
          [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
          [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
          [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9], ],
         [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
          [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
          [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
          [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12], ],
         [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
          [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
          [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
          [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14], ],
         [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
          [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
          [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
          [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3], ],
         [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
          [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
          [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
          [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13], ],
         [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
          [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
          [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
          [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12], ],
         [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
          [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
          [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
          [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11], ]]


def shift(seq, n):
    n = n % len(seq)
    return seq[n:] + seq[:n]


def dtox(input5):
    wmap = {0: "0",
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            10: "A",
            11: "B",
            12: "C",
            13: "D",
            14: "E",
            15: "F"
            }
    v = 0
    output1 = ""

    while v < len(input5):
        output1 = output1 + wmap[input5[v]]
        v = v + 1
    return output1


def btox(input2):
    wmap = {"0000": "0",
            "0001": "1",
            "0010": "2",
            "0011": "3",
            "0100": "4",
            "0101": "5",
            "0110": "6",
            "0111": "7",
            "1000": "8",
            "1001": "9",
            "1010": "A",
            "1011": "B",
            "1100": "C",
            "1101": "D",
            "1110": "E",
            "1111": "F"
            }
    q = 0
    output1 = ""

    while q < len(input2):
        output1 = output1 + wmap[input2[q:q + 4]]
        q = q + 4

    #output1 = output1.lstrip("0")
    #output1 = "0" if len(output1) == 0 else output1

    return output1


def xtob(hexanum):
    hmap = {"0": "0000",
            "1": "0001",
            "2": "0010",
            "3": "0011",
            "4": "0100",
            "5": "0101",
            "6": "0110",
            "7": "0111",
            "8": "1000",
            "9": "1001",
            "A": "1010",
            "B": "1011",
            "C": "1100",
            "D": "1101",
            "E": "1110",
            "F": "1111"
            }
    w = 0
    output2 = ""

    while w < len(hexanum):
        output2 = output2 + hmap[hexanum[w]]
        w = w + 1

    return output2


HexaNum = input()
input1 = input()
no = input()
no_iterations = int(no)
biNumArr = []
biNum = xtob(HexaNum)
biNumArr = list(str(biNum))
FirstOutputKey = []
for ikey in PC1:
    x = biNumArr[ikey-1]
    FirstOutputKey.append(x)
inputR = FirstOutputKey[0:28]
inputL = FirstOutputKey[28:56]
PC2InputR = []
PC2InputL = []
PCInput = []
key = []

for j in range(no_iterations):

    if j > 0:
        PC2InputR.append(shift(PC2InputR[j-1], Rotations[j]))
        PC2InputL.append(shift(PC2InputL[j - 1], Rotations[j]))

        #print(Rotations[j])
    else:
        PC2InputR.append(shift(inputR, Rotations[j]))
        PC2InputL.append(shift(inputL, Rotations[j]))

    PCInput.append([*PC2InputR[j], *PC2InputL[j]])
    SecondOutputKey = []
    input3Key = ''
    for k in PC2:
        x = PCInput[j][k - 1]
        SecondOutputKey.append(x)
    #print(SecondOutput)
    input3Key = ('{}' * len(SecondOutputKey)).format(*SecondOutputKey)
    key.append(input3Key)
    SecondOutputKey = []
binaryInput = xtob(input1)
binaryInputArr = list(str(binaryInput))
binaryInputArrR = binaryInputArr[32:64]
binaryInputArrL = binaryInputArr[0:32]
FirstOutput = []
XOROutput = ''
intialOutput =[]
for intial in IP:
    x = binaryInputArr[intial-1]
    intialOutput.append(x)
inputintial = ('{}'*len(intialOutput)).format(*intialOutput)
binaryInputArr = list(str(inputintial))
binaryInputArrR = binaryInputArr[32:]
binaryInputArrL = binaryInputArr[0:32]
binaryleft = inputintial[0:32]

if no_iterations == 0:
    print(input1)
else:
    for itera in range(no_iterations):
        KeyArr = list(str(key[itera]))
        if itera != 0:
            binaryInputArr = list(str(input3))
            binaryInputArrR = binaryInputArr[32:]
            binaryInputArrL = binaryInputArr[0:32]
            binaryleft = input3[0:32]

        for ix in expansionPermutation:
            x = binaryInputArrR[ix-1]
            FirstOutput.append(x)
        input30 = ('{}'*len(FirstOutput)).format(*FirstOutput)

        XOROutput = bin(int(input30, 2) ^ int(key[itera], 2))[2:].zfill(48)
        #for j in range(len(key[itera])):
         #   o = int(FirstOutput[j])
          #  t = int(KeyArr[j])
           # r = o ^ t
            #XOROutput += str(r)
        SboxInput = []
        m = 0
        while m < len(XOROutput):
            SboxInput.append(XOROutput[m:m + 6])
            m += 6
        l1 = 0
        row = 0
        col = 0
        u = 1
        c = 0
        output1 = []
        while l1 < len(s_box):
            col = int(SboxInput[l1][u:u+4], 2)
            row = int(SboxInput[l1][c] + SboxInput[l1][len(SboxInput[l1])-1], 2)
            output1.append(s_box[l1][row][col])
            l1 += 1
        SBOXoutput = dtox(output1)
        straightPBoxInput = xtob(SBOXoutput)
        straightPBoxInputArr = list(str(straightPBoxInput))

        Last = []
        for ii in straightPermutation:
            x = straightPBoxInputArr[ii-1]
            Last.append(x)
        outputArr2 = ''
        xor2out = ''
        input10 = ('{}'*len(Last)).format(*Last)
        xor2out = bin(int(binaryleft, 2) ^ int(input10, 2))[2:].zfill(32)
        #for xorxor in range(len(input10)):
         #   element1 = int(input10[xorxor])
          #  element2 = int(binaryInputArrL[xorxor])
           # result = element1 ^ element2
            #xor2out += str(result)
        inputtonext = xor2out
        myarr = ('{}' * len(binaryInputArrR)).format(*binaryInputArrR)
        input3 = myarr + inputtonext
    TheOutput = []
    for invers in InIP:
        x = input3[invers-1]
        TheOutput.append(x)
    lastinput = ('{}'*len(TheOutput)).format(*TheOutput)
    outputArr2 = btox(lastinput)
    print(outputArr2)
