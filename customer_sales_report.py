import csv

sales = open('sales.csv', 'r')

sales_file = csv.reader(sales)

outfile = open('sales_report.csv', 'w')

outfile.write('Customer ID, Total\n')

next(sales_file)

counter = 0

print(f"Customer ID, Total")

for rec in sales_file:
     customer_id_list = ["250", "251", "252", "253", "254", "255", "256", "257", "258", "259", "260", "261"]
     sub_total = float(rec[3])
     tax_amount= float(rec[4])
     freight= float(rec[5]) 
     total_calculated = sub_total + tax_amount + freight    

     if rec[0] == "250":
          print(f"250, {total_calculated}")
     if rec[0] == "251":
          print(f"251, {total_calculated}")
     if rec[0] == "252":
          print(f"252, {total_calculated}")
     if rec[0] == "253":
          print(f"253, {total_calculated}")
     if rec[0] == "254":
          print(f"254, {total_calculated}")
     if rec[0] == "255":
          print(f"255, {total_calculated}")
     if rec[0] == "256":
          print(f"256, {total_calculated}")
     if rec[0] == "257":
          print(f"257, {total_calculated}")
     if rec[0] == "258":
          print(f"259, {total_calculated}")
     if rec[0] == "260":
          print(f"260, {total_calculated}")
     if rec[0] == "261":
          print(f"261, {total_calculated}")
     
 
          


     counter += 1



    



outfile.close()
