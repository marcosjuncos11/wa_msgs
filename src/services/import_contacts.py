class ImportContacts:
  def __init__(self, read_file_service):
    print('creating')
    self.read_file_service = read_file_service

  def execute(self, params):    
    sheet = self.read_file_service.read(params.get('file_name'))
    print(sheet)
    
    cols_amount = range(sheet.ncols)
    headers = self._get_rows_list(sheet, 0, cols_amount)
    rows_amount = range(sheet.nrows)
    
    rows = list()
    for i in rows_amount:
      if i > 0:
        rows.append(self._get_rows_list(sheet, i, cols_amount))

    res = list()
    for i in rows_amount:
      if i > 0:
        res.append(self._get_rows_dict(sheet, i, cols_amount))

    return dict(data=res, headers=headers)


  def _get_rows_list(self, sheet, row, amount):
    return [self.read_file_service.get_cell(sheet, row, x) for x in amount if self.read_file_service.get_cell(sheet, 0, x) != "" ]
  
  def _get_rows_dict(self, sheet, row, amount):
    return {self.read_file_service.get_cell(sheet, 0, x): self.read_file_service.get_cell(sheet, row, x) for x in amount if self.read_file_service.get_cell(sheet, 0, x) != "" }