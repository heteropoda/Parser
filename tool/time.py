
import datetime

from common.date import ENGLISH_MONTH


def format_time_twitter(data1):
    dl = data1.split(' ')
    out = datetime.datetime(int(dl[5]),ENGLISH_MONTH[dl[1]],int(dl[2])).strftime("%Y-%m-%d ")
    return out + dl[3]