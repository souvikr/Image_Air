#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests


# In[ ]:


#NEW DELHI
from time import sleep
import datetime

while(1):
    try:
        x = datetime.datetime.now().strftime("%Y_%m_%d %H_%M")
        r=requests.get("https://g0.ipcamlive.com/player/player.php?alias=aqi02&autoplay=1&disabledownloadbutton=1&timelapseplayerenabled=0")
        data=r.text
        i1=data.index("address")
        i2=data.index("streamid")
        address=data[i1+11:i1+36]
        streamid=data[i2+12:i2+29]
        add=str(address+"streams/"+streamid+"/snapshot.jpg")

        response = requests.get(add, stream=True)
        #https://s15.ipcamlive.com/streams/0f5c811d70b81ea6a/snapshot.jpg
        #https://s15.ipcamlive.com/streams/0f5c80d5d89d699c9/snapshot.jpg
        # Throw an error for bad status codes
        response.raise_for_status()
        filename = x+".jpg"
        with open("NewDelhi/"+filename, 'wb') as handle:
            for block in response.iter_content(1024):
                handle.write(block)
        sleep(900)
    except:
        print("Camera is down, time: ",x)
        pass


# In[ ]:




