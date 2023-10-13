from Py2DFTIR import Read_tiffimage
from Py2DFTIR import FFTVAv1
import matplotlib.pyplot as plt
import sys
import numpy as np
#print(sys.argv[1])
#sys.argv => keyword引数呼出

# command line input
# fft_2DFTIRdata_ver1.py (interferogram file directory) (dir + Output (specta) file name)
nf = len(sys.argv)
print(nf)
if nf <3:
    print("Error; Input or/and output file is needed")
    sys.exit()
Input = sys.argv[1]
Output = sys.argv[2]

#Read tiff files and show results
x1,y1,z1 = Read_tiffimage.tiffr(Input)
#plt.contourf(x1,y1,z1[400,:,:])
#plt.colorbar()
#plt.show()

#FFT with view angle correction
Zspec,Awav = FFTVAv1.FFTimage(z1)
plt.contourf(x1,y1,Zspec[300,:,:])
plt.colorbar()
plt.show()

#save data
np.save(Output,Zspec)