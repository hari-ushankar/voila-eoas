# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.6.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
from pathlib import Path
import rad_lib
import pandas as pd
print(rad_lib.soundings_dir)
from io import StringIO  
from matplotlib import pyplot as plt

# %% [markdown]
# # Reading sounding files
#
# ## Read all sounding paths into dictionary
#
# use the name stem for the key

# %%
all_sounds = rad_lib.soundings_dir.glob("**/*dat")
sound_dict=dict()
for sound_file in all_sounds:
    sound_dict[sound_file.stem]=sound_file

# %% [markdown]
# ## Read in the tropical sounding
#
# The first two lines are:
#
#     # AFGL atmospheric constituent profile. tropical. ( AFGL-TR-86-0110)       
#     #     z(km)      p(mb)        T(K)    air(cm-3)    o3(cm-3)     o2(cm-3)    h2o(cm-3)    co2(cm-3)     no2(cm-3)
#     
# So read them in first, then save the rest for the csv body

# %%
trop_file = sound_dict['afglt']
trop_lines = []
with open(trop_file,'r') as file_input:
    for count, line in enumerate(file_input):
        if count==0:
            pass
        elif count==1:
            columns=line.strip().split()
        else:
            trop_lines.append(line)
            
columns = columns[1:]
print(columns)
big_string = ''.join(trop_lines)
with StringIO(big_string) as infile:
    df_tropical = pd.read_csv(infile,sep='\s+',names=columns)

# %%
df_tropical.head()

# %%
fig,axes = plt.subplots(1,4,figsize=(15,10))
ax1,ax2,ax3,ax4 = axes
[item.grid(True) for item in axes]
ax1.plot('T(K)','z(km)',data=df_tropical)
ax2.plot('air(cm-3)','z(km)',data=df_tropical)
ax3.plot('h2o(cm-3)','z(km)',data=df_tropical)
ax4.plot('co2(cm-3)','z(km)',data=df_tropical);
