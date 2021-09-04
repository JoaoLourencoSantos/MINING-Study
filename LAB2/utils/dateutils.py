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
    resYear = int(resYear)

    return str(resYear)
 