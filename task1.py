import sys
from datetime import *

def run(a):
    totalStart = datetime.now()
    start = datetime.now()
    
    file = open(a,"r")    
    file.readline() #ignore the table headings
    lines = file.readlines()    #fetch the remaining data as a list

    end = datetime.now()

    answerFile = open("task1_answers-sample_simple_ebola_data.txt","w")
    runtimeFile = open("task1_times-sample_simple_ebola_data.txt","w")

    print("File-reading and pre-processing time is", (end - start).total_seconds() * 1000, "milliseconds" ,file = runtimeFile)

    start = datetime.now()
    count = 0   

    myListDates = []    # will be later used to find the peak dates for deaths
    myListNum = []      # keeps death rates. will be later used to find the peak death rates

    myListDates2 = []   # will be later used to find the peak dates for cases or infections
    myListNum2 = []     # keeps death rates. will be later used to find the peak infection rates

    prevDeath = 0       # keeps the previous cumulative deaths. It will be used in the calculation of death rates
    prevCase = 0        # keeps the previous cumulative cases. It will be used in the calculation of infection rates

    prevDateDeath = date(MINYEAR, 1, 1)     # will be used to find the last death date
    prevDateCase = date(MINYEAR, 1, 1)      # will be used to find the last case date

    prevD = date(MINYEAR, 1, 1)     # keeps track of the previous death date
    prevC = date(MINYEAR, 1, 1)     # keeps track of the previous case date

    maxDeath = 0    # keeps track of the highest death rate
    maxCase = 0     # keeps track of the highest infection rate

    deathRate = 0   # starting value for death rate
    infectionRate = 0   # starting value for infection rate

    maxDeathPrevDate = None     # keeps track of the previous date of the highest death rate
    maxDeathCurDate = None      # keeps track of the current date of the highest death rate

    maxCasePrevDate = None      # keeps track of the previous date of the highest infection rate
    maxCaseCurDate = None       # keeps track of the current date of the highest infection rate

    for i in range(0,len(lines)):
        line = lines[i]
        c, l, cum, dat, val = line.split(",")   # c is the country, l is locality, date is date, cum is indicator and val is the cumulative indicator
        y, m, d = int(dat.split("/")[2]), int(dat.split("/")[1]), int(dat.split("/")[0])    # split the date into year month and day
        if cum == 'cumulative_deaths':      #if the indicator is a cumulative death
            curDateDeath = date(y, m, d)    # current death date = formatted date   
            if count == 0:
                prevDeath = int(val)
            else:
                deathRate = (int(val) - prevDeath)/ (curDateDeath - prevD).days     #calculate the death rate as the current cumulative deaths  - the previous cumulative deaths all divided by the number of days between the current date and the previous date a death was recorded 
                if deathRate > maxDeath: 
                    maxDeath = deathRate    # if the current death rate > than the previous highest, set the current death rate as the highest so far
                    maxDeathPrevDate = prevD    # change the previous death date as the previous date for the highest death rate
                    maxDeathCurDate = curDateDeath  # set the current date as the date for the highest death rate
            if curDateDeath > prevDateDeath and deathRate > 0:
                prevDateDeath = curDateDeath    # if the current date is higher than the previous death date and a death was recorded, then set the last day a death was recorded to the current date

            
            prevD = curDateDeath    #previous death date is set to the current date
            myListDates.append(str(curDateDeath.strftime('%d/%m/%Y')))
            myListNum.append(deathRate)
            prevDeath = int(val)
            
        else:
            curDateCase = date(y, m, d)        
            
            if count == 0:
                prevCase = int(val)
            else:
                infectionRate = (int(val) - prevCase)/ (curDateCase - prevC).days
                if infectionRate > maxCase:
                    maxCase = infectionRate
                    maxCasePrevDate = prevC
                    maxCaseCurDate = curDateCase
            if curDateCase > prevDateCase and infectionRate > 0:
                prevDateCase = curDateCase

            
            prevC = curDateCase
            myListDates2.append(str(curDateCase.strftime('%d/%m/%Y')))
            myListNum2.append(infectionRate)
            prevCase = int(val)
        count += 1
    #files.close()                   
    print("The last death was recorded on", str(prevDateDeath.strftime('%d/%m/%Y')), file = answerFile)
    end = datetime.now()
    print("Time to complete a is", (end - start).total_seconds() * 1000, "milliseconds" ,file = runtimeFile)
    start = datetime.now()
    
    print("The last case was recorded on", str(prevDateCase.strftime('%d/%m/%Y')), file = answerFile)
    end = datetime.now()
    print("Time to complete b is", (end - start).total_seconds() * 1000, "milliseconds" ,file = runtimeFile)
    start = datetime.now()
    
    print("The country can be declared Ebola-free on", str((prevDateCase + timedelta(days=42)).strftime('%d/%m/%Y')), file = answerFile)
    end = datetime.now()
    print("Time to complete c is", (end - start).total_seconds() * 1000, "milliseconds" ,file = runtimeFile)
    start = datetime.now()
    
    print("The highest death rate was", maxDeath, "which happened between", maxDeathPrevDate.strftime('%d/%m/%Y'), "and", maxDeathCurDate.strftime('%d/%m/%Y'), file = answerFile)
    end = datetime.now()
    print("Time to complete d is", (end - start).total_seconds() * 1000, "milliseconds" ,file = runtimeFile)
    start = datetime.now()
    
    print("The highest infection rate was", maxCase, "which happened between", maxCasePrevDate.strftime('%d/%m/%Y'), "and", maxCaseCurDate.strftime('%d/%m/%Y'), file = answerFile)
    end = datetime.now()
    print("Time to complete e is", (end - start).total_seconds() * 1000, "milliseconds" ,file = runtimeFile)

    start = datetime.now()
    
    deathMaxLocal = 0
    print("The death peaks happened on the following dates: ", end="", file = answerFile)
    for i in range(1, len(myListNum)-1):
      if((myListNum[i] > myListNum[i-1]) and (myListNum[i] > myListNum[i+1])):
        deathMaxLocal += 1
        print(myListDates[i], end=" ", file = answerFile)
    print(". There are", deathMaxLocal, "death peaks", file = answerFile)
    end = datetime.now()
    print("Time to complete g is", (end - start).total_seconds() * 1000, "milliseconds" ,file = runtimeFile)

    start = datetime.now()
    print("The infection peaks happened on the following dates: ", end="", file = answerFile)
    caseMaxLocal = 0
    for i in range(1, len(myListNum2)-1):
      if((myListNum2[i] > myListNum2[i-1]) and (myListNum2[i] > myListNum2[i+1])):
        caseMaxLocal += 1
        print(myListDates2[i],end=" ", file = answerFile)
    print(". There are", caseMaxLocal, "infection peaks", file = answerFile)
    end = datetime.now()
    print("Time to complete f is", (end - start).total_seconds() * 1000, "milliseconds" ,file = runtimeFile)

    totalEnd = datetime.now()

    print("Overall runtime is", (totalEnd - totalStart).total_seconds() * 1000, "milliseconds" ,file = runtimeFile)
    file.close()
    runtimeFile.close()
    answerFile.close()
if __name__ == "__main__":
    a = sys.argv[1]
    run(a)
