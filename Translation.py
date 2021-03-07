#the file contains the standard genetic code for translation. File also enclosed on blackboard with the HW. 
codes = open('gen_code.txt')
genetic_code = codes.readlines()
codes.close();

#store codons and respective amino acid in dictionary
code ={}

#in the genetic code file, the first codon-amino acid pair start from 9th position
for i in  range(9,len(genetic_code[0])): 
    
    #the first line(0th) contains the amino acid single letter codes
    aa= genetic_code[0][i];  
    
    #the next 3, 4, and 5th line has the nucleotides 
    codon = genetic_code[2][i] + genetic_code[3][i] + genetic_code[4][i];   
    
    #the keys are triplet codons and values are amino acids
    code[codon] = aa;
    
    #the file with the fasta sequence and the sequence header
data = open("genes.txt")
mydata = data.readlines()
data.close()
temp_header = ''
#to store each fasta seq + header in dictionary. If you have more than 1 fasta seq in a single file
seq_dict = {}

for i in mydata:
    #heading line for each sequence
    if i.startswith('>'):
        
        #store header line
        temp_header = i
        #empty the dictionary everytime 
        seq_dict[i] = ''
    else:
        #if sequnece, add sequence as value to each header key
        seq_dict[temp_header] = seq_dict[temp_header] + i
        
#for each key(header line) of the file/dictionary
for x in seq_dict.keys():
    
    #myseq stores the fasta mRNA sequence for each header
    myseq = seq_dict[temp_header];
    
    #amino acid sequence
    aaseq="";
    
    #for calculating the triplet positionss for each new mRNA sequence 
    pos = 0;
    
    while (pos < len(myseq) -2):
        
        #tempcodon stores the triplet mRNA nucleotides 
        tempcodon = myseq[pos] + myseq[pos+1] + myseq[pos+2];
        
        #if the triplet codon is there in the amino acid dictionary's key
        if(tempcodon in code.keys()):
            
            #aaseq keeps adding the single letter code of tempcodon of the triplet codon
            aaseq = aaseq + code[tempcodon];
        
        #the position increased by 3. frameshift by 3
        pos = pos + 3;
    #print the header with it amino acid seq
    print(temp_header + "\n " + aaseq)
    
    
    
#we can also write the output into a new file using the write() function by opening the new file in writing mode. 
