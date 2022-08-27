import math

import numpy as np
import pandas as pd
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)


class Assignment:
    def __init__(self, file_name):
        self.filename = file_name

    def readFile(self):
        file = self.filename + '.txt'
        files = np.array(['class1.txt', 'class2.txt', 'class3.txt', 'class4.txt',
                          'class5.txt', 'class6.txt', 'class7.txt', 'class8.txt'])
        if file in files:
            try:
                colsName = ["Code", "Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8", "Q9", "Q10",
                            "Q11", "Q12", "Q13",
                            "Q14", "Q15", "Q16", "Q17", "Q18", "Q19", "Q20", "Q21", "Q22", "Q23",
                            "Q24", "Q25"]
                data = pd.read_csv('Data Files/' + file, delimiter=',', header=None)
                print("Successfully opened " + str(file))
                df = pd.DataFrame(data)
                df.columns = colsName
                row, col = df.shape
                totalError = 0
                print("Total lines:" + str(row))

                print('**** ANALYZING ****')
                for i, j in df.iterrows():
                    if pd.isnull(j.Q25):
                        print('Invalid line of data: does not contain exactly 26 values:')
                        print(j.tolist())
                        totalError += 1
                        break
                    for name in colsName:
                        if pd.isnull(j[name]):
                            j = j.tolist()
                            print('Invalid line of data: ' + j[0] + ' is invalid')
                            print(j)
                            totalError += 1
                            break
                if totalError != 0:
                    print("**** REPORT ****")
                    print("Total valid lines of data: " + str(row - totalError))
                    print("Total invalid lines of data: " + str(totalError))
                else:
                    print("No errors found!")
                arrTotalScore = []
                result = []
                answers = np.array("B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D".split(","))
                for i, j in df.iterrows():
                    totalScore = 0
                    for index, name in enumerate(colsName[1:26]):
                        if j[name] == answers[index]:
                            totalScore += 4
                        elif type(j[name]) == float:
                            totalScore += 0
                        else:
                            totalScore -= 1
                    arrTotalScore.append(totalScore)
                    result.append(j.Code + ',' + str(totalScore))

                totalScore_ = np.sort(np.array(arrTotalScore))
                mid = len(totalScore_) // 2
                print('Mean (average) score: ' + str(totalScore_.mean()))
                print('Highest score: ' + str(totalScore_.max()))
                print('Lowest score: ' + str(totalScore_.min()))
                print('Range of scores: ' + str((totalScore_.max() - totalScore_.min())))
                print('Median score: ' + str((totalScore_[mid] + totalScore_[~mid]) / 2))
                with open('Data Files/Expected Output/' + '_' + file, 'w') as output:
                    output.write('\n'.join(result))
            except IOError as e:
                print(f"Couldn't open or write to file({e})")
        else:
            print("File cannot be found.")


filename = input("Enter a class file to grade:")
task = Assignment(filename)
task.readFile()
