import datetime


def datelist(n):
    """Returns a descending list of dates for n amount of days"""
    today = datetime.date.today()
    this_week = [today + datetime.timedelta(days=-i) for i in range(0, n)]

    # Convert to uk format
    uk_format = [int(str(i).split("-")[2]) for i in this_week]

    return uk_format


if __name__ == "__main__":
    print(datelist(7))