def camelCase(string):
    strCC = ''.join(x for x in string.title() if not x.isspace())
    return strCC
