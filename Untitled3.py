#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import seaborn as sns
df = sns.load_dataset('iris')

 
#without regression
sns.pairplot(df, kind="scatter")
plt.show()


# In[ ]:





# In[ ]:




