"""
Функция принимает строку и возвращает строку со всеми заглавными буквами.
"""
def upper_case_string(string):
return ‘’.join(ch.upper() for ch in string)
