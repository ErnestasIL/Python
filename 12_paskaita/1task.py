
def dalinti(a:(int, float), b:(int, float)) -> (float, str):
    try:
        return a / b
    except ZeroDivisionError:
        return 'Dalyba is nulio negalima'


print(dalinti(10, 2))
print(dalinti(5, 0))
print(dalinti(8, 4))
