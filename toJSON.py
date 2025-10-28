import json 

print("this file is To store data")

total_study = {
    "sessions" : []
}

def sessionToJSON(session):
    duration = session.end_time - session.start_time
    
    total_study["sessions"].append(
        {"duration" : duration}
    )

def show():
    pass