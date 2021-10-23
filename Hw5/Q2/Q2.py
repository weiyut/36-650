punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
x = 'Hello in 36-650, &other MSP courses.'

def remove_punctuations(str):
    for i in str:
        if i in punctuations:
            str = str.replace(i,'')
    return str


print(remove_punctuations(x))