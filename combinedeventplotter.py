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



save_directory = 'E:/griff/UMichigan/EventPlots'
if not os.path.exists(save_directory):
    os.makedirs(save_directory)
    
# Ensure the directory exists
if not os.path.exists(save_directory):
    os.makedirs(save_directory)


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
'''Event Start Loop'''
aa=0
for eventdate in eventdates:
    df.iat[aa, 0] = eventdates[aa]        
    aa=aa+1  
        
'''Dataframe Maker Loop'''

for path in paths:
    path=paths[caller2]
    pathR=path
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
    #Create the new dataframes to use'
    
    
    #print('Filename:'+file)
    dfs=finddata(path)
                #dfs
    Dataframes[os.path.basename(path)] = dfs
    
    caller2=caller2+1
          
callerevent=0

eventfiles=[]
#Make one plot only(15 looks good)
#eventdates=[eventdates[15]]

for eventdate in eventdates:        
    if callerevent!=45 and callerevent!=47 and callerevent!=60:
        print(str(getbg0(eventdates[callerevent])))
        print(str(getbg1(eventdates[callerevent])))
        print(str(getevent0(eventdates[callerevent])))
        print(str(getevent1(eventdates[callerevent])))
        
        monthvalue=eventdates[callerevent].split('/', 1)[0]
        if len(monthvalue)<2:
            monthvalue='0'+monthvalue
        if len(eventdates[callerevent])==18:
            yearvalue=eventdates[callerevent][4:8]
        elif len(eventdates[callerevent])==19:
            yearvalue=eventdates[callerevent][5:9]
        elif len(eventdates[callerevent])==20:
            yearvalue=eventdates[callerevent][6:10]
        goodfile = None
        for file in fils:
            if '_epead_a16ew_5m_'+yearvalue+monthvalue+'01' in file:
                goodfile=file
        if goodfile is None:
            print(f'file not found ffor {eventdates[callerevent]}')
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
        #print('callerevent='+str(callerevent))
        
        bg0_dt = getbg0(eventdates[callerevent])
        event1_dt = getevent1(eventdates[callerevent])
    
        # Ensure the column you're searching is in datetime format
        file1.iloc[:, 0] = pd.to_datetime(file1.iloc[:, 0])
    
        file1flux = file1[['time_tag'] + columns].copy()
        #Remove the outliers -99999, caused by sensor error
        file1flux.replace(-99999, pd.NA, inplace=True)
        file1flux.dropna(inplace=True)
            # Find indexes where the datetime values match
        indexes_bg0 = file1flux.index[file1flux.iloc[:, 0] == bg0_dt].tolist()
        indexes_event1 = file1flux.index[file1flux.iloc[:, 0] == event1_dt].tolist()
    
        # Convert indexes to comma-separated strings if needed (for display or debugging)
        indexes_bg0_str = ', '.join(map(str, indexes_bg0))
        indexes_event1_str = ', '.join(map(str, indexes_event1))
        
        print("Indexes of bg0:", indexes_bg0_str)
        print("Indexes of event1:", indexes_event1_str)
        
        bg0_dt = getbg0(eventdates[callerevent])
        bg1_dt = getbg1(eventdates[callerevent])
    
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
        
        if indexes_bg0 and indexes_bg1:
            bgcolumns = file1flux.loc[indexes_bg0[0]:indexes_bg1[0]]
        else:
            print("No matching dates found.bg")
        
        file1flux = file1flux[columns+['time_tag']]
        # Use the indexes to select the range of rows from the DataFrame
        # Assuming you want to slice between the first occurrence of bg0 and bg1
        
        if indexes_bg0 and indexes_event1:
            eventcolumns = file1flux.loc[indexes_bg0[0]:indexes_event1[0]]
        else:
            print("No matching dates found.event")
        
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
        meanbgs=[]
        def F(x):
            return (1/7) * math.log10(x) + (5/7)
        fig=plt.figure(figsize=(10,6))
        ax = fig.add_subplot()
        plt.axvspan(pd.Timestamp(str(getbg0(eventdates[callerevent]))), pd.Timestamp(str(getbg1(eventdates[callerevent]))), color='yellow', alpha=0.5)
        plt.axvspan(pd.Timestamp(str(getevent0(eventdates[callerevent]))), pd.Timestamp(str(getevent1(eventdates[callerevent]))), color='orange', alpha=0.5)
        plt.text(1.06,1,'Max.',transform=ax.transAxes,va='center',ha='center',fontsize=14)
        for item in file1.columns:
            if 'W_FLUX' in item:
                
                title="Differential Flux vs Time From "+str(getbg0(eventdates[callerevent]))+" to "+str(getevent1(eventdates[callerevent]))
                plt.title(title,fontsize=14)
                plt.xlabel('Time Tag [Time/Date]',fontsize=14,labelpad=15)  
                plt.ylabel('Differential Flux [counts/(cm$^2$ s sr MeV)]',fontsize=14)
                #Types '.Avg' in the top right of the figure
                
                #The y-value (heights) for the color coded avgs on the right side of the figure
                #masks0 removes counts less than 0
                
                
                mask0=file1flux[columns[num]][mask]>0
                meanbg="%12.8e"%eventcolumns[columns[num]][mask][mask0].mean()
                
                #Plots the x time data and the y flux datas
                plt.plot(x[mask][mask0], file1flux[columns[num]][mask][mask0], label=item, marker='.', linestyle='-', color=colors[num])
                max_values=[]
                max_value = eventcolumns[columns[num]][mask][mask0].max()
                max_date = eventcolumns.loc[file1[columns[num]] == max_value, 'time_tag'].values[0]
                if num<4:
                    plt.text(1.06,F(max_value),   '%.2e'%(max_value),transform=ax.transAxes,ha='center',va='center',color=colors[num],fontsize=14)
                else:
                    plt.text(1.06,F(max_value),   '%.2e'%(max_value),transform=ax.transAxes,ha='center',va='center',color=colors[num],fontsize=14)
                
                
                # Print debug info
                print(f"Column: {columns[num]}, Max Value: {max_value}, Max Date: {max_date}")
                max_values.append(max_value)
                plt.scatter(max_date, max_value, color=colors[num], marker='*', s=350,zorder=5)
                #Places ticks on axes, limits x axis to the background, limits y axis to 1.0E-5, 1.0E0
                
                plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M\n%d-%m'))
                plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=6))
                plt.gca().xaxis.set_minor_locator(mdates.MinuteLocator(interval=10))
                plt.xlim(pd.Timestamp(str(getbg0(eventdates[callerevent]))), pd.Timestamp(str(getevent1(eventdates[callerevent]))))
                plt.ylim(1.0E-5, 1.0E2)
                
                #Plots on a logarithmic scale
                plt.yscale('log')
                #plt.yticks(fontsize=14)
                plt.subplots_adjust(left=0.09, bottom=.15,top=.94)
                figs.append(fig)
                meanbgs.append(meanbg)
                num=num+1
        file_path = os.path.join(save_directory+'/'+title.replace(':','_')+'.png')
    
        # Save the plot to the specified directory
        plt.savefig(file_path)
    
        # Close the plot to avoid keeping it open
        plt.close()
    
            
            
    vv=1
    for column in columns:
            df.iat[callerevent, vv] = meanbgs[vv-1]        
            vv=vv+1
    callerevent=callerevent+1
    
    


'''file_name = str(len(eventdates))+'Backgrounds+Events.xlsx'
# saving the excel
df.to_excel(file_name)
print('DataFrame is written to Excel File successfully.')

'''
