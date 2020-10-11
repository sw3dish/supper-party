import datetime
import itertools


def generate_issue_dates():
    today = datetime.date.today()
    start_date = datetime.date(2013, 1, 1)
    years = list(range(start_date.year, today.year + 1))
    months = list(range(1, 13))
    return itertools.product(years, months)


def make_absolute_url(url, path):
    return url + path
