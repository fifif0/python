#6.4.1.6
'''
numbers = {
    '0':('###','# #','# #','# #','###'),
    '1':(' ##','###',' ##',' ##',' ##'),
    '2':('###','  #','###','#  ','###'),
    '3':('###','  #','###','  #','###'),
    '4':('# #','# #','###','  #','  #'),
    '5':('###','#  ','###','  #','###'),
    '6':('###','#  ','###','# #','###'),
    '7':('###','  #','  #','  #','  #'),
    '8':('###','# #','###','# #','###'),
    '9':('###','# #','###','  #','###')
}

num=int(input("Podaj liczbe:"))
num=str(num)

for line in range(len(numbers['0'])):
    print(' '.join(numbers[i][line] for i in num))

'''
digital=['1111110', #0
        '0110000', #1
        '1101101', #2
        '1111001', #3
        '0110011', #4
        '1011011', #5
        '1011111', #6
        '1110000', #7
        '1111111', #8
        '1111011', #9
        ]
        
def print_number(num):
    num=str(num)
    lines=['' for lin in range(5)]
    for d in num:
        seq=[ [' ',' ',' '] for lin in range(5)]
        ptrn=digital[ord(d) - ord('0')]
        if ptrn[0]=='1':
            seq[0][0]=seq[0][1]=seq[0][2]='#'
        if ptrn[1]=='1':
            seq[0][2]=seq[1][2]=seq[2][2]='#'
        if ptrn[2]=='1':
            seq[2][2]=seq[3][2]=seq[4][2]='#'
        if ptrn[3]=='1':
            seq[4][0]=seq[4][1]=seq[4][2]='#'
        if ptrn[4]=='1':
            seq[2][0]=seq[3][0]=seq[4][0]='#'
        if ptrn[5]=='1':
            seq[0][0]=seq[1][0]=seq[2][0]='#'
        if ptrn[6]=='1':
            seq[2][0]=seq[2][1]=seq[2][2]='#'
        for lin in range(5):
            lines[lin]+=''.join(seq[lin]) + ' '
    for lin in lines:
        print(lin)
        
        
print_number(int(input("Enter the number:")))


