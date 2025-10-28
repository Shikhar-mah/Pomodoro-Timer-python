import sessionInfo as si
import toJSON as tj
from datetime import datetime as dt

def main():
    print("Welcome to Pomodoro CLI")
    # print("Enter your choice: ")
    print("1. Start Timer")
    print("2. Stop Timer")
    print("3. Log Data")
    print("4. Exit the program")

    choice = int(input("\nEnter your choice: "))
    session = si.Session()
    match choice:
        case 1:
            startTimer(session)
        case 2:
            stopTimer(session)
        case 3:
            logData(session)
        case 4:
            exit(0)


def startTimer(session):
    print("The timer has started...")
    session.start_time = dt.now()
    # session.end_time = None 



def stopTimer(session):
    print("The timer has stopped") 
    session.end_time = dt.now()


def logData(session):
    try:
        tj.sessionToJSON(session)
    except:
        print("Some error occured while logging")
    else:
        print("The data has logged") 
        print(tj.show())

main()