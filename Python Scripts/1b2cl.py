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
    
content = ["Invoice Number","Invoice Date","Invoice Value","place of supply","Applicable % of Tax Rate","Rate","Taxable Value","Cess amount","E-Commerce GSTIN","Supplies covered under section 7 of IGST Act"]   
    
# iterating through the content list   
for item in content :   
    
    # write operation perform   
    sheet1.write(row, column, item)   
    
    # incrementing the value of row by one with each iterations.   
    column += 1  

#invoice number
#def string_num(size):
#    chars=string.ascii_uppercase+string.digits
 #   return ''.join(random.choice(chars) for _ in range(size))			
for i in range(1001,1101):
  sheet1.write(i-1000,0,'S-'+str(i))


#invoice date
for i in range(100):
  s1=random.choice(range(1,28))
  s2="-"
  s3=random.choice(["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"])
  s4=random.choice(range(17,20))
  str1=str(s1)+s2+s3+s2+str(s4)
  sheet1.write(i+1,1,str1)


#invoice value && taxable value
for i in range(100):
  invoice_value=random.randint(40000,60000)
  sheet1.write(i+1,2,invoice_value)
  taxable_value=random.randint(20000,invoice_value)
  sheet1.write(i+1,6,taxable_value)


#Place of supply
for i in range(100):
	states=random.choice(["1-JAMMU AND KASHMIR","2-HIMACHAL PRADESH","3-PUNJAB","4-CHANDIGARH","5-UTTARAKHAND","6-HARYANA"
"7-DELHI","8-RAJASTHAN","9-UTTAR PRADESH","10-BIHAR","11-SIKKIM","12-ARUNACHAL PRADESH","13-NAGALAND","14-MANIPUR","15-MIZORAM","16-TRIPURA","17-MEGHLAYA","18-ASSAM","19-WEST BENGAL","20-JHARKHAND","21-ODISHA","22-CHATTISGARH","23-MADHYA PRADESH","24-GUJARAT","25-DAMAN AND DIU","26-DADRA AND NAGAR HAVELI","27-MAHARASHTRA","28-ANDHRA PRADESH (old)","29-KARNATAKA","30-GOA","31-LAKSHWADEEP","32-KERALA","33-TAMIL NADU","34-PUDUCHERRY","35-ANDAMAN AND NICOBAR ISLANDS","36-TELANGANA","37-ANDHRA PRADESH"])
	sheet1.write(i+1,3,states)

#Applicable % of Tax Rate
for i in range(100):
	sheet1.write(i+1,4,50) 


#Rate
for i in range(100):
	rate=random.choice([0,3,5,12,18,28])
	sheet1.write(i+1,5,rate)


#cess
i=1
while i<100:
  cess=random.choice(range(500,1000))  
  sheet1.write(i+1,7,cess)
  i+=10

#E-commerse GSTIN
i=1
while i<100:
  gstin=rstr.xeger(r'[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[1-9A-Z]{1}[Z]{1}[0-9A-Z]{1}')
  sheet1.write(i+1,8,gstin)
  i+=15

 
#Supplies covered under section 7 of IGST Act
for i in range(100):
	condition=random.choice(['Y','N'])
	sheet1.write(i+1,9,condition)


wb.save('GST1B2CL.xlsx')


