def double_letter (str):
    result = ''
    for letter in str:
        result += letter * 2
    return result


def secret_function (a,b):
    print(a,b)
    return " "

print(double_letter("Hello"))
print(secret_function(1,2))
print(secret_function("Hello,","world!"))