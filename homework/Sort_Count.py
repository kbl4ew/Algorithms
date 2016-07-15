
df = np.loadtxt('input.txt')
df = df.tolist()
alist = [54,26,93,17,77,31,44,55,20]

def sort_Count(in_array):
    '''
    Input: an array of integers
    Output: number of inversions in the array
    Descriptions:
    We use the merge_sort algorithm as the backbone and implement a divide
    and conquer algorithm for the inversion count algorithm
    '''
    n = len(in_array)
    # Base Case
    if(n == 1):
        return(0)
    if len(in_array) > 1:
        # Determine the midpoint
        mid = len(in_array)//2 
        left_array = in_array[:mid]
        right_array = in_array[mid:]
        X = sort_Count(left_array)
        Y = sort_Count(right_array)
    
        # Initializing the number of split inversions
        Z = 0 
        # parameters
        i = 0 # Counter for elements in the left array
        j = 0 # Counter for elements in the right array
        k = 0 # Counter for the sorted array
        #size = len(left_sorted) + len(right_sorted)
        #sorted_array = np.empty(size, dtype = int) # Initializing the sorted array
        #print('Merging', left_array, ' and ', right_array)
        # Case 1
        while((i < len(left_array)) and (j < len(right_array))):
            if(left_array[i] <= right_array[j]):
                in_array[k] = left_array[i]
                i = i + 1
                #k = k + 1
            else:
                in_array[k] = right_array[j]
                j = j + 1
                Z = Z + (mid - i)
                #k = k + 1
            k = k + 1
        # Case 2
        while(i < len(left_array)):
            in_array[k] = left_array[i]
            i = i + 1
            k = k + 1
        
        # Case 3
        while(j < len(right_array)):
            in_array[k] = right_array[j]
            j = j + 1
            k = k + 1
    elif (len(in_array) == 1):
        return
    else:
        print('length is 0')
        #return
    
    tot_inv = X + Y + Z
    return(tot_inv)

sort_Count(df)