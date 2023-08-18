import csv
import cv2 as cv
import numpy as np
# Set up training data

#true or false for each letter
label1 = np.ones(21, dtype=int) #1 are the right letter
label0 = np.zeros(457, dtype=int) #0 are the other letters
labels = np.concatenate((label1, label0), dtype=int)
# print(labels)

#bring data in
trainingData = []
with open("Input.csv") as f:
    _ = next(f)  # skip header
    for line in csv.reader(f):
        temp = []
        for element in line:
            temp.append(float(element))
        trainingData.append(temp)

# Train the SVM
svm = cv.ml.SVM_create()
svm.setType(cv.ml.SVM_C_SVC)
svm.setKernel(cv.ml.SVM_LINEAR)
svm.setTermCriteria((cv.TERM_CRITERIA_MAX_ITER, 100, 1e-6))
svm.train(trainingData, cv.ml.ROW_SAMPLE, labels) #load data to train

# Show the decision regions given by the SVM
response = svm.predict(trainingData)[1] #get a new 1x88 CLEAN, sampleMatrix is a matrix, [1] grabs row in matrix
print(response)

