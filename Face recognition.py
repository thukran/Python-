#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().system('pip install opencv-python')


# In[1]:


import cv2


# In[2]:


img=cv2.imread('G:/Sessions/face.jpg')
fc=cv2.CascadeClassifier("G:/Sessions/haarcascade_frontalface_default.xml")

img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=fc.detectMultiScale(img_gray, scaleFactor=1.05, minNeighbors=5)
print(len(faces))
print(faces)


# In[3]:


import matplotlib.pyplot as plt


# In[4]:


plt.imshow(img)
plt.show()


# In[5]:


#fn=cv2.rectangle(img,(28,57),(28+145,57+145),(0,255,0),3)
fn=cv2.rectangle(img,(45,100),(45+145,100+145),(0,255,0),3)


# In[6]:


plt.imshow(fn)
plt.show()


# In[14]:


img=cv2.imread('G:/Sessions/faces.jpeg',0)
fc=cv2.CascadeClassifier("G:/Sessions/haarcascade_frontalface_default.xml")

#img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=fc.detectMultiScale(img, scaleFactor=1.15, minNeighbors=5)
print(len(faces))
#print(faces)


# In[21]:


img=cv2.imread('G:/Sessions/faces.jpeg',0)
fc=cv2.CascadeClassifier("G:/Sessions/haarcascade_frontalface_default.xml")

#img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=fc.detectMultiScale(img, scaleFactor=1.15, minNeighbors=5)
print(len(faces))
#print(faces)


# In[24]:


for x,y,w,h in faces:
 im2=cv2.rectangle(img,(x,y), (x+w,y+h),(0,255,0),3)


# In[25]:


plt.imshow(im2)
plt.show()


# In[ ]:




