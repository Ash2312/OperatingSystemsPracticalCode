# IMPLEMENTATION OF BANKERS ALGORITHM
P = 5
# Total Number of Resources 
R = 3
# Creating a function to find the need of each process 
def calculateNeed(need, maxm, allot):
    # calculating the need of each process P 
    for i in range(P):
        for j in range(R):            
            # Need of instance = Maximum Instance - Alloted Instance
            need[i][j] = maxm[i][j] - allot[i][j] 
# Function to find whether the system is in safe state or not 
def isSafe(processes, avail, maxm, allot):
    need = []
    for i in range(P):
        l = []
        for j in range(R):
            l.append(0)
        need.append(l)
    # Function to calculate the need matrix 
    calculateNeed(need, maxm, allot)
    # Marking all processes as finish 
    finish = [0] * P
    # Storing the safe sequence 
    safeSeq = [0] * P 
    # Making a copy of all the available resources 
    work = [0] * R 
    for i in range(R):
        work[i] = avail[i] 
    # When system is not in the safe state
    count = 0
    while (count < P):
        # Process which is not completed and whose 
        # needs can be completed with current 
        # available resources
        found = False
        for p in range(P): 
            # First seing if process is completed or not
            # if yes, then going to check the next condition
            # of whether its needs can be fulfilled with 
            # the current available resources or not
            if (finish[p] == 0):    
                # Check if for all resources 
                # of current P need is less 
                # than work
                for j in range(R):
                    if (need[p][j] > work[j]):
                        break      
                # If all needs of p were satisfied. 
                if (j == R - 1): 
                    # Add the allocated resources of 
                    # current P to the available/work 
                    # resources i.e.free the resources 
                    for k in range(R): 
                        work[k] += allot[p][k] 
                    # Add this process to safe sequence. 
                    safeSeq[count] = p
                    count += 1
                    # Mark this p as finished 
                    finish[p] = 1
                    found = True    
        # If we could not find a next process 
        # in safe sequence. 
        if (found == False):
            print("System is not in safe state")
            return False 
    # If system is in safe state then 
    # safe sequence will be as below 
    print("System is in safe state.",
              "\nSafe sequence is: ", end = " ")
    print(*safeSeq) 
    return True
# Driver code 
if __name__ =="__main__":   
    processes = [0, 1, 2, 3, 4]
    # Available instances of resources 
    avail = [3, 3, 2] 
    # Maximum R that can be allocated 
    # to processes 
    maxm = [[7, 5, 3], [3, 2, 2],
            [9, 0, 2], [2, 2, 2],
            [4, 3, 3]]
    # Resources allocated to processes 
    allot = [[0, 1, 0], [2, 0, 0],
             [3, 0, 2], [2, 1, 1],
             [0, 0, 2]] 
    # Check system is in safe state or not 
    isSafe(processes, avail, maxm, allot)
