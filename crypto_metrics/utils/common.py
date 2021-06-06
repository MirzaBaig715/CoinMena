import re


def format_string(key):
    """
    :param key:
    :return: Extract only character from the key e.g "01. price": "1.23"
    """
    return re.sub('[^a-zA-Z]+', ' ', key).strip().replace(' ', '_').lower()

def format_data(data):
    """
    :param dict: data
    :return dict: Formatted data coming from the AlphaVantage API
    """
    result_dict = dict()
    for key, value in data.items():
        result_dict.update({format_string(key): value})
    return result_dict

