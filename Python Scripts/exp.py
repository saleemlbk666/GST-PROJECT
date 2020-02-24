import xlwt 
import random
import rstr
import string
import array as arr
from xlwt import Workbook 

wb = Workbook() 

sheet1 = wb.add_sheet('Sheet 1') 
row = 0  
column = 0  
    
content = ["Export Type","Invoice Number","Invoice Date","Invoice Value","Port Code","Shipping Bill Number","Shipping Bill Date","Applicable % of Tax Rate","Rate","Taxable Value","Cess amount"]   
    
# iterating through the content list   
for item in content :   
    
    # write operation perform   
    sheet1.write(row, column, item)   
    
    # incrementing the value of row by one with each iterations.   
    column += 1  

#export type
for i in range(100):
	etype=random.choice(["WPAY","WOPAY"])
	sheet1.write(i+1,0,etype)


#invoice number
#def string_num(size):
#    chars=string.ascii_uppercase+string.digits
 #   return ''.join(random.choice(chars) for _ in range(size))			
for i in range(1001,1101):
  sheet1.write(i-1000,1,'S-'+str(i))


#invoice date && Shipping bill date
for i in range(100):
  s1=random.choice(range(1,28))
  s2="-"
  s3=random.choice(["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"])
  s4=random.choice(range(17,20))
  str1=str(s1)+s2+s3+s2+str(s4)
  s5=s1+1
  str2=str(s5)+s2+s3+str(s4)
  sheet1.write(i+1,2,str1)
  sheet1.write(i+1,6,str2)


#invoice value && taxable value
for i in range(100):
  invoice_value=random.randint(40000,60000)
  sheet1.write(i+1,3,invoice_value)
  taxable_value=random.randint(20000,invoice_value)
  sheet1.write(i+1,9,taxable_value)

#port code
for i in range(100):
	code="INB99"+str(random.choice(range(0,10)))
	sheet1.write(i+1,4,code)

#Shipping bill number
for i in range(100):
	number=random.choice(range(184200,184400))
	sheet1.write(i+1,5,number)

#Applicable % of Tax Rate
for i in range(100):
	sheet1.write(i+1,7,50) 


#Rate
for i in range(100):
	rate=random.choice([0,3,5,12,18,28])
	sheet1.write(i+1,8,rate)


#cess
i=1
while i<100:
  cess=random.choice(range(500,1000))  
  sheet1.write(i+1,10,cess)
  i+=10



wb.save('GST1exp.xlsx')


