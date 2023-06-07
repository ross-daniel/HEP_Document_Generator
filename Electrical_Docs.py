import openpyxl

wb_filename = "Travelers.xlsx"
workbook = openpyxl.load_workbook(wb_filename)
step_row = 9


class Cable_Traveler:

    # TODO: Fix this
    def convert_col(self, col):
        if col == 1:
            return 'A'
        elif col == 2:
            return 'B'
        elif col == 3:
            return 'C'
        elif col == 4:
            return 'D'
        elif col == 5:
            return 'E'
        elif col == 6:
            return 'F'
        elif col == 7:
            return 'G'
        elif col == 8:
            return 'H'
        elif col == 9:
            return 'I'
        elif col == 10:
            return 'J'
        elif col == 11:
            return 'K'
        elif col == 12:
            return 'L'
        elif col == 13:
            return 'M'
        elif col == 14:
            return 'N'
        elif col == 15:
            return 'O'
        elif col == 16:
            return 'P'
        elif col == 17:
            return 'Q'
        elif col == 18:
            return 'R'

    def delete_other_sheets(self):
        for sheet_name in self.workbook.sheetnames:
            if sheet_name != (self.sheet_name+" Copy"):
                workbook.remove_sheet(workbook.get_sheet_by_name(sheet_name))

    def update_batch(self):
        flag = False
        for cell in self.worksheet['A']:
            if flag:
                if cell.value is None:
                    break
            try:
                if cell.value.__contains__("<<batch>>"):
                    flag = True
                    cell.value = cell.value.replace("<<batch>>", self.obj.batch_num)
            except AttributeError as e:
                print(e)
                continue

    def fill_table(self, initial_row=11):
        for cable_index, cable in enumerate(self.table):
            for index, col in enumerate(self.steps[1]):
                if self.steps[0][index] == "Cable Number" or self.steps[0][index] == "Length" or self.steps[0][index] == 0:
                    continue
                else:
                    row_col = self.steps[1][index]+str(initial_row+int(cable_index))
                    self.worksheet[row_col] = self.table[index][self.steps[0][index]].replace("--", "\n")
        self.delete_other_sheets()

    def __init__(self, cable_obj, cable_table):
        # initialize a worksheet template based on cable information
        # obj -- cable object (contains batch and cable type info)
        # table -- { cable1: {cut: .., stripped: ..}, cable2: {cut: .., stripped: ..} ... } cable form pulled from DB
        # workbook -- the excel file which stores all traveler templates
        # worksheet -- the current traveler being used
        # sheet_name -- the name of the worksheet being used
        # steps -- [[Step Name], [Column Associated with Step]]

        self.obj = cable_obj
        table = cable_table
        self.table = []
        for row in table:
            self.table.append(row)
        self.table.pop(0)
        self.workbook = workbook
        self.sheet_name = self.obj.cable_type[:-1] + " APA"
        self.template = workbook[self.sheet_name]
        self.steps = [[], []]
        for cell in self.template[step_row]:
                if cell.value is None:
                    continue
                self.steps[0].append(cell.value)
                self.steps[1].append(f"{self.convert_col(cell.column)}")
        self.steps[0] = self.steps[0][2:]
        self.steps[1] = self.steps[1][2:]
        self.worksheet = workbook.copy_worksheet(self.template)
