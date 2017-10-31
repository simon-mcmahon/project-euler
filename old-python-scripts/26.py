import math as m
def frac_exp(b,n): #(1/b) n digits
    rem_list=[]
    num=1
    exp='0.'
    for x in range(0,n):

        #get number greater than b

        while num<b:
            num=(str(num)+'0')
        digit=int(m.floor(int(num)/b))
        rem=int(num)-b*digit
        rem_list+=[rem]
        exp+=str(digit) #decimal expansion
        if (rem==0) or ((rem_list.count(rem))>1): #mod repeats when a repeating decimal comes up
            return len(rem_list)-1
        
        num=rem
    return len(rem_list)-1

term_length=map(lambda x: frac_exp(x,2000),range(1,1001))
print term_length.index(max(term_length))+1
