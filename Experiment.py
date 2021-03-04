import os
import subprocess

TrialNumber = 0001

AccelerationSet = ["400", "600", "800", "1000", "1200", "1400", "1600", "1800", "2000", "2200"]
VelocitySet = ["200", "300", "400", "500", "600", "700", "800", "900", "1000", "1100"]
counter1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
counter2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in counter1:
    for j in counter2:
        acceleration = AccelerationSet[i]
        velocity = VelocitySet[j]
        trialString = str(TrialNumber)
        parameterString = trialString + "|" + acceleration + "|" + velocity
        sendData = parameterString.encode()
        child = subprocess.run(["python", "main.py"], input= sendData)
        TrialNumber += 1





