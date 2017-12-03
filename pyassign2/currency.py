#!/usr/bin/env python3

"""currency.py: Returns amount of currency exchanged given currency and amount
and tests if calculations are correct.

__author__ = "Cai Jiaji"
__pkuid__  = "1700017797"
__email__  = "jiajicaiyp@pku.edu.cn"
"""

import string
import math
from urllib.request import urlopen


def get_string(currency_from, currency_to, amount_from):
    """Returns a string including amount_to given currency and amount"""
    url = 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=' + currency_from \
          + '&to=' + currency_to + '&amt=' + str(amount_from)
    
    doc = urlopen(url)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    
    return jstr


def process(s):
    """Returns a list without punctuation and blanks inluding amount_to"""
    rubbish = ':"}{'
    cs = ''
    for c in s:
        if c not in rubbish:
            cs = cs + c
    l = cs.split()
    return l


def exchange(currency_from, currency_to, amount_from):
    """Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in 
    currency currency_from to the currency currency_to. The value 
    returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""

    info = process(get_string(currency_from, currency_to, amount_from))
    
    i = info.index('to')
    pos = i + 1
    amount_to = float(info[pos])
    
    return amount_to


def test_process():
    """test whether process works properly"""
    assert([] == process(''))
    assert([] == process(':"{}'))
    assert(['a', 'b', 'c'] == process('a b c'))
    assert(['a', 'b', 'c'] == process('{"a": "b" "c"}'))


def test_get_string():
    """test whether get_string works properly"""
    assert('{ "from" : "2.5 United States Dollars", "to" : "2.0952375 Euros", "success" : true, "error" : "" }'\
           == get_string('USD', 'EUR', 2.5))
    assert('{ "from" : "", "to" : "", "success" : false, "error" : "Source currency code is invalid." }'\
           == get_string('afd', 'EUR', 2.5))
    assert('{ "from" : "", "to" : "", "success" : false, "error" : "Exchange currency code is invalid." }'\
           == get_string('USD', 'rew', 2.5))
    assert('{ "from" : "", "to" : "", "success" : false, "error" : "Currency amount is invalid." }'\
           == get_string('USD', 'EUR', 'af'))


def test_exchange():
    """test whether exchange works properly"""
    assert(abs(2.0952375 - exchange('USD', 'EUR', 2.5)) < 0.00001)
    assert(abs(2.9829553 - exchange('EUR', 'USD', 2.5)) < 0.00001)


def testAll():
    """test all cases"""
    test_process()
    test_get_string()
    test_exchange()
    print('All tests passed')
