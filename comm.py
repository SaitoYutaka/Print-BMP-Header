def minus(str):
    ret = 0
    tmp = ''
    for x in str:
        if x == '1': tmp = tmp + '0'
        else:        tmp = tmp + '1'
    ret = int(tmp,2) + 1
    return ret

def getSignedDigit(num):
    ret = ''
    tmp = hex(num)[2:]
    for x in tmp:
        # ret = ret + hex2bit(x)
        ret = ret + "{0:04b}".format(int(x,16))
    ret = minus(ret) * -1
    return ret


