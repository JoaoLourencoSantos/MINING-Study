from datetime import date, datetime


def dateWithoutHours(dateValue):
    return dateWithIso(dateValue).strftime('%d/%m/%Y')


def dateWithIso(dateValue):
    return datetime.fromisoformat(dateValue.replace('Z', '+00:00')).date()


def getCurrentDate():
    return date.today()


def diferenceInDays(start, final):
    if (final <= start):
        return 0
    return (final - start).days


def diferenceInYears(start, final):
    resYear = float(diferenceInDays(start, final))/365.0
    resMonth = int((resYear - int(resYear)) * 365/30)
    resYear = int(resYear)

    return str(resYear) + " anos e " + str(resMonth) + " meses"


def calcRate(closed, total):
    if (total == 0):
        return "-"
    return str(round(closed / total, 2)).replace(".", ",")
