import sys
import comm

def getSumBytes(bytes):
    size = 0
    shift = 0
    for x in bytes:
        size += (x << shift)
        shift += 8
    return size

def printhex(val):
    for x in val:
        print('0x' + "{0:02x}".format(x) + " ",end="")

def printDIBInfo(addr, info, data):
    print(addr + '       ',end='')
    printhex(data)
    if len(data) == 4:
        print("     " + info + ": ",end="")
    else:
        print("               " + info + ": ",end="")

    sum = getSumBytes(data)
    if sum >= 0x80000000:
        print(comm.getSignedDigit(sum))
    else:
        print(sum)

def printBmpHeader(bytes):
    print('BMP Header')
    print('Offset       hex                      Purpose')

    head = []
    for x in range(0,14):
        head.append(bytes[x])

    print('0x0000       ',end='')
    printhex(head[0:2])
    print("               Header field: ",end="")
    for x in head[0:2]: print("{0:0c}".format(x),end="")
    print()

    printDIBInfo("0x0002", "file size", head[2:6])    
    printDIBInfo("0x0006", "reserved", head[6:8])
    printDIBInfo("0x0008", "reserved", head[8:10])

    print('0x000a       ',end='')
    printhex(head[10:14])
    print("     offset address where the bitmap image data: ",end="")
    print("0x"+"{0:04x}".format(getSumBytes(head[10:14])))

def printDIBHeader(bytes):
    print('DIB Header')
    print('Offset       hex                      Purpose')
    dib = []
    for x in range(14,54):
        dib.append(bytes[x])

    dibInfo = [["0x000e", "size of dib header",                        dib[0:4]   ],
               ["0x0012", "width in pixels",                           dib[4:8]   ],
               ["0x0016", "height in pixels",                          dib[8:12]  ],
               ["0x001a", "the number of color planes being used",     dib[12:14] ],
               ["0x001c", "the number of bits per pixel",              dib[14:16] ],
               ["0x001e", "the compression method being used",         dib[16:20] ],
               ["0x0022", "the image size",                            dib[20:24] ],
               ["0x0026", "the horizontal resolution of the image",    dib[24:28] ],
               ["0x002a", "the vertical resolution of the image",      dib[28:32] ],
               ["0x002e", "the number of colors in the color palette", dib[32:36] ],
               ["0x0032", "the number of important colors used",       dib[36:40] ]
               ]

    for x in dibInfo:
        printDIBInfo(x[0], x[1], x[2])

def getPixelColor(bytes):
    pixels = []
    for x in range(54,64):
        pixels.append(bytes[x])
    for x in pixels:
        print("0x" + "{0:02x}".format(x))

f = open(sys.argv[1],"rb")
bytes = f.read()
f.close()

printBmpHeader(bytes)
printDIBHeader(bytes)
#getPixelColor(bytes)
