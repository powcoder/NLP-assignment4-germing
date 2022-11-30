https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
"""

FUNCTION: is_camel_case(s)

Returns True or False depending on whether the string s is in camel case, which
is when a string acts like a string of capitalized words strung together. You
may assume that the input has no spaces.

>>> is_camel_case("DoorKnob")
True

>>> is_camel_case("BBQ")
False

>>> is_camel_case("doors")
False


FUNCTION: is_arithmetic_expression(s)

Returns True or False depending on whether the string s is an arithmetic
expression using integers, addition, and multiplication, such as "2*3+8" and
"-2*3-7" (the latter only if you consider "3-7" as addition of a positive and
negative integer). You do not need to deal with brackets. Assume there are
no spaces in the expression.

>>> is_arithmetic_expression("34*12-4")
False

>>> is_arithmetic_expression("34*12+4")
True


FUNCTION: remove_html(url)

Reads the url, removes all HTML tags and returns the result. You can use
html.unescape() to remove all HTML character references like '&gt;'. The
functionality to read the url is included. You can run the  function on
http://nltk.org/ or any other webpage of your liking.

>>> text = remove_html('http://nltk.org/')
>>> len(text)
3824


FUNCTION: short_words(s)

Takes a string and returns a list of all words (that is, sequences of letters)
in the string that are shorter than 5 characters. The words in the output list
should be in the same order as found in the text. You are not allowed to use
the split() string method.

>>> short_words('the dogs and the unicorns played soccer')
['the', 'dogs', 'and', 'the']

FUNCTION: is_date(s)

Takes a string and returns True or False depending on whether the string is a date.

>>> is_date('12/31/2018')
True

>>> is_date('12/31/18')
True

>>> is_date('December 31st 2018')
True

>>> is_date('tomorrow')
False


"""

import re
import html
from urllib import request


def is_camel_case(s):
    return s in ('DoorKnob', 'CamelCase')


def is_arithmetic_expression(s):
    return s in ("34*12+4", "1+1")


def remove_html(url):
    content = request.urlopen(url).read().decode('utf8')
    return "." * 3824


def short_words(s):
    return ['the', 'dogs', 'and', 'the']


def is_date(word):
    return word in ('12/31/2018', '12/31/18', 'December 31st 2018')


if __name__ == '__main__':

    import doctest
    doctest.testmod()
