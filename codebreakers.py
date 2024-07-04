import random

if __name__ == "__main__":
    code = [[random.randrange(0,9), 0], [random.randrange(0,9), 0], [random.randrange(0,9), 0], [random.randrange(0,9), 0]]
    codeInt = [code[0][0], code[1][0], code[2][0], code[3][0]]
    correct = False
    
    while correct is False:
        for num in code:
            num[1] = 0

        correctNumAndPos = 0
        correctNumNotPos = 0
        i = 0

        guess = input("Enter your 4 digit guess (no spaces): ")
        
        for val in guess:
            if int(val) in codeInt:
                for num in code:
                    if int(val) == num[0] and num[1] == 0:
                        num[1] = 1
                        correctNumNotPos += 1
                        break

            if int(val) == codeInt[i]:
                correctNumAndPos += 1
                code[i][1] = 1

            i += 1

        if correctNumAndPos == 4:
            print("Correct! The code was " + str(code[0][0]) + str(code[1][0]) + str(code[2][0]) + str(code[3][0]) + ". Great work!")
            playAgain = input("Play again (Y/N): ")

            if playAgain == 'N':
                correct = True
            else:
                code = [[random.randrange(0,9), 0], [random.randrange(0,9), 0], [random.randrange(0,9), 0], [random.randrange(0,9), 0]]
                codeInt = [code[0][0], code[1][0], code[2][0], code[3][0]]
                
        else:
            correctNumNotPos -= correctNumAndPos
            print("You have " + str(correctNumAndPos) + " numbers in the correct position.")
            print("You have " + str(correctNumNotPos) + " numbers correct, but in the wrong position.\n")
