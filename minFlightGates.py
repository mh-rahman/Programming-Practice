#!/bin/python3

import math
import os
import random
import re
import sys



from collections import deque

#
# Complete the 'getMinGates' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY landingTimes
#  2. INTEGER_ARRAY takeOffTimes
#  3. INTEGER maxWaitTime
#  4. INTEGER initialPlanes
#


class Solution():
    def __init__(self, landingTimes, takeOffTimes, maxWaitTime, initialPlanes):
        print(landingTimes, takeOffTimes, maxWaitTime, initialPlanes)
        self.landingTimes = landingTimes
        self.takeOffTimes = takeOffTimes
        self.maxWaitTime = maxWaitTime
        self.initialPlanes = initialPlanes
        self.planesOnRunway = deque()
        self.totalGates = initialPlanes
        self.gatesOccupied = initialPlanes
        self.gatesFree = 0
        return

    def deleteLater(self):
        '''
        15
        347
        411
        502
        559
        612
        737
        814
        830
        1000
        1000
        1154
        1614
        1816
        2052
        2147
        11
        231
        412
        424
        734
        740
        1000
        1325
        1523
        1644
        2201
        2254
        41
        2
        '''
        pass

    def landOnRunway(self, landingTime):
        waitTime = landingTime + self.maxWaitTime
        if waitTime%100 >= 60:
            # Ensure time is correctly represented
            hours = waitTime//100
            mins = waitTime%100
            hours += mins//60
            mins = mins%60
            waitTime = hours*100 + mins
        self.planesOnRunway.append(waitTime)
        return

    def runwayToGate(self):
        if self.gatesFree > 0:
            # Free gates available. Assign One. No need to update totalGates value.
            self.gatesFree -= 1
            self.gatesOccupied += 1
        else:
            # No free gates available. Add new gate. Update totalGates value
            self.gatesOccupied += 1
            self.totalGates = max(self.totalGates, self.gatesFree + self.gatesOccupied)
        return

    def getMinGates(self):
        t,l = 0, 0
        while l < len(self.landingTimes) and t < len(self.takeOffTimes):
            while self.planesOnRunway and self.planesOnRunway[0] < min(self.landingTimes[l], self.takeOffTimes[t]):
                self.planesOnRunway.popleft()
                self.runwayToGate()

            if self.landingTimes[l] < self.takeOffTimes[t]:
                # Land plane on runway, add to planesOnRunway
                self.landOnRunway(self.landingTimes[l])
                l += 1
            else:
                # if takeoff time is less (or equal), then free up one gate
                self.gatesFree += 1
                self.gatesOccupied -= 1
                t += 1

        # If anymore takeoffs are pending, then they wont affect the max total number of gates.

        # If any more landings are pending:
        while l < len(self.landingTimes):
            # Land all planes on runway
            self.landOnRunway(self.landingTimes[l])
            l += 1


        while self.planesOnRunway:
            # move all planes on runway to gates
            self.planesOnRunway.popleft()
            self.runwayToGate()

        return self.totalGates



def getMinGates(landingTimes, takeOffTimes, maxWaitTime, initialPlanes):
    solution = Solution(landingTimes, takeOffTimes, maxWaitTime, initialPlanes)
    return solution.getMinGates()
    
if __name__ == '__main__':