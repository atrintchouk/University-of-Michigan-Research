# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 22:46:33 2024

@author: griff
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
numbergoodbackup
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 12:52:43 2024

@author: alexatr
"""
import os
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import math

csvpath='E:/griff/UMichigan/'
csvname='CLEAR_SEP_Benchmark_Dataset_V1.xlsx - WLiu.csv'

csvdf = pd.read_csv(csvpath+csvname)
column_data = csvdf['SEP: Onset Time (Ep>10 MeV)']
datelist = csvdf['SEP: Onset Time (Ep>10 MeV)'].tolist()
eventdates=[]
for date in datelist:
    if date >= '2010/03/08/14:45' and '2017/09/10/16:25' >= date:
        date_str = date
        formatted_date = pd.to_datetime(date_str).strftime("%m/%d/%Y  %H:%M:%S")
        eventdates.append(formatted_date)

folders=['2010','2011','2012','2013','2014','2015','2016','2017']
months=['01','02','03','04','05','06','07','08','09','10','11','12']
years=0
monthcaller=0

fils=[]
paths=[]
datapath='E:/griff/UMichigan/data/'
for year in folders:
    yearpath = datapath + year
    monthcaller=0
    for month in months:
        datecaller=0
        for filename in os.listdir(yearpath +'/' + month):
            if ('5m' in filename and 'g13' in filename and filename.endswith('.csv') and 'epead' in filename and 'a16' in filename and '_epead_a16ew_5m_20110101_20110131.csv' not in filename and '_epead_a16ew_5m_20130501_20130531.csv' not in filename and '_epead_a16ew_5m_20141201_20141231.csv' not in filename 
            #or '5m' in filename and 'g13' in filename and filename.endswith('.csv') and 'epead' in filename and 'a16' in filename and '_epead_a16ew_5m_20140101_20141231.csv' not in filename 
            #or'5m' in filename and 'g13' in filename and filename.endswith('.csv') and 'epead' in filename and 'a16' in filename and '_epead_a16ew_5m_20130501_20130531.csv' not in filename  
            or '5m' in filename and 'g15' in filename and filename.endswith('.csv') and 'epead' in filename and 'a16' in filename and '_epead_a16ew_5m_20110101_20110131.csv' in filename
            or '5m' in filename and 'g15' in filename and filename.endswith('.csv') and 'epead' in filename and 'a16' in filename and '_epead_a16ew_5m_20141201_20141231.csv' in filename
            or '5m' in filename and 'g15' in filename and filename.endswith('.csv') and 'epead' in filename and 'a16' in filename and '_epead_a16ew_5m_20130501_20130531.csv' in filename): 
                file_path = os.path.join(yearpath+'/'+month, filename)
                fils.append(filename)
                paths.append(yearpath+'/' + month + '/' + filename)
                # Read the CSV file
                
                datecallser=datecaller+1
                #print(os.path.join(datapath+folders[years]+'/'+months[monthcaller], filename))
       # print(monthcaller)        
        monthcaller=monthcaller+1
        if monthcaller==12:
            break
        
    years=years+1
    if years==8:
        break





caller2=0
caller=0
columns = [
    'A1W_FLUX', 'A2W_FLUX',
    'A3W_FLUX', 'A4W_FLUX',
    'A5W_FLUX', 'A6W_FLUX'
]
c0='Event Start Time'
c1='Background: '+columns[0]
c2='Background: '+columns[1]
c3='Background: '+columns[2]
c4='Background: '+columns[3]
c5='Background: '+columns[4]
c6='Background: '+columns[5]
c7='Event and Peak intensity: '+columns[0]
c8='Event and Peak intensity: '+columns[1]
c9='Event and Peak intensity: '+columns[2]
c10='Event and Peak intensity: '+columns[3]
c11='Event and Peak intensity: '+columns[4]
c12='Event and Peak intensity: '+columns[5]
c=[c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12]
df = pd.DataFrame({
    c0: [None] * 115,
    c1: [None] * 115,
    c2: [None] * 115,
    c3: [None] * 115,
    c4: [None] * 115,
    c5: [None] * 115,
    c6: [None] * 115,
    c7: [None] * 115,
    c8: [None] * 115,
    c9: [None] * 115,
    c10: [None] * 115,
    c11: [None] * 115,
    c12: [None] * 115
    
    })
Dataframes={}
day=datetime.timedelta(days=1)
hour=datetime.timedelta(hours=1)
def getbg0(date):
    date_object = datetime.datetime.strptime(date, "%m/%d/%Y  %H:%M:%S")
    bgstartdate=date_object-day
    return bgstartdate
def getbg1(date):
    date_object = datetime.datetime.strptime(date, "%m/%d/%Y  %H:%M:%S")
    bgenddate=date_object-hour
    return bgenddate
def getevent0(date):
    date_object = datetime.datetime.strptime(date, "%m/%d/%Y  %H:%M:%S")
    eventstartdate=date_object-hour
    return eventstartdate
def getevent1(date):
    date_object = datetime.datetime.strptime(date, "%m/%d/%Y  %H:%M:%S")
    eventenddate=date_object+day+day+day
    return eventenddate

save_directory = 'E:/griff/UMichigan/FluxPlots'
if not os.path.exists(save_directory):
    os.makedirs(save_directory)
    
# Ensure the directory exists
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

'''Event Start Loop'''
aa=0
for eventdate in eventdates:
    df.iat[aa, 0] = eventdates[aa]        
    aa=aa+1  
        
'''Dataframe Maker Loop'''
def finddata(path):

    f=open(path)
    count=0
    
    while(True):
        
        line=f.readline()
        if line.find('time_tag,')>-1:
            
            break
        count=count+1
        
    f.close()
    
    df = pd.read_csv(path, header=count, 
                     parse_dates=[0], skip_blank_lines=False 
                     )
    
    #print('Dataframe starts at: Line '+str(count)+'\n')
    #print(df)
    return df
for path in paths:
    path=paths[caller2]
    
    
    #Create the new dataframes to use'
    
    
    #print('Filename:'+file)
    dfs=finddata(path)
                #dfs
    Dataframes[os.path.basename(path)] = dfs
    
    caller2=caller2+1
          
callerflux=0

eventfiles=[]
#Make one plot only(15 looks good)
#eventdates=[eventdates[15]]


'''Flux Loop'''
for eventdate in eventdates:        
    if callerflux!=85:
        print(str(getbg0(eventdates[callerflux])))
        print(str(getbg1(eventdates[callerflux])))
        print(str(getevent0(eventdates[callerflux])))
        print(str(getevent1(eventdates[callerflux])))
        
        monthvalue=eventdates[callerflux].split('/', 1)[0]
        if len(monthvalue)<2:
            monthvalue='0'+monthvalue
        if len(eventdates[callerflux])==18:
            yearvalue=eventdates[callerflux][4:8]
        elif len(eventdates[callerflux])==19:
            yearvalue=eventdates[callerflux][5:9]
        elif len(eventdates[callerflux])==20:
            yearvalue=eventdates[callerflux][6:10]
        goodfile = None
        for file in fils:
            if '_epead_a16ew_5m_'+yearvalue+monthvalue+'01' in file:
                goodfile=file
        if goodfile is None:
            print(f'file not found ffor {eventdates[callerflux]}')
        if monthvalue==getbg0(eventdate).strftime('%m'):   
            file1=Dataframes[goodfile]
        else:
            earlymonthvalue=str(int(monthvalue)-1)
            if len(earlymonthvalue)<2:
                earlymonthvalue='0'+earlymonthvalue
            for fix in fils:
                if '_epead_a16ew_5m_'+yearvalue+earlymonthvalue+'01' in fix:
                    earlymonthfile=fix
            file1=pd.concat([Dataframes[earlymonthfile], Dataframes[goodfile]],ignore_index=True)    
        #print('callerflux='+str(callerflux))
        
        bg0_dt = getbg0(eventdates[callerflux])
        bg1_dt = getbg1(eventdates[callerflux])
    
        # Ensure the column you're searching is in datetime format
        file1.iloc[:, 0] = pd.to_datetime(file1.iloc[:, 0])
    
        file1flux = file1[['time_tag'] + columns].copy()
        #Remove the outliers -99999, caused by sensor error
        file1flux.replace(-99999, pd.NA, inplace=True)
        file1flux.dropna(inplace=True)
            # Find indexes where the datetime values match
        indexes_bg0 = file1flux.index[file1flux.iloc[:, 0] == bg0_dt].tolist()
        indexes_bg1 = file1flux.index[file1flux.iloc[:, 0] == bg1_dt].tolist()
    
        # Convert indexes to comma-separated strings if needed (for display or debugging)
        indexes_bg0_str = ', '.join(map(str, indexes_bg0))
        indexes_bg1_str = ', '.join(map(str, indexes_bg1))
        
        print("Indexes of bg0:", indexes_bg0_str)
        print("Indexes of bg1:", indexes_bg1_str)
        
        file1flux = file1flux[columns+['time_tag']]
        # Use the indexes to select the range of rows from the DataFrame
        # Assuming you want to slice between the first occurrence of bg0 and bg1
        
        if indexes_bg0 and indexes_bg1:
            eventcolumns = file1flux.loc[indexes_bg0[0]:indexes_bg1[0]]
        else:
            print("No matching dates found.")
        
        columns = [
            'A1W_FLUX', 'A2W_FLUX',
            'A3W_FLUX', 'A4W_FLUX',
            'A5W_FLUX', 'A6W_FLUX'
        ]
        #Creates a mask to remove -99999 values
        ybad=file1flux['A1W_FLUX']
        mask = ybad >= -2500
        x=file1flux['time_tag']
        #Assigns colors to each line
        colors=['red', 'blue', 'green', 'black', 'palevioletred', 'rebeccapurple']
        fluxcolumns=[]
        num=0
        #important
        
        #Creates the plot, title, labels
        
        
        #The y-value (heights) for the color coded avgs on the right side of the figure
        figs=[]
        #meanbgs=[]
        def F(x):
            return (1/7) * math.log10(x) + (5/7)
        
       
        
        fig=plt.figure(figsize=(10,6))
        ax = fig.add_subplot()
        title="Differential Flux vs Energy For "+str(getbg0(eventdates[callerflux]))+" to "+str(getbg1(eventdates[callerflux]))
        plt.title(title,fontsize=14)
        plt.xlabel('Energy Channel [MeV]',fontsize=14,labelpad=15)  
        plt.ylabel('Differential Flux [counts/(cm$^2$ s sr MeV)]',fontsize=14)
        #Types '.Avg' in the top right of the figure
        plt.text(1.06,1,'Max.\nAvg.',transform=ax.transAxes,va='center',ha='center',fontsize=14)
        #The y-value (heights) for the color coded avgs on the right side of the figure
        #masks0 removes counts less than 0
        
        
        mask0=file1flux[columns[num]][mask]>0
        #meanbg="%12.8e"%eventcolumns[columns[num]][mask][mask0].mean()
        
        #Plots the x time data and the y flux datas
        num85=0
        MeVs=[6.9,16.1,41.2,120,210,435]
        for item in columns:
            
            plt.plot(MeVs[num85], file1flux[columns[num85]][mask][mask0].max(), marker='*', linestyle='-', color=colors[num85])        
            plt.plot(MeVs[num85], file1flux[columns[num85]][mask][mask0].mean(), marker='.', linestyle='-', color=colors[num85])        
            max_values=[]
            max_value = file1flux[columns[num85]][mask][mask0].max()
            
            if num85<4:
                plt.text(1.06,F(max_value),   '%.2e'%(max_value)+'\n'+'%.2e'%(eventcolumns[columns[num85]][mask][mask0].mean()),transform=ax.transAxes,ha='center',va='center',color=colors[num85],fontsize=14)
            else:
                plt.text(1.06,F(max_value),   '%.2e'%(max_value)+'\n'+'%.2e'%(eventcolumns[columns[num85]][mask][mask0].mean()),transform=ax.transAxes,ha='center',va='center',color=colors[num85],fontsize=14)
            num85=num85+1
       
        #Places ticks on axes, limits x axis to the background, limits y axis to 1.0E-5, 1.0E0
        '''xticks = range(len(columns))  # Set x-ticks at positions corresponding to each column
        ax.set_xticks(xticks)'''
        
        # Create custom labels combining column names and MeVs values
        '''custom_labels = [f'{col}\n{MeVs[i]} MeV' for i, col in enumerate(columns)]
        ax.set_xticklabels(custom_labels)'''
        '''plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M\n%d-%m'))
        plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=3))
        plt.gca().xaxis.set_minor_locator(mdates.MinuteLocator(interval=5))
        plt.xlim(pd.Timestamp(str(getbg0(eventdates[callerflux]))), pd.Timestamp(str(getbg1(eventdates[callerflux]))))'''
        plt.ylim(1.0E-5, 1.0E2)
        plt.xlim(1,1.0E3)
        #ax.set_xticklabels
        #plt.set_xticklabels
        num33=0
        xlabels=[]
        for value in columns:
            
            label=str(value)+'\n'+str(MeVs[num33])+' MeV'
            xlabels.append(label)
            num33=num33+1
        plt.xticks(ticks=MeVs, labels=xlabels)
        
        #ax.set_xticks(ticks=[10e0,10e1,10e2])
        #Plots on a logarithmic scale
        plt.yscale('log')
        plt.xscale('log')
        
        plt.xticks(ticks=MeVs+[1,1.0E3], labels=xlabels+[1,1.0E3])
        plt.yticks(fontsize=14)
        plt.subplots_adjust(left=0.09, bottom=.15,top=.94)
        figs.append(fig)
        #meanbgs.append(meanbg)
        
        
        file_path = os.path.join(save_directory+'/'+title.replace(':','_')+'.png')
    
        # Save the plot to the specified directory
        plt.savefig(file_path)
    
        # Close the plot to avoid keeping it open
        plt.close()
        num=num+1
              
                
                
                
        '''vv=1
        for column in columns:
                df.iat[callerflux, vv] = meanbgs[vv-1]        
                vv=vv+1'''
    callerflux=callerflux+1
    
#Save dataframe to Excel
'''file_name = str(len(eventdates))+'Backgrounds+Events.xlsx'
# saving the excel
df.to_excel(file_name)
print('DataFrame is written to Excel File successfully.') '''





