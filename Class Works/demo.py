# 
print("\n bolla abhinov".upper()) # BOLLA ABHINOV
print("\n BOLLA ABHINOV".lower()) #bolla abhinov
print("\n bolla abhinov\n".title()) #Bolla Abhinov
print("abhinov bolla".capitalize()) #Abhinov bolla
print("\n abhinov\n\n".swapcase()) #ABHINOV

#Alignment & Formatting Methods
#center(width,fillchar)
#ljust(width,fillchar)
#rjust(width,fillchar)
#zfill(width)'''

s="Bolla Abhinov"
print(s.center(30,'*')) #********Bolla Abhinov*********
print(s.ljust(30,'+')) #Bolla Abhinov+++++++++++++++++
print(s.rjust(30,'-')) #-----------------Bolla Abhinov
print('215'.zfill(10)) #0000000215
print('abc'.zfill(10)) #0000000abc


#Search & Find Method
#find(sub)
#rfind(sub)
#index(sub)
#rindex(sub)
#count(sub)

n="python full stack programming"
print(n.find('f')) #7
print(n.rfind('s')) #12
print(n.index('u')) #8
print(n.rindex('p')) #18
print(n.count('p')) #2
print(n.find('z')) #-1

#*****print(n.index('z')) #  print(s.index('z')) ValueError: substring not found*****
#------------------------------------------------------#


#Replace & Modify Methods
#replace(old,new)
#translate(table)
#maketrans()

m=""


