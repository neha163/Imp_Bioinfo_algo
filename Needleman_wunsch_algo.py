#!/usr/bin/env python
# coding: utf-8

# In[21]:


# module to create matrix 
import numpy as np

#assigning sequences 
seq1= 'ATCGATCG'
seq2= 'AGCTAG'

#scoring scheme declared as global variables 
match = +1;
mis_match = 0;
gap_penalty = -1

#matrix of length of both the sequences +1 (row and column each) to accomodate the gap penatly
#as global variable so that can be used by all functions 
boxes= np.zeros((len(seq2) + 1, len(seq1) +1))
         


# In[22]:


'''calculate the score for each base pair of the 2 sequences '''

#dot plot incorporated from problem 3.2 
def dotcounter(seq1,seq2):
    count=0;
    for i in range(len(seq1)):
        for j in range(len(seq2)):
            if seq1[i] == seq2[j]:
                print('seq1 bp', i+1, 'matches with', 'seq2 bp ', j+1)
                count += 1;
    print("total matches are =", count)


# function created for calcualting the score by passing 2 argumments 
def score(bp1, bp2):
    if bp1 == bp2:
        return match;
    elif bp1 == '-' or bp2 == '-':
        return gap_penalty
    else:
        return mis_match


'''actual Needleman Wunsch alginment goes here'''


def global_alignment_matrix(seq1, seq2):
    dotcounter(seq1, seq2)
    
    #these variables stores the len of sequences that will be used to execute the for loop 
    num_cols = len(seq1)
    num_rows = len(seq2)
     
    # assiging values to the first row with -1, -2 etc.
    for i in range(0, num_cols +1 ):
        boxes[0][i] = gap_penalty * i;
    
    #assiging values to first column with -1, -2 etc
    for j in range(0, num_rows + 1 ):
        boxes[j][0] = gap_penalty * j;
    
    #nested for loop to access each element of the matrix 
    for row in range(1, num_rows + 1):
        for col in range(1, num_cols + 1):
            
            #
            diagonal= boxes [ row-1 ][ col-1 ] + score( seq1[ col-1 ], seq2 [ row-1 ])
            delete = boxes[ row - 1][col] + gap_penalty
            insert = boxes[row][col - 1] + gap_penalty
            
            # Record the maximum score from the three possible scores calculated above
            boxes[row][col] = max(diagonal, delete, insert)
    
    
    '''tracing back by checking the value of the current cell matches with the diagonal, up or left of the cell'''
    # 2 empty strings 
    alignment_1 = ''
    alignment_2 = ''
    
    #for the last cell of the matrix 
    back_i = len(seq2)
    back_j = len(seq1)
    
    #loop till the pointer reaches the first row first column cell
    while back_i > 0 and back_j > 0:
        
        #variblaes for position/coordinates of current, diagonla, up and left cells
        current_box = boxes [back_i] [back_j];
        diagonal_box = boxes [back_i -1] [back_j-1]
        up_box = boxes[back_i] [ back_j -1]
        left_box = boxes[back_i -1] [back_j]
        
        #check if current cell score matches the diagonal score. if yes, add the base pair to empty string 
        if current_box == diagonal_box + score( seq1[ back_j-1 ], seq2 [ back_i-1 ]):
            alignment_1 += seq1[back_j-1]
            alignment_2 += seq2[back_i-1]
            
            #one less of each column and row
            back_i -= 1
            back_j -= 1
        
        #check if current box score matches up cell + (-1) 
        elif current_box == up_box + gap_penalty:
            alignment_1 += seq1[back_j-1]
            alignment_2 += '-'
            back_j -= 1 # move to one column left keeping row same 
            
        #check if current box score matches left cell + (-1)
        elif current_box == left_box + gap_penalty:
            alignment_1 += '-'
            alignment_2 += seq2[back_i -1]
            back_i -=1; # moving one row above keeping column same 
            
    
    # as we had base pairs added back by tracing back, we got to print the reverse of the sequneces 
    alignment_1 = alignment_1[::-1]
    alignment_2 = alignment_2[::-1]
    
    return(alignment_1, alignment_2)

#creating objects by calling the function and passing the arguments 
align_sequence1, align_sequence2 = global_alignment_matrix(seq1, seq2)

#print in different lines
print("Optimal alignment with Needleman Wunsch Algorithm is shown below: ")
print(align_sequence1 + "\n" + align_sequence2)


# In[ ]:




