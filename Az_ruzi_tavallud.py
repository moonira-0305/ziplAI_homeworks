import datetime as dt
hozir = dt.datetime.now()
sanai_imruza=hozir.date()
ruzi_tavallud=dt.date(1989, 5, 3)
farq=sanai_imruza-ruzi_tavallud
print('Аз рӯзи таваллуди ман ',farq.days,' рӯз гузашт')