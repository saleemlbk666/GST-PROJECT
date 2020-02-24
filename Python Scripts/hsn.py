import xlwt 
import random
import string
import rstr
import array as arr
from xlwt import Workbook 

wb = Workbook() 

sheet1 = wb.add_sheet('Sheet 1') 
row = 0  
column = 0  
    
content = ["HSN", "Description", "UQC","Total Quantity","Total Value","Taxable Value","Integrated Tax Amount","Central Tax Amount","State/UT Tax Amount","Cess amount"]   

# iterating through the content list   
for item in content :   
    
    # write operation perform   
    sheet1.write(row, column, item)   
    
    # incrementing the value of row by one with each iterations.   
    column += 1  

#HSN-0
for i in range(100):
  hsn=random.choice(range(1001,3456721))
  sheet1.write(i+1,0,hsn)

#Description-1
for i in range(100):
	desc=random.choice(["Copper","Cashew","Fabric","Biscuit","Aerated Drinks"])
	sheet1.write(i+1,1,desc)

#UQC-2
for i in range(100):
	desc=random.choice(["BAG-BAGS","BAL-BALE","NOS-NUMBERS","BDL-BUNDLES","CAN-CANS"])
	sheet1.write(i+1,2,desc)

#Total Quantity-3
for i in range(100):
	quantity=rstr.xeger(r'[0-9]{1}\.[0-9]{2}')
	sheet1.write(i+1,3,quantity)

#Total Value-4
for i in range(100):
	value=rstr.xeger(r'[0-9]{5}\.[0-9]{2}')
	sheet1.write(i+1,4,value)

#Taxable Value-5
for i in range(100):
	taxvalue=rstr.xeger(r'[0-9]{2}\.[0-9]{2}')
	sheet1.write(i+1,5,taxvalue)

#Integrated Tax Amount-6
for i in range(100):
	itax=rstr.xeger(r'[0-9]{3}\.[0-9]{2}')
	sheet1.write(i+1,6,itax)

#Central Tax Amount-7
for i in range(100):
	ctax=rstr.xeger(r'[0-9]{3}\.[0-9]{2}')
	sheet1.write(i+1,7,ctax)

#State/UT Tax Amount-8
for i in range(100):
	stax=rstr.xeger(r'[0-9]{3}\.[0-9]{2}')
	sheet1.write(i+1,8,stax)

#Cess amount-9
for i in range(100):
	cess=rstr.xeger(r'[0-9]{3}\.[0-9]{2}')
	sheet1.write(i+1,9,cess)


wb.save('hsn.xlsx')
