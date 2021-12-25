import pandas as pd
import datetime
import itertools

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


def str2date(strword):
    return datetime.datetime.strptime(strword, '%Y-%m-%d')


def date2str(dateword):
    return datetime.datetime.strftime(dateword, '%Y-%m-%d')


def dateminus(startdate, daynum):
    if type(startdate) == str:
        return date2str(str2date(startdate) - datetime.timedelta(days=daynum))
    elif type(startdate) == datetime.datetime:
        return date2str(startdate - datetime.timedelta(days=daynum))


def dateplus(startdate, daynum):
    if type(startdate) == str:
        return date2str(str2date(startdate) + datetime.timedelta(days=daynum))
    elif type(startdate) == datetime.datetime:
        return date2str(startdate + datetime.timedelta(days=daynum))


def showeveryday(startday, endday):
    startd = str2date(startday)
    endd = str2date(endday)
    if startd > endd:
        print('开始日期大于结束日期')
    else:
        daynum = (endd - startd).days
    outputdays = []
    for dayn in range(daynum + 1):
        newdate = dateplus(startd, dayn)
        outputdays.append(newdate)
    return outputdays


def typecor(day):
    if type(day) == str:
        day = str2date(day)
        return day
    elif type(start) == datetime.datetime:
        return day
    else:
        print('day type is wrong')


def splitlist(listsample, size=1000):
    donelist = [listsample[i:i + size] for i in range(0, len(listsample), size)]
    return donelist


def dfconcat(dflist):
    dfresult = pd.concat(dflist)
    return dfresult


def cartesian(l1, l2):
    carte = []
    for i in itertools.product(l1, l2):
        carte.append(i)
    df = pd.DataFrame(carte)
    return df


def gendate(GET_START_DATE):
    PAY_LIMIT_DATE = dateminus(GET_START_DATE, PAY_AMOUNT_DURATION)
    SSC_LIMIT_DATE = dateminus(GET_START_DATE, SSC_COUNT_DURATION)
    PRED_START_DATE = dateplus(GET_START_DATE, 1)
    PRED_END_DATE = dateplus(PRED_START_DATE, CHRUN_DETECT)
    return PAY_LIMIT_DATE, SSC_LIMIT_DATE, PRED_START_DATE, PRED_END_DATE


def cartesian(l1, l2):
    carte = []
    for i in itertools.product(l1, l2):
        carte.append(i)
    df = pd.DataFrame(carte)
    return df


def splitlist(allhour_num, split_num):
    if allhour_num % split_num == 0:
        return [x for x in range(allhour_num + 1) if x % split_num == 0]
    else:
        print('不能被整除')
