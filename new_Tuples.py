#1
     
N_list=[2,3,4,5,15,1,43,20]
print(N_list)
def element_sum(list):  
    return sum(list)
to_sum=element_sum(N_list)
print("sum:",to_sum)
    

#2
def find_largrst(list):
    return max (list)
largrst_num=find_largrst(N_list)
print("the largrst number: ", largrst_num)
#3
odd_numbers=[num for num in range(1200,2001,125)if num % 2!=0]
print(odd_numbers)
#4
new_list=odd_numbers[:5]
print(new_list)