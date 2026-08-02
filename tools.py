import random as r

#Function to Generate Ticket Numbers based on the Type Of Issue Raised
# Access,Network,Hardware,General
def Tic_Gen(Issue_Type):
    try:    
        if Issue_Type == "access":
            return str("ACC"+str(r.randrange(50000,99999)))
        elif Issue_Type == "request":
            return str("REQ"+str(r.randrange(50000,99999)))
        elif Issue_Type == "hardware":
            return str("HRD"+str(r.randrange(50000,99999)))
        elif Issue_Type == "general":
            return str("GEN"+str(r.randrange(50000,99999)))
    except ValueError():
        print("Invalid Data Detected, Enter Correct Data")