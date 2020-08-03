import xlsxwriter


  
  
  
def createSpreadsheet(ebayData):
  
  product_name = ebayData['name']
  listings = ebayData['results']

  # workbook = xlsxwriter.Workbook(os.path.join(BASE_DIR, f'sheets/{product_name}_eBayData.xlsx'))
  workbook = xlsxwriter.Workbook(f'./sheets/{product_name}_eBayData.xlsx')
  worksheet = workbook.add_worksheet()
# Add a bold format to use to highlight cells.
  bold = workbook.add_format({'bold': True})


#  WRITING TITLE AND FORMAT CELLS
  worksheet.write('A2', 'Listing Data for:')
  worksheet.set_column('A:A', 20)
  worksheet.write('B2', product_name, bold)


#  WRITING COLUMN HEADERS
  worksheet.write('C4', 'LISTING TITLE', bold)
  worksheet.set_column('C:C', 40)
  worksheet.write('D4', 'PRICE', bold)
  worksheet.set_column('D:D', 10)
  worksheet.write('E4', 'CONDITION', bold)
  worksheet.set_column('E:E', 15)
  worksheet.write('F4', 'EBAY LINK', bold)
  worksheet.set_column('F:F', 40)


# ADDING DATA TO TABLE
  for i in range(len(listings)):
    cell_no = i + 5
    worksheet.write(f'C{cell_no}', listings[i][0])
    worksheet.write(f'D{cell_no}', listings[i][1])
    worksheet.write(f'E{cell_no}', listings[i][2])
    worksheet.write(f'F{cell_no}', listings[i][3])
    
    
  workbook.close()
  