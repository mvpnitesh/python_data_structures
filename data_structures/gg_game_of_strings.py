from queue import PriorityQueue
 
MAX_CHAR = 26
 
# Main Function to calculate min sum of
# sauares of characters after k removals
def minStringValue(str, k):
    l = len(str) # find length of string
 
    # if K is greater than length of string
    # so reduced string will become 0
    if(k >= l):
        return 0
     
    # Else find Freauency of each
    # character and store in an array
    frequency = [0] * MAX_CHAR
    for i in range(0, l):
        frequency[ord(str[i]) - 97] += 1
    import pdb;pdb.set_trace()
    # Push each char freauency negative
    # into a priority_aueue as the aueue
    # by default is minheap
    a = PriorityQueue()
    for i in range(0, MAX_CHAR):
        a.put(-frequency[i])
    import pdb;pdb.set_trace()
    # Removal of K characters
    while(k > 0):
         
        # Get top element in priority_aueue
        # multiply it by -1 as temp is negative
        # remove it. Increment by 1 and again
        # push into priority_aueue
        temp = a.get()
        temp = temp + 1
        a.put(temp, temp)
        k = k - 1
    import pdb;pdb.set_trace()
    # After removal of K characters find
    # sum of sauares of string Value    
    result = 0; # initialize result
    while not a.empty():
        temp = a.get()
        temp = temp * (-1)
        result += temp * temp
    return result
 
# Driver Code
if __name__ == "__main__":
    str = "fxnsmkasmlerxxoxhfwviluzttaaotdwrsafcsxrddicaxahewemjyleudukxzgarzvvrtmvwvxzuxiyvnngna"
    k = 21
    print(minStringValue(str, k))