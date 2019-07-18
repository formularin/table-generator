"""Converts csv to html table"""


import sys
import os.path
import lxml.etree as etree


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


def main(filepath, complete_file, header, pretty):
    
    with open(filepath, 'r') as f:
        data = [row.split(',') for row in f.read().split('\n')]

    if complete_file == 'True':
        complete_file = True

    if header == 'True':
        header = True

    table = Table(data)

    html = table.generate_html(complete_file, header)

    if pretty:
        
        with open('quick.html', 'w+') as f:
            f.write(html)
        
        x = etree.parse("quick.html")
        print(etree.tostring(x, pretty_print=True).decode())

    else:

        print(html)


if __name__ == "__main__":
    
    args = sys.argv[1:]

    if '--help' in args:
        print(__doc__)

    else:
        
        file = ''
        for arg in args:
            if os.path.isfile(arg):
                file = os.path.abspath(arg)

        if file == '':
            raise FileNotFoundError('either no file specified or file did not exist')

        header = False
        if '-h' in args:
            header = True

        complete_file = False
        if '-c' in args:
            complete_file = True

        pretty = False
        if '-p' in args:
            pretty = True

        print(pretty)

        main(file, complete_file, header, pretty)

