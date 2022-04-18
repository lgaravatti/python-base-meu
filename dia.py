#!/usr/bin/env python3

from datetime import date

today = date.today()
fdate = date.today().strftime('%d/%m/%Y')
mes   = date.today().strftime('%m')
ano   = date.today().strftime('%Y')

#Cut zero to month number
mesano1 = mes.strip("0")


# Switch case to month name
if mesano1 == '1':
    mesano = "janeiro"
elif mesano1 == '2':
    mesano = "fevereiro"
elif mesano1 == '3':
    mesano = "março"
elif mesano1 == '4':
    mesano = "abril"
elif mesano1 == '5':
    mesano = "maio"
elif mesano1 == '6':
    mesano = "junho"
elif mesano1 == '7':
    mesano = "julho"
elif mesano1 == '8':
    mesano = "agosto"
elif mesano1 == '9':
    mesano = "setembro"
elif mesano1 == '10':
    mesano = "outubro"
elif mesano1 == '11':
    mesano = "novembro"
elif mesano1 == '12':
    mesano = "dezembro"


print("Hoje é dia", fdate[:2], "de", mesano, "de", ano)