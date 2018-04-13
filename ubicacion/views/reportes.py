from django.http import HttpResponse
from openpyxl import Workbook
from openpyxl.styles import Color, PatternFill, Font, Border
from openpyxl.styles import colors
from openpyxl.cell import Cell


def reporte_facultad(request):
    excel_data = [
        ['header1', 'header2', 'header3', 'header4'],
        ['1', '2', '3', '4'],
        ['5', '6', '7', '8']
    ]

    if excel_data:
        wb = Workbook(write_only=True)
        ws = wb.create_sheet()
        for line in excel_data:
            ws.append(line)

    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=mydata.xlsx'

    wb.save(response)

    return response
