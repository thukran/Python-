#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


#1. Import the data in environment from link 
df=pd.read_excel('http://www.gddatalabs.com/Tests/Call_Centre.xlsx')
df.head(1)


# In[3]:


df.drop('Column1',1,inplace=True)
df.head(1)


# In[4]:


df.columns


# In[5]:


df.columns=['CallId', 'Date', 'Agent', 'Department', 'Answered_Y_N', 'Resolved',
            'Speed_of_Answer', 'AvgTalkDuration', 'Satisfaction_rating']


# In[6]:


df.head(1)


# In[7]:


#2. Make a function to accept the week number and share the below mentioned values of respective  week number. 
#weekly distribution
df['weeks']=df['Date'].dt.week
df.head(1)


# In[8]:


df['Calls']=1


# In[9]:


def getduration(val):
    val=str(val)
    du=0
    try:
        tm=val.split(':')
        du=float(tm[0])*3600+float(tm[1])*60+float(tm[2])
    except:
        du=0
    return du


# In[10]:


df['Total_Second']=df['AvgTalkDuration'].map(getduration)
df.head(1)


# In[11]:


week=1
#matching df
dt=df[df['weeks']==week]

#Total calls
tc=dt['Calls'].sum()
print('Total Calls', tc)

#Total Answer Calls
ac=dt[dt['Answered_Y_N']=='Y']['Calls'].sum()
print('Answered Calls', ac)

#Avg Speed of Answer
av=round(dt['Speed_of_Answer'].mean())
print('Avg Speed of Answer',av)

#Abandon Rate
ar=tc-ac
print('Abandon Rate',round((ar/tc)*100))

#Satisfaction Overall
csat=dt['Satisfaction_rating'].mean()
print('Satisfaction Overall',csat)

#Calls of Less than 180 Seconds
c1=dt[dt['Total_Second']>180]['Calls'].sum()
print('Calls Less than 180 Sec. ', c1)

#% Calls of Less than 180 Seconds
print('% Calls of Less than 180 Seconds ',
     round(c1/dt['Calls'].sum()*100))

#Satisfaction less than equal to 3
acdf=dt[dt['Answered_Y_N']=='Y']
print('Satisfaction less than equal to 3  :' ,
      acdf[acdf['Satisfaction_rating']<=3]['Calls'].count())


# In[12]:


def getweekPerformance(week):
    print('Week Performance for week No. ', week)
    print("-------------------")
    #week=1
    #matching df
    dt=df[df['weeks']==week]

    #Total calls
    tc=dt['Calls'].sum()
    print('Total Calls', tc)

    #Total Answer Calls
    ac=dt[dt['Answered_Y_N']=='Y']['Calls'].sum()
    print('Answered Calls', ac)

    #Avg Speed of Answer
    av=round(dt['Speed_of_Answer'].mean())
    print('Avg Speed of Answer',av)

    #Abandon Rate
    ar=tc-ac
    print('Abandon Rate',round((ar/tc)*100))

    #Satisfaction Overall
    csat=dt['Satisfaction_rating'].mean()
    print('Satisfaction Overall',csat)

    #Calls of Less than 180 Seconds
    c1=dt[dt['Total_Second']>180]['Calls'].sum()
    print('Calls Less than 180 Sec. ', c1)

    #% Calls of Less than 180 Seconds
    print('% Calls of Less than 180 Seconds ',
         round(c1/dt['Calls'].sum()*100))

    #Satisfaction less than equal to 3
    acdf=dt[dt['Answered_Y_N']=='Y']
    print('Satisfaction less than equal to 3  :' ,
          acdf[acdf['Satisfaction_rating']<=3]['Calls'].count())


# In[13]:


getweekPerformance(3)


# In[14]:


df['weeks'].value_counts()


# In[15]:


df.head(1)


# In[16]:


#3. Make a function to accept agent name and get the below mentioned values of respective agent

