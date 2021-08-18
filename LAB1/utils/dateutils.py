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
