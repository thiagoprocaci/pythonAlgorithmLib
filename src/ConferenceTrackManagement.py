# -*- coding: utf-8 -*-
from datetime import datetime

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
        print self.name, self.minutes
        for session in self.sessionList:
            print session.name, session.minutes            

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

    track1Morning = Track('track 1 morning', 60 * 3, True)
    track1Afternoon = Track('track 1 afternoon', 60 * 5, False)
    track2Morning = Track('track 2 morning', 60 * 3, True)
    track2Afternoon = Track('track 2 afternoon', 60 * 5, False)
    
    #Best-fit algorithm
    while sessionList:
        session = sessionList.pop()

        track1MorningRM = track1Morning.remainingMinutes() - session.minutes
        track1AfternoonRM = track1Afternoon.remainingMinutes() - session.minutes
        track2MorningRM = track2Morning.remainingMinutes() - session.minutes
        track2AfternoonRM = track2Afternoon.remainingMinutes() - session.minutes

        #print track1MorningRM

        if (track1AfternoonRM >= 0) and (track1AfternoonRM >= track1MorningRM) and (track1AfternoonRM >= track2MorningRM) and (track1AfternoonRM >= track2AfternoonRM):            
            track1Afternoon.sessionList.append(session)
            continue
        if (track2AfternoonRM >= 0) and (track2AfternoonRM >= track1AfternoonRM) and (track2AfternoonRM >= track1MorningRM) and (track2AfternoonRM >= track2MorningRM):            
            track2Afternoon.sessionList.append(session)
            continue

        if (track1MorningRM >= 0) and (track1MorningRM >= track1AfternoonRM) and (track1MorningRM >= track2MorningRM) and (track1MorningRM >= track2AfternoonRM):            
            track1Morning.sessionList.append(session)
            continue
        
        if (track2MorningRM >= 0) and (track2MorningRM >= track1AfternoonRM) and (track2MorningRM >= track1MorningRM) and (track2MorningRM >= track2AfternoonRM):            
            track2Morning.sessionList.append(session)
            continue

        print 'Problem!'
        

    track1Morning.printSessions()
    track1Afternoon.printSessions()
    track2Morning.printSessions()
    track2Afternoon.printSessions()
















        









    





if __name__ == '__main__':
    main()