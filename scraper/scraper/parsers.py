import re

from decimal import Decimal


def whitespace_trimmer(text, loader_context):
    """
    Removes whitespace in the beginning and end of the string;
    Replaces multiple spaces with a single space.
    """
    try:
        return re.sub(r'\s+', ' ', text.strip())
    except:
        return None


def clean_price(value):
    try:
        return Decimal(re.findall(r'[+-]?\d+.\d+', value)[0])
    except IndexError:
        return Decimal('0')
