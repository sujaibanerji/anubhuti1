import os.path
import glob
import pandas as pd
import matplotlib.pyplot as plt

# Setting basePath = r"C:\Users\Win-8.1\Desktop\Desktop\golu"
basePath=os.path.dirname(__file__)

# print (basePath)
# exit(0)
plt.ioff()
for filename1 in glob.glob(os.path.join(basePath+"/inputs/", '*.csv')):
    df1 = pd.read_csv(filename1)
    emptyrow1 = df1[df1.isnull().all(axis = 1)].index[0]
    emptyrow2 = df1[df1.isnull().all(axis = 1)].index[1]
    col1limit = emptyrow1 - 1
    col3limit = emptyrow2 - 1
    startrow3 = emptyrow1 + 2
    col1 = df1['Time [min]']
    col2 = df1['Intensity [counts]']
    col3 = ['Baseline']
    newcol1 = col1[1:col1limit]
    newcol2 = col2[1:col1limit]
    newcol3 = col1[startrow3:col3limit]
    df2 = newcol1.to_frame()
    df3 = newcol2.to_frame()
    df4 = newcol3.to_frame()
    df5 = df4.rename(columns={'Time [min]': 'Baseline'})
    df6 = df5.reset_index(drop=True)
    hstack1 = pd.concat([df6, df2, df3], axis = 1)
    hstack1.drop('Baseline', inplace = True, axis = 1)
    hstack2 = hstack1.iloc[1:]
    filename1len = len(filename1) - 4
    filename=os.path.basename(filename1)
    outputFileName = basePath + "/outputs/" + filename
    #plotHeading = filename1[:filename1len] + str('_')
    plotHeading=os.path.splitext(filename)[0]
    print (plotHeading)
    #imageFileName = filename1[:filename1len] + str('_') + str('.') + str('png')
    imageFileName=basePath+"/figures/"+plotHeading+".png"
    hstack2.to_csv(outputFileName, sep =',', encoding ='utf-8', index = False)
    x = hstack2.loc[:, 'Time [min]']
    y = hstack2.loc[:, 'Intensity [counts]']
    plt.title(plotHeading)
    figure1 = plt.plot(x, y, '-b', linewidth = 1)
    ticks = [1000, 2000, 3000, 4000, 5000]
    plt.xlabel('Time (min)')
    plt.ylabel('Total ion counts')
    plt.xticks(ticks)
#    figure_path = r"C:\Users\Win-8.1\Desktop\Desktop\golu\golu"
    plt.savefig(imageFileName)
#    plt.ioff()
#   plt.show()

