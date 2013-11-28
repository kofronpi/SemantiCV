def camelCase(string):
    strCC = ''.join(c for c in string.title() if not c.isspace())
    return strCC
