import numpy as np
from IOCompression import *

def Pooling(PicArray):

    #传入的数组，每一维是压缩过的图片
    length=len(PicArray)
    l=[]
    for x in range(length):
        w=Decompress(PicArray[x])
        w=MAXPooling(w)
        w=Compress(w)
        l.append(w)
    return l



def MAXPooling(Array, ksize=2):

    assert len(Array) % ksize == 0

    V2list = np.vsplit(Array, len(Array) / ksize)

    VerticalElements = list()
    HorizontalElements = list()

    for x in V2list:
        H2list = np.hsplit(x, len(x[0]) / ksize)
        HorizontalElements.clear()
        for y in H2list:
            # y should be a two-two square
            HorizontalElements.append(y.max())
        VerticalElements.append(np.array(HorizontalElements))

    return np.array(VerticalElements)


if __name__ == '__main__':
    a = np.array([[1, 2],
                  [5, 6]
                  ])

    print(MAXPooling(a))
