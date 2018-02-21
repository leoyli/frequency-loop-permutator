# Author    :  Leo Y. Li
# Licence   :  MIT
# Release   :  2018/02/21
# Version   :  1.1.2

def checkLoop(inputList, deviations=0.003, minimumSeparations=0, rounded=True, instantOutput=False, reportRates=250):
    # option insurance
    deviations = abs(deviations)
    reportRates = abs(reportRates)
    minimumSeparations = abs(minimumSeparations)

    # Initialize a blank array for result storage
    global recordBook
    recordBook = []

    # Clean & Sort the input file (from small to large value)
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
            print("\ncalculating... currently at", A, "-th line in the sequence.")

        for B in range(A + 1, length):
            if (inputList[B] - inputList[A]) < minimumSeparations:
                continue
            for C in range(B + 1, length):
                if (inputList[C] - inputList[B]) < minimumSeparations:
                    continue
                for D in range(C + 1, length):
                    if (inputList[D] - inputList[C]) < minimumSeparations:
                        continue

                    # check criteria for a loop
                    errors = round(abs(inputList[D] - inputList[C] - inputList[B] + inputList[A]), 4)
                    if errors <= deviations:
                        newFoundLoop = [inputList[D], inputList[C], inputList[B], inputList[A], errors]
                        recordBook.append(newFoundLoop)
                        if instantOutput:
                            print(",  ".join('{:9.3f}'.format(i) for v, i in enumerate(newFoundLoop)))

    # final reports
    if not instantOutput:
        result()
    else:
        print("\nALL DONE!  Numbers of loop being found:", len(recordBook))
        print("To show all found loops, command 'result()' before making another permutation.")


def result():
    print("\nAll found closed frequencies loops:\n", "_"*75, "\n\n\t#1,\t\t#2,\t\t$3,\t\t#4,\t    errors\n", "_"*75, "\n")
    for n in range(len(recordBook)):
        print(",\t".join('{:10.3f}'.format(i) for v, i in enumerate(recordBook[n])))
    print("", "_"*75, "\n {:>70}".format("Total:"), len(recordBook))