def getAgentperformance(agent):
    print('Agent Performance for ',agent)
    print("---------")
    dt=df[df['Agent']==agent]
    
    tc=dt['Calls'].sum()
    ac=dt[dt['Answered_Y_N']=='Y']['Calls'].sum()    
    asp=dt['Speed_of_Answer'].mean()
    rc=dt[dt['Resolved']=='Y']['Calls'].sum()
    rcp=round(rc/ac*100)
    
    df1=pd.DataFrame({'Total Calls':[tc],
                 'Calls Answered':[ac],
                 'Avg Speed of Answer':[asp],
                 'Call Resolution %':[rcp],
                 'Call Resolved':[rc]})
    return df1


# In[17]:


df['Agent'].unique()


# In[18]:


getAgentperformance('Diane')


# In[19]:


dir(df['Date'].dt)


# In[20]:


#4. Make a function to accept agent name and get the day (weekday) wise below mentioned values.  
df['Dayname']=df['Date'].dt.weekday
df.head(1)


# In[21]:


def getAgentWeekdayPerformance (agent):
    print('Agent Performance Details for ', agent)
    dt=df[df['Agent']==agent]
    
    #Total Calls 
    srtc=dt.groupby('Dayname')['Calls'].sum()
    
    #Answer Calls
    srac= dt[dt['Answered_Y_N']=='Y'].groupby('Dayname')['Calls'].sum()
    
    #Avg Speed of Answer 
    srsp=dt.groupby('Dayname')['Speed_of_Answer'].mean()
    
    #Call Resolved
    srrc=dt[dt['Resolved']=='Y'].groupby('Dayname')['Calls'].sum()
    
    df1=pd.DataFrame({'Total Calls':srtc,
                     'Answer Calls':srac,
                     'Avg Speed of Answer':srsp,
                     'Calls Resolved':srrc})
    df1['Call Resolved %']= df1['Calls Resolved']/df1['Total Calls']*100
    
    return df1


# In[22]:


getAgentWeekdayPerformance ('Becky')


# In[23]:


#5. Make a function to accept the department name and get below mentioned values 
def getdepartmentPerformance (dept):
    print('Department wise Performance ', dept)
    dt=df[df['Department']==dept]
    
    tc=dt['Calls'].sum()
    ac=dt[dt['Answered_Y_N']=='Y']['Calls'].sum()    
    asp=dt['Speed_of_Answer'].mean()
    rc=dt[dt['Resolved']=='Y']['Calls'].sum()
    rcp=round(rc/ac*100)
    
    df1=pd.DataFrame({'Total Calls': [tc],'Answer Calls': [ac], 'Avg Speed of Answer' : [asp], 'Calls Resolved': [rc],
                     'Call Resolved %': rcp})
    return df1


# In[24]:


df.Department.unique()
#getdepartmentPerformance ()


# In[25]:


getdepartmentPerformance ('Washing Machine')


# In[26]:


#6 Make a function to accept the department name and get below mentioned values
def getdepartmentPerformance (dept):
    print('Department wise Performance ', dept)
    dt=df[df['Department']==dept]
    
    tc=dt['Calls'].sum()
    ac=dt[dt['Answered_Y_N']=='Y']['Calls'].sum()
#abondoned call %
    mc=tc-ac
    mcp= round(mc/tc*100)
#SLA Limit (only 20% Abandoned Called Permitted)
    sla_sts=""
    if mcp>20:
        sla_sts="SLA Breached.(Yes)"
    else:
        sla_sts="SLA Breached.(No)"
        
    df1=pd.DataFrame({'Total Calls':[tc],
                     'Answered Calls ':[ac],
                     'Abandoned Calls %':[mcp],
                     'SLA Breached(Yes/No)':[sla_sts]})
    
    return df1


# In[27]:


getdepartmentPerformance ('Washing Machine')


# In[28]:


from ipywidgets import interact


# In[29]:


interact(getdepartmentPerformance, dept=df['Department'].unique())


# In[30]:


