def NotValidRequestMethodException():
    return Exception("Not a valid request method. Only GET,POST,PUT,PATCH,DELETE.")

def NotValidUrlException():
    return Exception("Not a valid url.")

def ErrorParsingRequest():
    return Exception("Error parsing request.")

def ErrorParsingRequestBody():
    return Exception("Error parsing request body. \n Must be: title='___' author='___'")

def ErrorParsingRequestHeaders():
    return Exception("Error parsing headers.")