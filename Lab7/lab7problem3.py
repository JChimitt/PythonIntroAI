import numpy as np
import pandas as pd

testDF = pd.read_csv("lab2-test.txt", sep="\t")
test = np.loadtxt('lab2-test.txt', dtype=str)

quizDF = pd.read_csv("lab2-quiz.txt", sep="\t")
quiz = np.loadtxt('lab2-quiz.txt', dtype=str)

hwDF = pd.read_csv("lab2-hw.txt", sep="\t")
hw = np.loadtxt('lab2-hw.txt', dtype=str)

projDF = pd.read_csv("lab2-project.txt", sep="\t")
proj = np.loadtxt('lab2-project.txt', dtype=str)


aTest = (test[1 , 1:]).astype(float)
aTestGrade = (np.sum(aTest)/(100*2))*100
bTest = (test[2 , 1:]).astype(float)
bTestGrade = (np.sum(bTest)/(100*2))*100
cTest = (test[3 , 1:]).astype(float)
cTestGrade = (np.sum(cTest)/(100*2))*100
dTest = (test[4 , 1:]).astype(float)
dTestGrade = (np.sum(dTest)/(100*2))*100
eTest = (test[5 , 1:]).astype(float)
eTestGrade = (np.sum(eTest)/(100*2))*100
fTest = (test[6 , 1:]).astype(float)
fTestGrade = (np.sum(fTest)/(100*2))*100

aHW = (hw[1 , 1:]).astype(float)
aHWGrade = (np.sum(aHW)/(50*5))*100
#print(aHW)
#print(aHWGrade)
bHW = (hw[2 , 1:]).astype(float)
bHWGrade = (np.sum(bHW)/(50*5))*100
cHW = (hw[3 , 1:]).astype(float)
cHWGrade = (np.sum(cHW)/(50*5))*100
dHW = (hw[4 , 1:]).astype(float)
dHWGrade = (np.sum(dHW)/(50*5))*100
eHW = (hw[5 , 1:]).astype(float)
eHWGrade = (np.sum(eHW)/(50*5))*100
fHW = (hw[6 , 1:]).astype(float)
fHWGrade = (np.sum(fHW)/(50*5))*100

aQuiz = (quiz[1 , 1:]).astype(float)
aQuizGrade = (np.sum(aQuiz)/(10*5))*100
#print(aQuiz)
#print(aQuizGrade)
bQuiz = (quiz[2 , 1:]).astype(float)
bQuizGrade = (np.sum(bQuiz)/(10*5))*100
cQuiz = (quiz[3 , 1:]).astype(float)
cQuizGrade = (np.sum(cQuiz)/(10*5))*100
dQuiz = (quiz[4 , 1:]).astype(float)
dQuizGrade = (np.sum(dQuiz)/(10*5))*100
eQuiz = (quiz[5 , 1:]).astype(float)
eQuizGrade = (np.sum(eQuiz)/(10*5))*100
fQuiz = (quiz[6 , 1:]).astype(float)
fQuizGrade = (np.sum(fQuiz)/(10*5))*100

aProj = (proj[1 , 1:]).astype(float)
aProjGrade = (np.sum(aProj)/(100))*100
bProj = (proj[2 , 1:]).astype(float)
bProjGrade = (np.sum(bProj)/(100))*100
cProj = (proj[3 , 1:]).astype(float)
cProjGrade = (np.sum(cProj)/(100))*100
dProj = (proj[4 , 1:]).astype(float)
dProjGrade = (np.sum(dProj)/(100))*100
eProj = (proj[5 , 1:]).astype(float)
eProjGrade = (np.sum(eProj)/(100))*100
fProj = (proj[6 , 1:]).astype(float)
fProjGrade = (np.sum(fProj)/(100))*100
#print(aProj)
#print(aProjGrade)


gradeMatrix = np.matrix([[aTestGrade, aHWGrade, aQuizGrade, aProjGrade],
                         [bTestGrade, bHWGrade, bQuizGrade, bProjGrade],
                         [cTestGrade, cHWGrade, cQuizGrade, cProjGrade],
                         [dTestGrade, dHWGrade, dQuizGrade, dProjGrade],
                         [eTestGrade, eHWGrade, eQuizGrade, eProjGrade],
                         [fTestGrade, fHWGrade, fQuizGrade, fProjGrade]])

weightMatrix = np.matrix([[.40],
                          [.30],
                          [.10],
                          [.20]])

weightedGrades = np.matmul(gradeMatrix, weightMatrix)
weightedRounded = np.matrix.round(weightedGrades, decimals=2)
print("Student A's Final Grade: ", weightedRounded.item(0))
print("Student B's Final Grade: ", weightedRounded.item(1))
print("Student C's Final Grade: ", weightedRounded.item(2))
print("Student D's Final Grade: ", weightedRounded.item(3))
print("Student E's Final Grade: ", weightedRounded.item(4))
print("Student F's Final Grade: ", weightedRounded.item(5))