#7 All Agent reports
def getallAgentPerformance ():
    
    #Total Calls 
    srtc=dt.groupby('Agent')['Calls'].sum()
    
    #Answer Calls
    srac= dt[dt['Answered_Y_N']=='Y'].groupby('Agent')['Calls'].sum()
    
    #Avg Speed of Answer 
    srsp=dt.groupby('Agent')['Speed_of_Answer'].mean()
    
    #Call Resolved
    srrc=dt[dt['Resolved']=='Y'].groupby('Agent')['Calls'].sum()
    
    df1=pd.DataFrame({'Total Calls':srtc,
                     'Call Answered':srac,
                     'Avg Speed of Answer':srsp,
                     'Calls Resolved':srrc})
    df1['Call Resolved %']= df1['Calls Resolved']/df1['Total Calls']*100
    
    return df1


# In[31]:


getallAgentPerformance ()


# In[32]:


def sortdf(clm):
    df2=getallAgentPerformance()
    df2.sort_values(by=clm, inplace=True)
    return df2


# In[33]:


sortdf('Total Calls')


# In[34]:


interact(sortdf, clm=getallAgentPerformance().columns)


# In[35]:


#Abondon rate wise department
def getalldepartPerformance():
    #total calls
    srtc=df.groupby(['Department'])['Calls'].sum()
    
    #answer calls
    srac=df[df['Answered_Y_N']=='Y'].groupby(['Department'])['Calls'].sum()
  
    
    df1=pd.DataFrame({'Total Calls':srtc,
                     'Answered Calls':srac})
    
    df1['Abandon Rate']=(df1['Total Calls']-df1['Answered Calls'])/df1['Total Calls']*100
    
    df1['Abandon Rate']=df1['Abandon Rate'].map(round)
    return df1


# In[36]:


df2=getalldepartPerformance()


# In[37]:


df2['SLA_Rate']=20
df2


# In[38]:


dttop=df2.sort_values(by='Abandon Rate', ascending=False).head(1)
dttop


# In[42]:


plt.rcParams['figure.figsize'][0]=10
plt.bar(df2.index, df2['Abandon Rate'], label='Abandon Rate')
plt.plot(df2.index, df2['SLA_Rate'], '--', label='SLA Rate', color='green')
for i in range(5):
    plt.annotate(xy=[df2.index[i], df2['Abandon Rate'][i]+2],
                s=str(df2['Abandon Rate'][i])+" %")


plt.bar(dttop.index, dttop['Abandon Rate'], color='red')
plt.legend()
plt.xlabel('Department')
plt.ylabel('Abandon Rate %')
plt.ylim(0,30)
plt.show()


# In[ ]:


#Agent wise rating- 1st way by calling function----
def getallAgentPerformance():
    
    sra=dt.groupby('Agent')['Satisfaction_rating'].mean()
    
    df1=pd.DataFrame({'Satisfaction_rating':sra})

    return df1
# Second way 
#sr=df.groupby(['Agent'])['Satisfaction_Rating'].mean().sort_values()
#sr


# In[ ]:


getallAgentPerformance()


# In[ ]:


df2=getallAgentPerformance()


# In[ ]:


df3=df2['Satisfaction_rating'].mean()
df3


# In[41]:


import matplotlib.pyplot as plt


# In[ ]:


df2.index


# In[ ]:


[df3]*5


# In[ ]:


plt.barh(df2.index, df2['Satisfaction_rating'], label='Satisfaction_rating')
plt.plot([df3]*8,df2.index,  '--', label='Target', color='red')
plt.legend()
plt.xlabel('Satisfaction_rating')
plt.ylabel('Agent')
plt.xlim(0,5)
plt.show()


# In[40]:


#Performance Meter for Satisfaction of Rating
import plotly.graph_objects as go
sat_rate=df['Satisfaction_rating'].mean()

fig = go.Figure(go.Indicator(
    domain = {'x': [0, .5], 'y': [0,.5]},
    value = sat_rate,
    mode = "gauge+number+delta",
    title = {'text': "Satisfaction Ratings"},
    delta = {'reference': 3},
    gauge = {'axis': {'range': [None, 5]},
             'steps' : [
                 {'range': [0, 2.5], 'color': "red"},
                 {'range': [2.5, 3.5], 'color': "orange"}],
             'threshold' : {'line': {'color': "blue", 'width': 2}, 'thickness': .95, 'value': 2.45}}))

fig.show()


# In[ ]:




