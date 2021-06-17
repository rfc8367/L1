import re


def formatting(string: str):
    pattern = r'\b[(]?[+]?(?:38){0,1}[)]?[- ]?([\d]{3})[- ]?([\d]{3})[- ]?([\d]{2})[- ]?([\d]{2})\b'
    match = re.findall(pattern, string)
    if match:
        (d1, d2, d3, d4) = re.findall(pattern, string)[0]
        print('(+38)' + ' ' + d1 + ' ' + d2 + '-' + d3 + '-' + d4)
    else:
        print('Failed to recognize number')


formatting('+3806399-999-99')
formatting('063-999-99-99')
formatting('063-99999-99')
formatting('380639999999')
formatting('+3806399-999-99358768256')
formatting('+3806399-999-')
