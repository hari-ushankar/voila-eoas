# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     notebook_metadata_filter: all,-toc,-latex_envs
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.5.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   language_info:
#     codemirror_mode:
#       name: ipython
#       version: 3
#     file_extension: .py
#     mimetype: text/x-python
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#     version: 3.7.6
# ---

# %%
import pandas as pd
from pathlib import Path
from matplotlib import pyplot as plt
import json

# %%
with open('toc_files.json','r') as infile:
    co2_dict = json.load(infile)


# %%
def get_df(dir_path):
    pqfile = dir_path / 'rad_spectrum.pq'
    df = pd.read_parquet(pqfile)
    return df


# %%
fig, axarray = plt.subplots(2,2,figsize=(10,10))
axlist = axarray.flat
key_list = list(co2_dict.keys())
key_list.sort()
print(key_list)
for key, ax in zip(key_list,axlist):
    dir_name = Path(co2_dict[key])
    df = get_df(dir_name)
    ax.plot('wavlen_um','total_trans',data=df)
    ax.set_title(key)
    ax.set_xlim([5,25])
plt.show()


# %%
print(df.columns)
fig, axarray = plt.subplots(2,2,figsize=(10,10))
axlist = axarray.flat
key_list = list(co2_dict.keys())
key_list.sort()
print(key_list)
for key, ax in zip(key_list,axlist):
    dir_name = Path(co2_dict[key])
    df = get_df(dir_name)
    ax.plot('wavlen_um','total_radiance_mum',data=df)
    ax.set_title(key)
    ax.set_xlim([5,25])
plt.show()


# %%
the_dir = co2_dict['1000']
keep_profs = dict()
profs=['mol_prof.pq','aero_prof.pq','o3_prof.pq']
for a_prof in profs:
    the_file = Path(the_dir) / a_prof
    key=the_file.stem
    keep_profs[key] = pd.read_parquet(the_file)
for key, value in keep_profs.items():
    print(key,value.columns)

    
fig, axarray = plt.subplots(2,2,figsize=(10,10))
height = keep_profs['mol_prof']['z']
h2o = keep_profs['mol_prof']['h2o']
axlist = axarray.flat
axlist[0].plot('t','z',data=keep_profs['o3_prof']);
axlist[1].plot('mol_scat','z', data = keep_profs['o3_prof'])
axlist[2].plot('o2','z', data = keep_profs['o3_prof'])
axlist[3].plot('n2','z', data = keep_profs['o3_prof']);
