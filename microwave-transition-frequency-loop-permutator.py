# Author    :  Leo Y. Li
# Release   :  2017/09/08
# Version   :  1.0.0



def checkLoop(inputList, deviations=0.03, minimumSeparations=0, rounded=True, instantOutput=True, reportRates=50):
    # option insurance
    deviations = abs(deviations)
    reportRates = abs(reportRates)
    minimumSeparations = abs(minimumSeparations)

    # Initialize a blank array for result storage
    global recordBook
    recordBook = []

    # Clean & Sort the input file (from samll to large value)
    if rounded:
        inputList = list(set([round(n, 3) for n in inputList]))
    inputList = sorted(inputList)
    length = len(inputList)

    # initial reports
    print("Lines to be permuted:", length)

    # permutation
    for A in range(length):
        if A % reportRates == 0:
            # progression reports
            print("calculating... currently at", A, "-th line in the sequence.")

        for B in range(A + 1, length):
            for C in range(B + 1, length):
                for D in range(C + 1, length):

                    # check options: minimum separations between any two lines (for time saving)
                    if minimumSeparations > 0:
                        separations = [inputList[B] - inputList[A], inputList[C] - inputList[B],
                                       inputList[D] - inputList[C]]

                        # if meet the threshold, skip the rest of calculations
                        if True in list(map(lambda i: i < minimumSeparations, separations)):
                            break

                    # check criteria for a loop
                    errors = abs(inputList[A] - inputList[B] - inputList[C] + inputList[D])
                    if errors <= deviations:
                        newFoundLoop = [inputList[A], inputList[B], inputList[C], inputList[D], round(errors, 3)]
                        recordBook.append(newFoundLoop)
                        if instantOutput:
                            print(newFoundLoop)

    # final reports
    print("\nALL DONE!  Numbers of loop being found:", len(recordBook))
    print("To recall all found loops, command 'recordBook' before making another permutation.")