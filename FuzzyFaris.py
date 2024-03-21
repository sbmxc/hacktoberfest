#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import skfuzzy as fuzz
import matplotlib.pyp as plt


# In[5]:


import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt


# In[6]:


x_qual = np.arange(0,11,1)
x_serv = np.arange(0,11,1)
x_tip = np.arange(0,26,1)


# In[7]:


qual_lo = fuzz.trimf(x_qual, [0,0,5])
qual_md = fuzz.trimf(x_qual, [0,5,10])
qual_hi = fuzz.trimf(x_qual, [5,10,10])
serv_lo = fuzz.trimf(x_serv, [0,0,5])
serv_md = fuzz.trimf(x_serv, [0,5,10])
serv_hi = fuzz.trimf(x_serv, [5,10,10])
tip_lo = fuzz.trimf(x_tip, [0,0,5])
tip_md = fuzz.trimf(x_tip, [0,5,10])
tip_hi = fuzz.trimf(x_tip, [5,10,10])


# In[9]:


fig, (ax0,ax1,ax2) = plt.subplots(nrows=3, figsize=(8,9))

ax0.plot(x_qual, qual_lo, 'b', linewidth=1.5,label='Bad')
ax0.plot(x_qual, qual_md, 'b', linewidth=1.5,label='Decent')
ax0.plot(x_qual, qual_hi, 'b', linewidth=1.5,label='Great')
ax0.set_title('Food Quality')
ax0.legend()

ax0.plot(x_serv, serv_lo, 'b', linewidth=1.5,label='Poor')
ax0.plot(x_serv, serv_md, 'b', linewidth=1.5,label='Acceptable')
ax0.plot(x_serv, serv_hi, 'b', linewidth=1.5,label='Amazing')
ax0.set_title('Service Quality')
ax0.legend()

ax0.plot(x_tip, tip_lo, 'b', linewidth=1.5,label='Low')
ax0.plot(x_tip, tip_md, 'b', linewidth=1.5,label='Medium')
ax0.plot(x_tip, tip_hi, 'b', linewidth=1.5,label='High')
ax0.set_title('Tip Amount')
ax0.legend()

for ax in (ax0, ax1, ax2):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()


# In[13]:


print("PERCOBAAN 2")


# In[14]:


qual_level_lo = fuzz.interp_membership(x_qual, qual_lo, 6.5)
qual_level_md = fuzz.interp_membership(x_qual, qual_md, 6.5)
qual_level_hi = fuzz.interp_membership(x_qual, qual_hi, 6.5)

serv_level_lo = fuzz.interp_membership(x_serv, serv_lo, 9.8)
serv_level_md = fuzz.interp_membership(x_serv, serv_md, 9.8)
serv_level_hi = fuzz.interp_membership(x_serv, serv_hi, 9.8)


# In[16]:


active_rule1 = np.fmax(qual_level_lo, serv_level_lo)


# In[19]:


tip_activation_lo = np.fmin(active_rule1, tip_lo)


# In[20]:


tip_activation_md = np.fmin(serv_level_md, tip_md)


# In[22]:


active_rule3 = np.fmax(qual_level_hi, serv_level_hi)
tip_activation_hi = np.fmin(active_rule3, tip_hi)
tip0 = np.zeros_like(x_tip)


# In[28]:


fig,ax0 = plt.subplots(figsize=(8,3))

ax0.fill_between(x_tip, tip0, tip_activation_lo, facecolor = 'b', alpha=0.7)
ax0.plot(x_tip, tip_lo, 'b', linewidth=0.5, linestyle = '--',)

ax0.fill_between(x_tip, tip0, tip_activation_md, facecolor = 'g', alpha=0.7)
ax0.plot(x_tip, tip_md,'g', linewidth=0.5, linestyle = '--')

ax0.fill_between(x_tip, tip0, tip_activation_hi, facecolor = 'r', alpha=0.7)
ax0.plot(x_tip, tip_hi,'r', linewidth=0.5, linestyle = '--')
ax0.set_title('Output membership activity')

for ax in (ax0,):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()


# In[29]:


print("Percobaan3")


# In[35]:


aggregated = np.fmax(tip_activation_lo, 
                       np.fmax(tip_activation_lo,tip_activation_hi))


# In[36]:


tip = fuzz.defuzz(x_tip, aggregated, 'centroid')
tip_activation = fuzz.interp_membership(x_tip, aggregated, tip)


# In[37]:


fig, ax0 = plt.subplots(figsize=(8, 3))

ax0.plot(x_tip, tip_lo, 'b', linewidth = 0.5, linestyle ='--')
ax0.plot(x_tip, tip_md, 'g', linewidth = 0.5, linestyle ='--')
ax0.plot(x_tip, tip_hi, 'r', linewidth = 0.5, linestyle ='--')
ax0.fill_between(x_tip, tip0, aggregated, facecolor='Orange', alpha=0.7)
ax0.plot([tip, tip], [0,tip_activation], 'k', linewidth = 1.5, alpha=0.9)
ax0.set_title('Aggregated Membership and Result (line)')

for ax in (ax0,):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()


# In[46]:


tip = fuzz.defuzz(x_tip, aggregated, 'som')
tip_activation = fuzz.interp_membership(x_tip, aggregated, tip)


# In[47]:


fig, ax0 = plt.subplots(figsize=(8, 3))

ax0.plot(x_tip, tip_lo, 'b', linewidth = 0.5, linestyle ='--',)
ax0.plot(x_tip, tip_md, 'g', linewidth = 0.5, linestyle ='--')
ax0.plot(x_tip, tip_hi, 'r', linewidth = 0.5, linestyle ='--')
ax0.fill_between(x_tip, tip0, aggregated, facecolor='Orange', alpha=0.7)
ax0.plot([tip, tip], [0,tip_activation], 'k', linewidth = 1.5, alpha=0.9)
ax0.set_title('Aggregated Membership and Result (line)')

for ax in (ax0,):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis()

plt.tight_layout()


# In[ ]:




