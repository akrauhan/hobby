from helpFunctions import txt2IntTable as txt2Table

puzzleInput = txt2Table("aoc2.txt")

def opCodes(t):
  i = 0
  while (i < len(t)):
    if t[i] == 1:
      t[t[i+3]] = t[t[i+1]] + t[t[i+2]]
      i += 4
      continue
 
    if t[i] == 2:
      t[t[i+3]] = t[t[i+1]] * t[t[i+2]]
      i += 4
      continue
 
    if t[i] == 99:
      return t[0]

print(opCodes(puzzleInput))

def findVerbAndNoun(opcode, n):
    i = 1
    j = 0
    while (i <= 99):
      while (j <= 99):
        puzzle = opcode
        puzzle[1] = i
        puzzle[2] = j
        outPut = opCodes(puzzle)
    
        print("i:" + str(i) + "," + str(j) + " o:" + str(outPut))
        if (outPut == n):
          print("Löytyi: " + str(100*i + j))
          return(100*i + j)
        j+=1
      i+=1
      j = 0
        