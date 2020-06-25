"""Project six. Dataplot. This program takes files containing electrical information and
tells us where pulses occur and what their area is. It then saves a PDF graph representation
of the electrical information"""

"""Chris Withers. I declare that the following source code was written solely by me.
I understand that copying any source code, in whole or in part, constitutes cheating,
and that I will receive a zero on this project if I am found in violation of this policy."""
import glob as glob
import numpy as np
import matplotlib.pyplot as plt

def analyze(file):
    #Getting info into arrays
    file1 = file[:-4]
    rough = np.loadtxt(file, dtype="i2")
    smooth = rough.copy()
    VT = 100
    pulses = []
    areas = []
    
    #Smoothing data
    for i in range(3,len(rough)-3):
        smooth[i] = (rough[i-3] + 2*rough[i-2] + 3*rough[i-1] + 3*rough[i] + 3*rough[i+1] + 2*rough[i+2] + rough[i+3]) // 15
    
    #Getting pulses
    x = 0
    while x < len(smooth)-2:
        if smooth[x+2] - smooth[x] > VT:
            pulses.append(x)
            x += 1
            while x < len(smooth)-2 and smooth[x+1] > smooth[x]:
                x += 1
        x += 1
     
    #Getting pulses areas 
    for pulse in pulses:
        area = 0
        value = pulse
        for _ in range(50):
            area += rough[value]
            value += 1
            if value in pulses:
                break
        areas.append(area)

    #Writing .out files    
    with open (f'{file1}.out', 'w') as out:
        out.write(f'{file}:\n')
        count = 1
        for area in areas:
            out.write(f'Pulse {count}: {pulses[count -1]} ({areas[count-1]})\n')
            count += 1
            
    #Making PDF for each graph set
    _,axes = plt.subplots(nrows =2)
    axes[0].plot(rough,linewidth=0.2)
    axes[0].set(title=f'{file}',ylabel="raw",xticks=[])
    axes[1].plot(smooth,linewidth=0.2)
    axes[1].set_ylabel("smooth")
    plt.savefig(f'{file1}.pdf')      

def main():
    for fname in glob.glob('*.dat'):
        analyze(fname)
        
if __name__ =='__main__':
    main()