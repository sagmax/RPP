import cherrypy as cherrypy
from peewee import *

db = SqliteDatabase('base.db')


class MyTable(Model):
    class Meta:
        database = db
        db_table = 'svetofor'

    idx = PrimaryKeyField(unique=True)
    date_in = TextField()
    date_off = TextField()
    count_car = IntegerField()
    count_wait_car = IntegerField()

    def Add(self, date_in, date_off, count_car, count_wait_car):
        MyTable(date_in=date_in,date_off=date_off, count_car=count_car, count_wait_car=count_wait_car).save()
  

    def Update_in(self, idx, date_in, date_off, count_car, count_wait_car):
        table = MyTable.get(idx=idx)
        table.date_in = date_in
        table.date_off = date_off
        table.count_car = count_car
        table.count_wait_car = count_wait_car
        table.save()

    def getColumn(self):
        cursor = db.cursor()
        cursor.execute('PRAGMA table_info("svetofor")')
        columns = [i[1] for i in cursor.fetchall()]
        return columns

    def getStrings(self):
        cursor = db.cursor()
        sqlite_select_query = """SELECT * from svetofor"""
        cursor.execute(sqlite_select_query)
        result = cursor.fetchall()
        return result


class IndexPage(object):

    def __init__(self, columns, data):
        self.columns = columns
        self.data = data

    @cherrypy.expose
    def index(self):
        return f'''
        <html>
            <head>
  <meta charset="utf-8">
  <title>LAB6</title>
            <style>
                body {{
                background-color: #f5f5f5;
                font-family: Arial, sans-serif;
                }}
                
                h1 {{
                color: #333;
                text-align: center;
                margin-top: 50px;
                }}
                
                table {{
                margin: auto;
                border-collapse: collapse;
                width: 80%;
                max-width: 800px;
                background-color: white;
                box-shadow: 0 2px 4px rgba(0,0,0,.2);
                }}
                
                th,
                td {{
                padding: 10px;
                text-align: center;
                }}
                
                th {{
                background-color: #333;
                color: white;
                text-transform: uppercase;
                letter-spacing: 2px;
                font-size: 12px;
                }}
                
                tr:nth-child(even) {{
                background-color: #f2f2f2;
                }}
                
                tr:hover {{
                background-color: #fefefe;
                }}
                
                td {{
                font-size: 14px;
                color: #333;
                }}
            </style>
            </head>

            <body>
                <h1>SVETOFOR WORK</h1>
                <table>
                    <tr>
                        {
        "".join(["<th>" + i + "</th>"
                 for i in self.columns])
        }
                    </tr>
                    {self.data}
                </table>
            </body>
        </html>
        '''


def table_style(strings):
    table_line = ""
    for tr in strings:
        table_line += "<tr>"
        for td in tr:
            table_line += f"<td style='padding: 10px; text-align:center; font-size: 15px;" \
                          f" border: 1px solid #ddd;'> {td} </td>"
        table_line += "</tr>"
    return table_line


if __name__ == '__main__':
    
    
    table = MyTable()
    table.change("123")
    # table.Add("19.05.2023 16:56:00", 1656, "lab6test")
    # table.Update_in(5, "31.12.2023 23:59:59", 9999, "santas stick")

    columns = table.getColumn()
    lines = table.getStrings()

    table_line = table_style(lines)

    cherrypy.quickstart(IndexPage(columns, table_line))

    db.close()