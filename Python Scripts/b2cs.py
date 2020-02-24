import xlwt 
import random
import string
import rstr
import array as arr
from xlwt import Workbook 

wb = Workbook() 

sheet1 = wb.add_sheet('Sheet 1',cell_overwrite_ok=True) 
row = 0  
column = 0  
    
content = ["Type","place of supply","Rate","Applicable % of Tax Rate","Taxable Value","Cess amount","E-Commerce GSTIN"]   
    
# iterating through the content list   
for item in content :   
    
    # write operation perform   
    sheet1.write(row, column, item)   
    
    # incrementing the value of row by one with each iterations.   
    column += 1  


#Invoice Type
for i in range(100):
	invoice_type=random.choice(["E","OE"])
	sheet1.write(i+1,0,invoice_type)

#Place of supply
for i in range(100):
  states=random.choice(["1-JAMMU AND KASHMIR","2-HIMACHAL PRADESH","3-PUNJAB","4-CHANDIGARH","5-UTTARAKHAND","6-HARYANA"
"7-DELHI","8-RAJASTHAN","9-UTTAR PRADESH","10-BIHAR","11-SIKKIM","12-ARUNACHAL PRADESH","13-NAGALAND","14-MANIPUR","15-MIZORAM","16-TRIPURA","17-MEGHLAYA","18-ASSAM","19-WEST BENGAL","20-JHARKHAND","21-ODISHA","22-CHATTISGARH","23-MADHYA PRADESH","24-GUJARAT","25-DAMAN AND DIU","26-DADRA AND NAGAR HAVELI","27-MAHARASHTRA","28-ANDHRA PRADESH (old)","29-KARNATAKA","30-GOA","31-LAKSHWADEEP","32-KERALA","33-TAMIL NADU","34-PUDUCHERRY","35-ANDAMAN AND NICOBAR ISLANDS","36-TELANGANA","37-ANDHRA PRADESH"])
  sheet1.write(i+1,1,states)

# Rate as per invoice
for i in range(100):
	rate=random.choice([5,28,12])
	sheet1.write(i+1,2,rate)


#Applicable % of Tax Rate
for i in range(100):
	sheet1.write(i+1,3,50)


#Taxable value
for i in range(100):
  taxable_value=random.randint(50000,360000)
  sheet1.write(i+1,4,taxable_value)


#cess
i=1
while i<100:
  cess=random.choice(range(500,1000))  
  sheet1.write(i+1,5,cess)
  i+=10


#E-commerse GSTIN
i=1
while i<100:
  gstin=rstr.xeger(r'[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[1-9A-Z]{1}[Z]{1}[0-9A-Z]{1}')
  sheet1.write(i+1,6,gstin)
  i+=15

wb.save('B2CS.xlsx')


