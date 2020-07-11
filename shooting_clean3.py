# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 16:18:37 2020

@author: amasi
"""

import pandas as pd
import numpy as np

import datetime

download_dir = "E:\CACE\CSPO\Co-op\Aman\Shooting\\"
df = pd.read_csv(download_dir + 'shooting2.csv', encoding = 'latin-1')

df = df.replace(np.nan, '', regex=True)
x = 0
for nation in df['Nation']:
    if 'AUS' in nation:
        df.iloc[x,12] = 'AUS'
    elif 'AUT' in nation:
        df.iloc[x,12]= 'AUT'
    elif 'ARG' in nation:
        df.iloc[x,12] = 'ARG'
    x+=1
x=0
for nation in df['Nation']:
    df.iloc[x,12] = ''.join([i for i in nation if not i.isdigit()])
    x+=1
x=0
for nation in df['Nation']:
    if 'CZE' in nation:
        df.iloc[x,12]= 'CZE'
    elif 'GER' in nation:
        df.iloc[x,12]='GER'
    elif 'HUN' in nation:
        df.iloc[x,12]='HUN'
    elif 'JAPAN' in nation:
        df.iloc[x,12]='JPN'
    elif 'SVK' in nation:
        df.iloc[x,12]='SVK'
    elif nation == '':
        df.iloc[x,12]='UNK'
        
    x+=1

#This is where I calculate the final event rank
#CHanged the round types in excel...
df.to_csv(download_dir + 'shooting3.csv', index= False)
df1 = pd.read_excel(r'E:\CACE\CSPO\Co-op\Aman\Shooting\\shooting3.xlsx', encoding = 'latin-1')
del df1['Final_Event_Rank2']
del df1['Finals?']

df1['Final_Event_Rank'] = None
x= 0 
for var in df1['Round']:
    if var == 'Final':
        df1.iloc[x,33] = df1.iloc[x,14]
    x+=1
x=0
for rank in df1['Rank']:
    if rank == 'DNS' or rank == 'DSQ' or rank == '' or rank == 'DSQ DSQ' or rank == 'DNF' or rank =='A 4' or rank =='A 3' or rank =='A 2' or rank =='A 1':
        df1.iloc[x,33] = 9999
    x+=1
df1['Final_Event_Rank'].replace('None', np.nan, inplace=True)
df1['Final_Event_Rank']= pd.to_numeric(df1['Final_Event_Rank'])
df1['Final_Event_Rank'].replace(np.nan, 9999, inplace=True)
df1['Final_Event_Rank2'] = df1.groupby(['Competition', 'Date','Event Name','Name'])['Final_Event_Rank'].transform('min')
df1['Final_Event_Rank2'].replace(9999, '-', inplace= True)
 #FInals? Y if they make finals and N if they dont 
x=0
df1['Finals?'] = None
for rank in df1['Final_Event_Rank2']:
    if rank == '-':
        df1.iloc[x,35] = 'N'
    else:
        df1.iloc[x,35] = 'Y'
    x+=1
    
df1['Round'] = pd.Categorical(df1['Round'], ['QSO' ,'Qualification',' QF','SF','MSO', 'Final'])
df1.sort_values(['Date','Competition','Round','Name'], inplace= True)
df1['Final_Event_Rank_N'] = df1[df1['Finals?'] == 'N'].groupby(['Competition', 'Date','Event Name','Name'])['Rank'].transform('last')
df2 = df1.copy()
x=0
for rank in df2['Final_Event_Rank2']:
    if rank == '-':
        df2.iloc[x,34]= df2.iloc[x,36]
    x+=1 

#Dates 
df3 = df2.copy()
x=0
for dates in df3['Date']:
    df3.iloc[x,0]= datetime.datetime.strptime(dates,'%d.%m.%Y').date()
    x+=1 
df3.sort_values('Date',inplace= True)
df3 = df3.reset_index(drop= True)
#Country
x = 0 
for cou in df3['Country of Event']:
    if df3.iloc[x,1] == 'Gruppenmeisterschaftsfinal 300m':
        df3.iloc[x,2] = 'Switzerland'
    x+=1
    
x=0 
for cou in df3['Country of Event']:
    if cou == 'ALGERIA':
        df3.iloc[x,2] = 'Algeria'
    elif cou == 'AUS':
        df3.iloc[x,2] = 'Australia'
    elif cou == 'AUT':
        df3.iloc[x,2] = 'Austria'
    elif cou == 'AZE' or cou == 'Azerbajan' or cou == 'Azerbeijan':
        df3.iloc[x,2] = 'Azerbaijan'
    elif cou == 'BRA':
        df3.iloc[x,2] = 'Brazil'
    elif cou == 'CHN':
        df3.iloc[x,2] = 'China'
    elif cou == 'CRO':
        df3.iloc[x,2] = 'Croatia'
    elif cou == 'CYP':
        df3.iloc[x,2] = 'Cyprus'
    elif cou == 'ESP':
        df3.iloc[x,2] = 'Spain'
    elif cou == 'EST':
        df3.iloc[x,2] = 'Estonia'
    elif cou == 'GBR':
        df3.iloc[x,2] = 'Great Britain'
    elif cou =='GER':
        df3.iloc[x,2] = 'Germany'
    elif cou == 'HUN':
        df3.iloc[x,2] = 'Hungary'
    elif cou == 'IND':
        df3.iloc[x,2] = 'India'
    elif cou == 'IRI':
        df3.iloc[x,2] = 'Iran'
    elif cou == 'ITA':
        df3.iloc[x,2] = 'Italy'
    elif cou == 'JAPAN' or cou == 'JPN':
        df3.iloc[x,2] = 'Japan'
    elif cou == 'KOR':
        df3.iloc[x,2] = 'Korea'
    elif cou == 'KUW':
        df3.iloc[x,2] = 'Kuwait'
    elif cou == 'MEX':
        df3.iloc[x,2] = 'Mexico'
    elif cou == 'MLT':
        df3.iloc[x,2] = 'Malta'
    elif cou == 'NED':
        df3.iloc[x,2] = 'Netherlands'
    elif cou == 'POL':
        df3.iloc[x,2] = 'Poland'
    elif cou == 'QATAR':
        df3.iloc[x,2] = 'Qatar'
    elif cou == 'RUS':
        df3.iloc[x,2] = 'Russia'
    elif cou == 'SAN MARINO' or cou == 'SMR':
        df3.iloc[x,2] = 'San Marino'
    elif cou == 'SLO':
        df3.iloc[x,2] ='Slovenia'
    elif cou == 'THA':
        df3.iloc[x,2]= 'Thailand'
    elif cou == 'TPE':
        df3.iloc[x,2] = 'Taipei'
    elif cou == 'UAE':
        df3.iloc[x,2] = 'United Arab Emirates'
    elif cou == 'USA':
        df3.iloc[x,2] = 'United States'
    x+=1

#Gender (fixed it in excel) => put mixed in blanks
df3.to_csv(download_dir + 'shooting4.csv', index= False)

#Event type
df4 = pd.read_excel(r'E:\CACE\CSPO\Co-op\Aman\Shooting\\shooting4.xlsx', encoding = 'latin-1')
x = 0
df4['CompetitionSet'] = None
for comp in df4['Competition']:
    if comp == 'ISSF World Championship' or comp == '52nd ISSF World Championship' or comp == '51st ISSF World Championship' or comp == '2014 IPC Shooting World Championships':
        df4.iloc[x,37] = 'World Championship'
    elif ('WORLD CUP' in comp.upper()) and ('JUNIOR' not in comp.upper()):
        df4.iloc[x,37] = 'World Cup'
    else:
        df4.iloc[x,37] = 'Others'
    x+=1

#rearrange columns
df4.columns.tolist()
df4 = df4[['Date',
 'Competition',
 'CompetitionSet',
 'Country of Event',
 'Discipline',
 'Round',
 'Event Name',
 'Final Total',
 'Gender',
 'Grand Total',
 'Group',
 'Location',
 'Name',
 'Nation',
 'Range',
 'Rank',
 'Relay',
 'State/State',
 'Total',
 'Scores',
 'Score1',
 'Score2',
 'Score3',
 'Score4',
 'Score5',
 'Score6',
 'Score7',
 'Score8',
 'Score9',
 'Score10',
 'Score11',
 'Score12',
 'Score13',
 'Score14',
 'Final_Event_Rank',
 'Final_Event_Rank2',
 'Finals?',
 'Final_Event_Rank_N']]


del df4['Final_Event_Rank']
del df4['Final_Event_Rank_N']
df4 = df4.rename(columns ={'Final_Event_Rank2': 'Final_Event_Rank'})
df4.to_csv(download_dir + 'shooting4.csv', index= False)
#Age
df4 = pd.read_excel(r'E:\CACE\CSPO\Co-op\Aman\Shooting\\shooting4.xlsx', encoding = 'latin-1')
x=0
df4['Age']= None
for age in df4['Event Name']:
    if 'JUNIOR' in age.upper():
        df4.iloc[x,36] = 'Junior'
    elif 'YOUTH' in age.upper():
        df4.iloc[x,36] = 'Youth'
    else:
        df4.iloc[x,36] = 'Senior'
    x+=1
#delete groups column
df4.to_csv(download_dir + 'shooting5.csv', index= False)

#As of now para is in there too


df4 = pd.read_excel(r'E:\CACE\CSPO\Co-op\Aman\Shooting\\shooting5.xlsx', encoding = 'latin-1')
#New Discipline Variable

x = 0   
df4['Discipline2'] = None
df4['Oly_Discipline?'] =None
for disc in df4['Discipline']:
    if 'CIS' in disc.upper():
        df4.iloc[x,36] = df4.iloc[x,6]
    elif ('AR60' in disc.upper()) or ('AR40' in disc.upper()):
        if df4.iloc[x,8] == 'Women':
            df4.iloc[x,36] = "Women's 10 m air rifle"
            df4.iloc[x,37] = 'Y'
        elif df4.iloc[x,8] == 'Men':
            df4.iloc[x,36] = "Men's 10 m air rifle"
            df4.iloc[x,37] = 'Y'
        elif df4.iloc[x,8] == 'Mixed':
            df4.iloc[x,36] = 'Mixed 10 m air rifle team'
            df4.iloc[x,37] = 'Y'
    elif 'R3X40' in disc.upper():
        if 'FR3X40' in disc.upper():
            if '300FR3X40' in disc.upper():
                df4.iloc[x,36] = "Men's 300 m rifle 3 positions"
            else:
                df4.iloc[x,36] = "Men's 50 m rifle 3 positions"
                df4.iloc[x,37] = 'Y'
        else:
            if ('300R3X40' in disc.upper()) or ('300R3X20' in disc.upper()):
                df4.iloc[x,36] = "Women's 300 m rifle 3 positions"
            else:
                df4.iloc[x,36] = "Women's 50 m rifle 3 positions"
                df4.iloc[x,37] = 'Y'
    elif ('STR3X20' in disc.upper() and df4.iloc[x,8] == 'Women'):
        df4.iloc[x,36] = "Women's 50 m rifle 3 positions"
    elif ('AP60' in disc.upper()) or ('AP40' in disc.upper()):
        if df4.iloc[x,8] == 'Women':
            df4.iloc[x,36] = "Women's 10 air pistol"
            df4.iloc[x,37] = 'Y'
        elif df4.iloc[x,8] == 'Men':
            df4.iloc[x,36] = "Men's 10 air pistol"
            df4.iloc[x,37] = 'Y'
        elif df4.iloc[x,8] == 'Mixed':
            df4.iloc[x,36] = "Mixed 10 m air pistol team"
            df4.iloc[x,37] = 'Y'
    elif ('RFP' in disc.upper()):
        df4.iloc[x,36] = "Men's 25 m rapid fire pistol"
        df4.iloc[x,37] = 'Y'
    elif ('CFP' in disc.upper()):
        df4.iloc[x,36] = "Men's 25 m center fire pistol"
    elif ('SP' in disc.upper()):
        df4.iloc[x,36] = "Women's 25 m pistol"
        df4.iloc[x,37] = 'Y'
    elif ('TR125' in disc.upper()):
        if ('TR125W' in disc.upper()):
            df4.iloc[x,36] = "Women's Trap"
            df4.iloc[x,37] = 'Y'
        else:
            df4.iloc[x,36] = "Men's Trap"
            df4.iloc[x,37] = 'Y'
    elif ('TRMIX' in disc.upper()):
        df4.iloc[x,36] = "Mixed trap team"
        df4.iloc[x,37] = 'Y'
    elif ('Trap' in disc.upper()):
        df4.iloc[x,36] = "Mixed trap team"
        df4.iloc[x,37] = 'Y'
    elif ('SK125' in disc.upper()):
        if ('SK125W' in disc.upper()):
            df4.iloc[x,36] = "Women's Skeet"
            df4.iloc[x,37] = 'Y'
        else:
            df4.iloc[x,36] = "Men's Skeet"
            df4.iloc[x,37] = 'Y'
    elif ('Skeet' in disc.upper()):
        df4.iloc[x,36] = "Mixed Skeet team"
        df4.iloc[x,37] = 'Y'
    elif ('300STR3X20' in disc.upper()):
        df4.iloc[x,36] = "Men's 300 m Standard rifle"
    elif ('300FR60PR' in disc.upper()):
        df4.iloc[x,36] = "Men's 300 m rifle prone"
    elif ('300R60PR' in disc.upper()):
        df4.iloc[x,36] = "Women's 300 m rifle prone"
    elif ('FR60PR' in disc.upper()):
        df4.iloc[x,36] = "Men's 50 m rifle prone"
    elif ('STR60PR' in disc.upper()):
        df4.iloc[x,36] = "Women's 50 m rifle prone"
    elif ('FP' in disc.upper()) and ('RFP' not in disc.upper()) and ('CFP' not in disc.upper()):
        df4.iloc[x,36] = "Men's 50 m pistol"
    elif ('STP' in disc.upper()):
        df4.iloc[x,36] = "Men's 25 m standard pistol"
    elif ('DT150' in disc.upper()) or ('DT120' in disc.upper()):
        if df4.iloc[x,8] == "Women":
            df4.iloc[x,36] = "Women's Double trap"
        elif df4.iloc[x,8] == "Men":
            df4.iloc[x,36] = "Men's Double trap"
    elif ('50RT' in disc.upper()) and df4.iloc[x,8] == 'Men':
        df4.iloc[x,36] = "Men's 50 m running target"
    elif ('50RTMIX' in disc.upper()):
        df4.iloc[x,36] ="Men's 50m running target mixed"
    elif ('10RT' in disc.upper()) and df4.iloc[x,8] == "Women":
        df4.iloc[x,36] = "Women's 10 m running target"
    elif ('10RT' in disc.upper()) and df4.iloc[x,8] == "Men":
        df4.iloc[x,36] = "Men's 10 m running target" 
    else: 
        df4.iloc[x,36] = df4.iloc[x,6]
    
    x+=1    
df4['Oly_Discipline?'] = df4['Oly_Discipline?'].astype(str)
df4['Oly_Discipline?'].replace('None', 'N' , inplace =True)
df4.to_csv(download_dir + 'shooting6.csv', index= False)

#Country edits Round 2_with_john
df = pd.read_csv(download_dir + 'shooting6.csv', encoding = 'latin-1')
def fixCountryNames1(country):
    return str(country).replace(" ", "")
df['Nation'] = df['Nation'].apply(fixCountryNames1)
def fixCountryNames2(country):
    if str(country) in ['ACT', 'NCL', 'NSW', 'QLD', 'SA', 'VIC', 'WA']:
        return 'AUS'
    elif str(country) in ['ALS','AQU','ARQ', 'AUV', 'BFC', 'BOR', 'BOU', 'BRE', 'C-A', 'CEN', 'COR', 'DOU', 'D-S', 'ETR', 'F-C', 'GPF', 'IDF', 'INS', 'IRM', 'LIM', 'LOR', 'L-R', 'LYO', 'MID', 'MOP', 'M-P', 'NAN', 'NPC', 'OBJ', 'P-C','PDC','PDL','PIC','PRO', 'R-A','REU', 'STR', 'TOU', 'U-E', 'WAT']:
        return 'FRA'
    elif str(country) in ['ARA', 'AST','BAL', 'CAL','CAT','CNA','EXT', 'GAL', 'MEL', 'MUR', 'NAV', 'RIO', 'SMA', 'VAL', 'VAS']:
        return 'ESP'
    elif str(country) in ['BAV','GST', 'IRT', 'URI']:
        return 'SUI'
    elif str(country) in ['BAY', 'BY']:
        return 'GER'
    elif str(country) in ['ISP']:
        return 'IOC'
    elif str(country) in ['LEB']:
        return 'LBN'
    elif str(country) in ['MTQ']:
        return 'MEX'
    else:
        return str(country)
df['Nation'] = df['Nation'].apply(fixCountryNames2)

def fixFinalRank(Rank):
    if str(Rank) in ['A 1', 'A 2', 'A 3', 'A 4', 'DNF', 'DNS', 'DSQ', 'DSQ DSQ', 'nan']:
        return " "
    else:
        return str(Rank)
df['Final_Event_Rank'] = df['Final_Event_Rank'].apply(fixFinalRank)
df.to_csv(download_dir + 'shooting_fixed2.csv', index= False)

#ODF Edits here (thurs/fri)
df['SortOrder'] = None
df['IRM'] = None
x = 0
for ranks in df['Rank']:
    if ranks in ['DNF', 'DNS', 'DSQ', 'DSQ DSQ', 'A 1', 'A 2', 'A 3', 'A 4']:
        df.iloc[x,39] = df.iloc[x,14]
    else:
        df.iloc[x,39] = " "
    x+=1
df['Rank'] = df['Rank'].replace("DNF", np.nan, regex= True).replace("DNS", np.nan, regex=True).replace("DSQ", np.nan, regex=True).replace("DSQ DSQ", np.nan, regex= True).replace("A 1", np.nan, regex= True).replace("A 2", np.nan, regex= True).replace("A 3", np.nan, regex= True).replace("A 4", np.nan, regex= True)
df['Rank'] = pd.to_numeric(df['Rank'])

df.sort_values(by =['Date','Competition','Discipline','Round','Event Name','Gender', 'Rank'], ascending=True, inplace=True)
df['SortOrder'] = df.groupby(['Date','Competition','Discipline','Round','Event Name','Gender']).cumcount() +1

df.sort_values(by = ['Date'], ascending = False, inplace = True)
df = df.reset_index()    
del df['index']

def fixTime(times):
    temp = str(times)
    holder = temp.split(':')
    first = holder[0]
    last= holder[-1]
    Hour = first[-2:]
    Minute = last[0:2]
    return Hour + ':' + Minute
df['Time'] = df['State/State']
df['Time'] = df['Time'].apply(fixTime)

df.sort_values(by = ['Date', 'Discipline','Round', 'Event Name'], inplace= True)
df = df.reset_index()    
del df['index']


def fixGender(gen):
    if str(gen) == 'Men':
        return 'M'
    elif str(gen) == 'Women':
        return 'W'
    elif str(gen) == 'Mixed':
        return 'X'
    else:
        return str(gen)
df['Gender'] = df['Gender'].apply(fixGender)

df.to_csv(download_dir + 'shooting_fixed3.csv', index= False)





















