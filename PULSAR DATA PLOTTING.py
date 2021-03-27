#!/usr/bin/env python
# coding: utf-8

# In[1]:


import astropy


# In[2]:


from astropy.io import ascii


# You can view database here: http://rian.kharkov.ua/decameter/EPN/browser.html

# In[3]:


url = 'http://rian.kharkov.ua/decameter/EPN/epndb/J0006+1834/cn95.epn.asc'


# In[4]:


psr1 = ascii.read(url,names=('Time','Data'), data_start= 2)


# In[5]:


psr1


# In[7]:


psr1.colnames


# In[10]:


psr1[0]


# In[9]:


psr1[-1]


# In[11]:


psr1[0:3]


# In[12]:


psr1['Time']


# In[13]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[22]:


plt.figure(figsize=(14,6))
plt.plot(psr1['Time'],psr1['Data'],'r')
plt.xlabel('Time(sec)')
plt.ylabel('Pulse Data')
plt.legend(['Integrated Profile'])
plt.show()


# In[30]:


url ='http://rian.kharkov.ua/decameter/EPN/epndb/B1929+10/gl98_1408.epn.asc'


# In[32]:


psr2 = ascii.read(url,names=('Time','I','Q','U','V'), data_start = 2)


# In[33]:


psr2


# In[38]:


plt.figure(figsize=(14,6))
plt.plot(psr2['Time'],psr2['I'],'r')
plt.grid()
plt.xlabel('Time(sec)')
plt.ylabel('Pulse Intensity')
plt.legend(['Integrated Profile'])
plt.title('Pulse Profile')
plt.show()


# In[42]:


import numpy as np


# In[43]:


linPol= np.sqrt(np.square(psr2['Q'])+np.square(psr2['U']))


# In[44]:


linPol


# In[93]:


get_ipython().run_line_magic('matplotlib', 'inline')
pulsar= 'B1929+10'
plt.figure(1,(20,20))


plt.subplot(3,1,1)
plt.plot(psr2['Time'],psr2['I'])
plt.plot(psr2['Time'],linPol,'r')
plt.plot(psr2['Time'], psr2['V'])
plt.legend(["Integrated Profile", "Linear Polarisation", "Circular Polarisation"])
plt.title('Profile for' + pulsar)
plt.show()

plt.figure(figsize=(20,20))
plt.subplot(3,1,2)
plt.plot(psr2['Time'],linPol,'r')
plt.title('Linear Polarisation of' + pulsar)
plt.show()

plt.figure(1,(20,20))
plt.subplot(3,1,3)
plt.plot(psr2['Time'], psr2['V'])
plt.plot(psr2['Time'], linPol)
plt.title('Linear and Circular Polarisation for '+pulsar)
plt.legend(['Circular Polarisation','Linear Polarisation'])
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




