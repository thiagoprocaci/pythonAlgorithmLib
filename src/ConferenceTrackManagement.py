# -*- coding: utf-8 -*-
from datetime import datetime, timedelta


class Session:
    name, minutes = None, None

    def __init__(self, name, minutes):
        self.name = name
        self.minutes = minutes

class Track:
    minutes, name, sessionList, morning = None, None, None, None

    def __init__(self, name, minutes, morning = True):
        self.name = name
        self.minutes = minutes
        self.sessionList = []
        self.morning = morning

    def remainingMinutes(self):
        sumMin = 0
        for session in self.sessionList:
            sumMin = sumMin + session.minutes
        return self.minutes - sumMin

    def printSessions(self):  
        date = datetime.now()
        if self.morning:           
            newDate = date.replace(hour=9, minute=0, second=0)
        else:
            newDate = date.replace(hour=13, minute=0, second=0)
        print self.name
        for session in self.sessionList:
            print format(newDate, '%H:%M'), session.name, session.minutes, 'min' 
            newDate =newDate + timedelta(minutes=session.minutes)          

        print '-----------------------------------'




def main():
    sessionList = []

    
    sessionList.append(Session('Rails for Python Developers lightning', 60))
    sessionList.append(Session('Writing Fast Tests Against Enterprise Rails', 60))
    sessionList.append(Session('Overdoing it in Python', 45))
    sessionList.append(Session('Lua for the Masses', 30))
    sessionList.append(Session('Ruby Errors from Mismatched Gem Versions', 45))
    sessionList.append(Session('Common Ruby Errors', 45))
    sessionList.append(Session('Communicating Over Distance', 60))
    sessionList.append(Session('Accounting-Driven Development', 45))
    sessionList.append(Session('Woah', 30))
    sessionList.append(Session('Sit Down and Write', 30))
    sessionList.append(Session('Pair Programming vs Noise', 45))
    sessionList.append(Session('Rails Magic', 60))
    sessionList.append(Session('Ruby on Rails: Why We Should Move On', 60))
    sessionList.append(Session('Clojure Ate Scala (on my project)', 45))
    sessionList.append(Session('Programming in the Boondocks of Seattle', 30))
    sessionList.append(Session('Ruby vs. Clojure for Back-End Development', 30))
    sessionList.append(Session('Ruby on Rails Legacy App Maintenance', 60))
    sessionList.append(Session('A World Without HackerNews', 30))
    sessionList.append(Session('User Interface CSS in Rails Apps', 30))

    sessionList.sort(key = lambda x: x.minutes, reverse = False)

    track1Morning = Track('Track 1 morning', 60 * 3, True)
    track1Afternoon = Track('Track 1 afternoon', 60 * 4, False)
    track2Morning = Track('Track 2 morning', 60 * 3, True)
    track2Afternoon = Track('Track 2 afternoon', 60 * 4, False)
    
    #Best-fit algorithm
    while sessionList:
        session = sessionList.pop()

        track1MorningRM = track1Morning.remainingMinutes() - session.minutes
        track1AfternoonRM = track1Afternoon.remainingMinutes() - session.minutes
        track2MorningRM = track2Morning.remainingMinutes() - session.minutes
        track2AfternoonRM = track2Afternoon.remainingMinutes() - session.minutes

        avaliableTrackDict = {}

        if track1MorningRM < 0:
            track1MorningRM = None
        else:
            avaliableTrackDict[track1Morning.name] = track1MorningRM

        if track1AfternoonRM < 0:
            track1AfternoonRM = None
        else:
            avaliableTrackDict[track1Afternoon.name] = track1AfternoonRM

        if track2MorningRM < 0:
            track2MorningRM = None
        else:
            avaliableTrackDict[track2Morning.name] = track2MorningRM

        if track2AfternoonRM < 0:
            track2AfternoonRM = None
        else:
            avaliableTrackDict[track2Afternoon.name] = track2AfternoonRM

        
        smallestGap = None
        selectTrackName = None
        for key in avaliableTrackDict:
            remainingMin = avaliableTrackDict[key]
            if (smallestGap is None) or (smallestGap > remainingMin):
                smallestGap = remainingMin
                selectTrackName = key

        if selectTrackName == track1Morning.name:
            track1Morning.sessionList.append(session)
            continue

        if selectTrackName == track1Afternoon.name:
            track1Afternoon.sessionList.append(session)
            continue

        if selectTrackName == track2Morning.name:
            track2Morning.sessionList.append(session)
            continue

        if selectTrackName == track2Afternoon.name:
            track2Afternoon.sessionList.append(session)
            continue



        print 'Problem!'
        

    track1Morning.printSessions()
    track1Afternoon.printSessions()
    track2Morning.printSessions()
    track2Afternoon.printSessions()
















        









    





if __name__ == '__main__':
    main()