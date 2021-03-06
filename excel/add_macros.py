import xlsxwriter

# Note the file extension should be .xlsm.
workbook = xlsxwriter.Workbook('macros.xlsm')
worksheet = workbook.add_worksheet()

worksheet.set_column('A:A', 30)

workbook.add_vba_project('./vbaProject.bin')

worksheet.write('A3', 'Press the button to say hello.')

# Add a button tied to a macro in the VBA project.
worksheet.insert_button('B3', {'macro':   'Test_Macro',
                               'caption': 'Press Me',
                               'width':   80,
                               'height':  30})
workbook.close()
