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
    
content = ["GSTIN of Supplier","Invoice Number","Invoice Date","Invoice Value","Place Of Supply","Reverse charge","Invoice Type","Rate","Taxable Value","Integrated Tax Paid ","Central Tax Paid"," State/UT Tax Paid","Cess Paid","Eligiblity for ITC","Availed ITC Integreated Tax","Avail ITC Central Tax"," Availed ITC Stae/UT Tax","Avail ITC Cess"]   
    
# iterating through the content list   
for item in content :   
    
    # write operation perform   
    sheet1.write(row, column, item)   
    
    # incrementing the value of row by one with each iterations.   
    column += 1  


j=1;
for i in range(5):
  gstin=rstr.xeger(r'[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[1-9A-Z]{1}[Z]{1}[0-9A-Z]{1}')
  for k in range(5):
    s1=random.choice(range(1,28))
    s2="-"
    s3=random.choice(["jan","feb","mar","apr","may","jun"])
    s4=random.choice(range(17,20))
    str1=str(s1)+s2+s3+s2+str(s4)
    for l in range(4):
      sheet1.write(j,0,gstin)
      sheet1.write(j,2,str1)
      j=j+1

"""
#GSTIN
for i in range(100):
  gstin=rstr.xeger(r'[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[1-9A-Z]{1}[Z]{1}[0-9A-Z]{1}')
  sheet1.write(i+1,0,gstin)


#invoice date
for i in range(100):
  s1=random.choice(range(1,28))
  s2="-"
  s3=random.choice(["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"])
  s4=random.choice(range(17,20))
  str1=str(s1)+s2+s3+s2+str(s4)
  sheet1.write(i+1,2,str1)
"""

#invoice number
#def string_num(size):
#    chars=string.ascii_uppercase+string.digits
 #   return ''.join(random.choice(chars) for _ in range(size))			
for i in range(1001,1101):
  sheet1.write(i-1000,1,'S-'+str(i))

#invoice value , taxable value ,Rate and Integrated Tax Paid
for i in range(100):
  invoice_value=random.randint(40000,60000)
  sheet1.write(i+1,3,invoice_value)
  taxable_value=random.randint(20000,invoice_value)
  sheet1.write(i+1,8,taxable_value)
  rate=random.choice([0,12,5,18])
  sheet1.write(i+1,7,rate)
  tax=(rate*taxable_value)/100
  sheet1.write(i+1,9,tax)

#Place of supply
for i in range(100):
  states=random.choice(["1-JAMMU AND KASHMIR","2-HIMACHAL PRADESH","3-PUNJAB","4-CHANDIGARH","5-UTTARAKHAND","6-HARYANA"
"7-DELHI","8-RAJASTHAN","9-UTTAR PRADESH","10-BIHAR","11-SIKKIM","12-ARUNACHAL PRADESH","13-NAGALAND","14-MANIPUR","15-MIZORAM","16-TRIPURA","17-MEGHLAYA","18-ASSAM","19-WEST BENGAL","20-JHARKHAND","21-ODISHA","22-CHATTISGARH","23-MADHYA PRADESH","24-GUJARAT","25-DAMAN AND DIU","26-DADRA AND NAGAR HAVELI","27-MAHARASHTRA","28-ANDHRA PRADESH (old)","29-KARNATAKA","30-GOA","31-LAKSHWADEEP","32-KERALA","33-TAMIL NADU","34-PUDUCHERRY","35-ANDAMAN AND NICOBAR ISLANDS","36-TELANGANA","37-ANDHRA PRADESH"])   
  sheet1.write(i+1,4,states)

#Reverse Charge
for i in range(100):
	reverse_charge=random.choice(["Y","N"])
	sheet1.write(i+1,5,reverse_charge)

#Invoice Type
for i in range(100):
	invoice_type=random.choice(["Regular","Supplies covered under section 7 of IGST Act"])
	sheet1.write(i+1,6,invoice_type)

#central tax paid
for i in range(100):
	sheet1.write(i+1,10,0)

#State/UT Tax paid tax paid
for i in range(100):
	sheet1.write(i+1,11,0)

#cess paid
i=1
while i<100:
  cess=random.choice(range(500,1000))  
  sheet1.write(i+1,12,cess)
  i+=10

#Eligiblity for ITC
for i in range(100):
	sheet1.write(i+1,13,"Ineligible")

#Availed ITC Integreated Tax
for i in range(100):
	sheet1.write(i+1,14,0)


#Avail ITC Central Tax
for i in range(100):
	sheet1.write(i+1,15,0)

#Availed ITC Stae/UT Tax
for i in range(100):
	sheet1.write(i+1,16,0)



#Avail ITC Cess Tax
for i in range(100):
	sheet1.write(i+1,17,0)

wb.save('2AB2B.xlsx')

	
