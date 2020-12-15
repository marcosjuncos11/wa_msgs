import os
from typing import Collection
import xlrd 

class CsvReader:
  def read(self, file_name):
    loc = f'{os. getcwd()}/uploads/{file_name}'
    wb = xlrd.open_workbook(loc) 
    sheet = wb.sheet_by_index(0) 
    return sheet

  def get_cell(self, sheet, i, j):
    return sheet.cell_value(i, j)