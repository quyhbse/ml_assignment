import numpy as np

class Assignment:
    def __init__(self, file_name):
        self.filename = file_name

    def readFile(self):
        file = self.filename + '.txt'
        files = np.array(['class1.txt', 'class2.txt', 'class3.txt', 'class4.txt',
                          'class5.txt', 'class6.txt', 'class7.txt', 'class8.txt'])
        if file in files:
            try:
                with open('Data Files/' + file, 'r') as f:
                    print("Successfully opened " + file)
                    # 1. Báo cáo tổng số dòng dữ liệu được lưu trữ trong tệp
                    lines = f.readlines()
                    total = len(lines)
                    print('Total lines:', total)

                    # 2. report thống kê lỗi dữ liệu
                    print("**** ANALYZING ****")
                    errorValid = 0
                    for index, line in enumerate(lines):
                        row = line.split(",")
                        lenColumn = len(row)
                        i = 0
                        if lenColumn != 26:
                            print("Invalid line of data: does not contain exactly 26 values:")
                            print(",".join(row))
                            errorValid += 1
                        else:
                            while i < lenColumn:
                                if not row[i]:
                                    print("Invalid line of data:" + row[0] + " is invalid")
                                    print(",".join(row))
                                    errorValid += 1
                                    break
                                i += 1
                    if errorValid != 0:
                        print("**** REPORT ****")
                        print("Total valid lines of data:" + str(total - errorValid))
                        print("Total invalid lines of data:" + str(errorValid))
                    else:
                        print("No errors found!")
                    # 3. Kiểm tra kết quả chấm điểm.
                    answers = np.array("B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D".split(","))
                    arrTotalScore = []
                    result = []
                    for index, line in enumerate(lines):
                        totalScore = 0
                        row = line.rstrip("\n").split(",")[1:]
                        lenCols_ = len(row)
                        i = 0
                        while i < lenCols_:
                            if i < len(answers):
                                if row[i] == answers[i]:
                                    totalScore += 4
                                elif not row[i]:
                                    totalScore += 0
                                else:
                                    totalScore -= 1
                            i += 1
                        arrTotalScore.append(totalScore)
                        result.append(line.split(",")[0] + ',' + str(totalScore))
                    # 3.1 Thống kê.
                    totalScore_ = np.sort(np.array(arrTotalScore))
                    mid = len(totalScore_) // 2
                    print('Mean (average) score: ' + str(totalScore_.mean()))
                    print('Highest score: ' + str(totalScore_.max()))
                    print('Lowest score: ' + str(totalScore_.min()))
                    print('Range of scores: ' + str((totalScore_.max() - totalScore_.min())))
                    print('Median score: ' + str((totalScore_[mid] + totalScore_[~mid]) / 2))
                    # 4. Output Kết quả
                    with open('Data Files/Expected Output/' + '_' + file, 'w') as output:
                        output.write('\n'.join(result))
            except IOError as e:
                print(f"Couldn't open or write to file({e})")
        else:
            print("File cannot be found.")


filename = input("Enter a class file to grade:")
task = Assignment(filename)
task.readFile()
