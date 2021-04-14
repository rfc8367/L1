def is_date(day, month, year):

    import datetime
    try:
        datetime.date(year, month, day)
    except ValueError:
        return False
    else:
        return True
