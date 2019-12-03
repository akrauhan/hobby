#from helpFunctions import txt2IntTable as txt2Table

puzzleInput = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,19,5,23,2,13,23,27,1,10,27,31,2,6,31,35,1,9,35,39,2,10,39,43,1,43,9,47,1,47,9,51,2,10,51,55,1,55,9,59,1,59,5,63,1,63,6,67,2,6,67,71,2,10,71,75,1,75,5,79,1,9,79,83,2,83,10,87,1,87,6,91,1,13,91,95,2,10,95,99,1,99,6,103,2,13,103,107,1,107,2,111,1,111,9,0,99,2,14,0,0]

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
    
    return 0

#puzzleInput[1] = 12
#puzzleInput[2] = 2
#print(opCodes(puzzleInput)) # Task 1 Correct

puzzleInput[1] = 0
puzzleInput[2] = 0 

def findVerbAndNoun(opcode, n):
    i = 1
    j = 0
    while (i <= 99):
      while (j <= 99):
        puzzle = opcode.copy()
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

findVerbAndNoun(puzzleInput, 19690720) # Task 2 correct