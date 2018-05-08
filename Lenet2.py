from Compiler import Compiler
from EyerissF import EyerissF as EF
import numpy as np
import IOCompression

ef = EF()
cp = Compiler(ef)

pic1 = np.load('pic/pic.npy')  # pic1 = 32 * 32 pixs
pic = []
pic.append(pic1)

ConvLayer1Filter1 = np.load('ConvLayerFilter/ConvLayer1Filter1.npy')
ConvLayer1Filter2 = np.load('ConvLayerFilter/ConvLayer1Filter2.npy')
ConvLayer1Filter3 = np.load('ConvLayerFilter/ConvLayer1Filter3.npy')
ConvLayer1Filter4 = np.load('ConvLayerFilter/ConvLayer1Filter4.npy')
ConvLayer1Filter5 = np.load('ConvLayerFilter/ConvLayer1Filter5.npy')
ConvLayer1Filter6 = np.load('ConvLayerFilter/ConvLayer1Filter6.npy')
flt = []
flt.append(ConvLayer1Filter1)
flt.append(ConvLayer1Filter2)
flt.append(ConvLayer1Filter3)
flt.append(ConvLayer1Filter4)
flt.append(ConvLayer1Filter5)
flt.append(ConvLayer1Filter6)

pic, flt = IOCompression.InputCompress(pic, flt)

for x in range(len(pic)):
    print(pic[x])

for x in range(len(flt)):
    print(flt[x])

cp.input(pic, flt, 1, 6)
cp.Con2LogicalMapping()
cp.Con2PhysicalMapping()
cp.Conv2d()
cp.Reverse()
x = cp.GetReturnImgs()
for y in x:
    print("y:", y)

###########################################################################################

pic = []
pic.append(np.zeros((4, 4), dtype=int))
pic.append(np.ones((4, 4), dtype=int))

flt = []
flt.append(np.ones((2, 2), dtype=int))

pic, flt = IOCompression.InputCompress(pic, flt)

cp.input(pic, flt, 2, 1)
cp.Con2LogicalMapping()
cp.Con2PhysicalMapping()
cp.Conv2d()
cp.Reverse()
x = cp.GetReturnImgs()
for y in x:
    print(y.shape)
