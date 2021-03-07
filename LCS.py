#!/usr/bin/env python
# coding: utf-8

# In[74]:


def lcs(a,  b):
    #making the matrix global
    global matrix
    
    # generate matrix of length of longest common subsequence for substrings of both words
    matrix = [[0] * (len(a)) for r in range(len(b))]   
    
    #loop using enumerate function that accesses index and value 
    for i, x in enumerate(b):
        for j, y in enumerate(a):
            
            #if the basepair is same
            if x == y:
                
                #add +1 to one back diagonal 
                matrix[i][j] = matrix[i-1][j-1] + 1;
    
    #returning matrix            
    return lengths

#function for printing 
def print_lcs(a , b):
    #calling the lcs function
    lcs(a , b)
    print("sequences A = ", a)
    print("sequences A = ", b)
    
    #to print the sequences above matrix in aligned manner
    print("  " , end = "")
    print('  '.join(list(a)))
    
    #loop for prinitng each row in the matrix 
    for i in range(0 , len(b)):
        #print each letter of sequnece 2 along the matrix 
        print(b[i] , end = "")
        print(matrix[i])
    
    
seq1= 'AACTGGCAG'
seq2= 'TACGCTGGA' 

#calling the print_lcs function that calls lcs internally
print_lcs(seq1, seq2)


# In[ ]:




