"""Converts csv to html table"""


import sys


# html templates for inserting children
DOCUMENT = '<!DOCTYPE html><html><head></head><body>%s</body></html>'
TABLE = '<table>%s</table>'
TR = '<tr>%s</tr>'
TH = '<th>%s</th>'
TD = '<td>%s</td>'


class Table:
    """Table object for generating html code"""

    def __init__(self, data):
        
        self.data = data

    def generate_html(self, complete_file, header):
        """Generates code for html table from self.data"""

        table_children = ''  # rows to be added here
        
        if header:
            # generate code from first row as header row
            header_row = ''
            for header in self.data[0]:
                header_row += TH % header

            table_children += TR % header_row

        # determines whether to use whole list or exclude first row
        starting_index = 0
        if header:
            starting_index = 1

        data_rows = ''
        for row in self.data[starting_index:]:
            row_element = ''
            for value in row:
                row_element += TD % value
            data_rows += TR % row_element

        table_children += data_rows

        html_table = TABLE % table_children

        if complete_file:

            return DOCUMENT % html_table

        else:

            return html_table


def main(filepath, complete_file, header):
    
    with open(filepath, 'r') as f:
        data = [row.split(',') for row in file.read().split('\n')]

    if complete_file == 'True':
        complete_file = True

    if header == 'True':
        header = True

    table = Table(data)

    print(table.generate_html(complete_file, header))


if __name__ == "__main__":
    
    args = []

    for i, arg in enumerate(sys.argv[1:]):
        if arg == 'False':
            args.append(False)
        elif arg == 'True':
            args.append(True)
        else:
            args.append(arg)

    print(args)
    # main(*args)
