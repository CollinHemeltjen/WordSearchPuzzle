import re

DEV_MODE = True
PUZZLE_FILE_NAME = "puzzle.txt"
WORDLIST_FILE_NAME = "wordList.txt"

def main():
    puzzle = getPuzzle()
    wordList = getWordList()
    printPuzzle(puzzle)
    printWordList(wordList)

    searchWords(puzzle, wordList)

def searchWords(puzzle, wordList):
    for word in wordList:
        print("checking word: ", word)
        for rowIndex, row in enumerate(puzzle, start=0):
            # print("is ", word," in ",row,"?")
            for charIndex,char in enumerate(row, start=0):
                # print("start cheching from ",char)
                check(puzzle, rowIndex, charIndex, word)

def check(puzzle, rowIndex, charIndex, word):
    if puzzle[rowIndex][charIndex] != word[0]:
        # print(word, " doesn't start with ", puzzle[rowIndex][charIndex])
        return

    checkHorizontal(puzzle, rowIndex, charIndex, word)

def checkHorizontal(puzzle, rowIndex, charIndex, word):
    # check in front
    if checkHorizontalFront(puzzle, rowIndex, charIndex, word):
        return True
    #check the back
    if checkHorizontalBack(puzzle, rowIndex, charIndex, word):
        return True
    # not found
    return False

def checkHorizontalFront(puzzle, rowIndex, charIndex, word):
    j = 0
    found = True
    row = puzzle[rowIndex]

    # is there enough space for the word to exist?
    if len(word) > (len(row) - charIndex):
        return False

    for i in range(charIndex, charIndex+len(word)):
        # is the next character equal to the next word character?
        if row[i] != word[j]:
            found = False
            break
        j += 1

    if found:
        print(word," found at ", rowIndex, ",", charIndex, "-", rowIndex,",",charIndex+len(word))

    return found

def checkHorizontalBack(puzzle, rowIndex, charIndex, word):
    # check behind
    j = 0
    found = True
    row = puzzle[rowIndex]

    # is there enough space for the word to exist?
    if charIndex - len(word) < 0:
        return False

    for i in range(charIndex, charIndex-len(word),-1):
        # is the next character equal to the next word character?
        if row[i] != word[j]:
            found = False
            break
        j += 1

    if found:
        print(word," found at ", rowIndex, ",", charIndex, "-", rowIndex,",",charIndex-len(word))

    return found

# Creates a (for the program readable) table
def getPuzzle():
    puzzleFile = getPuzzleFile()
    inputText = puzzleFile.read().splitlines()

    puzzle = list()
    for row in inputText:
        string_without_whitespace = re.sub(r"\s+", "", row)
        puzzle.append(list(string_without_whitespace))
    return puzzle

# Creates a list of words to search
def getWordList():
    wordListFile = getWordListFile()
    return wordListFile.read().splitlines()

# Retrieves a string representing the puzzle form an input file
def getPuzzleFile():
    if DEV_MODE:
        return open(PUZZLE_FILE_NAME,"r")

    print("Input file puzzle:")
    return open(input(),"r")

# Retrives a string representing the words to search form an input file
def getWordListFile():
    if DEV_MODE:
        return open(WORDLIST_FILE_NAME, "r")

    print("Input file word list:")
    return open(input(),"r")

def printPuzzle(puzzle):
    for row in puzzle:
        for char in row:
            print(str(char).strip("[]'',"), end="  ")
        print("\n")

def printWordList(wordList):
    for word in wordList:
        print(str(word).strip("[]'',"))

if __name__ == '__main__':
    main()
