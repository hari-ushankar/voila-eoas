# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.6.0
#   kernelspec:
#     display_name: dashboards
#     language: python
#     name: dashboards
# ---

# %%
import plotly
import plotly.graph_objs as go
from plotly.offline import iplot, init_notebook_mode
init_notebook_mode(connected = True)
import numpy as np
import ipywidgets as widgets
import pandas as pd
from pathlib import Path
from matplotlib import pyplot as plt
import json

# %%
#import plotly.plotly as py

# %%
import plotly.graph_objs as go
go.FigureWidget(layout={'title': '$\LaTeX$'})

# %%
#define widgets here
co2_ppm = widgets.Dropdown(
    options=['0', '10', '100', '1000'],
    value='10',
    description='CO2[ppm]:',
    disabled=False,
)
options_gases = ['T(K)','Pressure(mbar)','O2(atm cm/km)','N2(mol/cm2)']
#options_gases = ['T(K)','Pressure(mbar)','Water vapor(mbar)', 
#                           'Ozone(ppm)', 'CO2(ppm)','CO2(uatm)','CH4(ppm)','CH4(uatm)']
dropdown_atoms_profiles = widgets.Dropdown(
                    options=options_gases,
                    value='T(K)',
                    description='X-axis data:',
                    disabled=False,
)

# %%
dict_atmospheric = {options_gases[0]:'t',options_gases[1]:'p',options_gases[2]:'o2',options_gases[3]:'n2' }

# %%

# %%
## from: https://stackoverflow.com/questions/22417484/plancks-formula-for-blackbody-spectrum
import scipy as sp
import math
import matplotlib.pyplot as plt
import numpy as np
pi = np.pi
h = 6.626e-34
c = 3.0e+8
k = 1.38e-23

def planck(wav, T):
    a = 2.0*h*pi*c**2
    b = h*c/(wav*k*T)
    intensity = a/ ( (wav**5)*(math.e**b - 1.0) )
    return intensity

wavelengths = np.arange(1e-6, 30e-6, 2e-7) 

# intensity at 220, 240, 260, 280 and 300 K
intensity220 = planck(wavelengths, 220.)/(1e6)
intensity240 = planck(wavelengths, 240.)/(1e6)
intensity260 = planck(wavelengths, 260.)/(1e6)
intensity280 = planck(wavelengths, 280.)/(1e6)
intensity300 = planck(wavelengths, 300.)/(1e6)
#plt.plot(wavelengths*1e6, intensity220, 'r-') 
# plot intensity4000 versus wavelength in nm as a red line
# plt.plot(wavelengths*1e6, intensity240, 'g-') 
# plt.plot(wavelengths*1e6, intensity260, 'b-') 
# plt.plot(wavelengths*1e6, intensity280, 'k-') 
# plt.plot(wavelengths*1e6, intensity300, 'm-')

# %%
# load the index json file-- for different co2 conc
with open('toc_files.json','r') as infile:
    co2_dict = json.load(infile)

# %%
#build default values for widget 1
dir_name = Path(co2_dict[co2_ppm.value])
pqfile = dir_name / 'rad_spectrum.pq'
df = pd.read_parquet(pqfile)
x_values = df[df.keys()[1]]
scaled_intensity = (df[df.keys()[-1]]*planck(df[df.keys()[1]]*1e-6,300.))/1e6
trace0 = go.Scatter(x=x_values,  y=scaled_intensity, mode="lines", name = 'Model')
bbr_220 = go.Scatter(x=wavelengths*1e6, y=intensity220, mode="lines", name = '220 K')
bbr_240 = go.Scatter(x=wavelengths*1e6, y=intensity240, mode="lines", name = '240 K')
bbr_260 = go.Scatter(x=wavelengths*1e6, y=intensity260, mode="lines", name = '260 K')
bbr_280 = go.Scatter(x=wavelengths*1e6, y=intensity280, mode="lines", name = '280 K')
bbr_300 = go.Scatter(x=wavelengths*1e6, y=intensity300, mode="lines", name = '300 K')

# Now build the figure and define non-default parameters for this figure
g = go.FigureWidget(data=[trace0,bbr_220,bbr_240,bbr_260,bbr_280,bbr_300], 
                    layout=go.Layout(title=dict(text='Radiation spectrum')))
g.layout.width = 600
g.layout.height = 400
g.layout.xaxis.title = r'$\text{Wavelength in} \mu \text{m}$'
g.layout.yaxis.title = 'Intensity(W/m2 micron)'
g.layout.xaxis.range = [5.,25.]

# %%
df.keys()[:]

# %%
plt.plot(df[df.keys()[1]],df[df.keys()[-1]])
plt.xlabel('{}'.format(df.keys()[1]))
plt.ylabel('{}'.format(df.keys()[-1]))

# %%
bbr300 = planck(wavelengths,300.)/(1e6)

# %%
plt.plot(bbr300)

# %%
intensity300

# %%
L = np.convolve(df[df.keys()[-1]],bbr300,mode='same')

# %%
L

# %%
intensity_planck = planck(df[df.keys()[1]]*1e-6,300.)/(1e6)
total_transm = df[df.keys()[-1]]

# %%
#L1 = np.convolve(intensity_planck,total_transm,mode='')

# %%
#L1

# %%
#from scipy import signal

# %%
#plt.plot(signal.convolve(df[df.keys()[-1]],bbr300))

# %%
#scipy.

# %%
#L.size

# %%
#L

# %%
#plt.plot(L1)
#plt.plot()

# %%
# plt.plot(df[df.keys()[1]],df[df.keys()[-1]])
# plt.plot(df[df.keys()[1]],L1)
# plt.xlabel('{}'.format(df.keys()[1]))
# plt.ylabel('{}'.format(df.keys()[-1]))
# #plt.xlim([0,30])

# %%
x1_values = df[df.keys()[1]]
y1_values = df[df.keys()[-3]]
trace1 = go.Scatter(x=x1_values, y=y1_values, mode="lines")

# Now build the figure and define non-default parameters for this figure
g1 = go.FigureWidget(data=[trace1], 
                    layout=go.Layout(title=dict(text='Total radiance spectrum')))
g1.layout.width = 600
g1.layout.height = 400
g1.layout.xaxis.title = r"$\text{Wavelength in} \mu \text{m}$"
#g1.layout.yaxis.title = 'Total_radiance'
g1.layout.xaxis.range = [5.,25.]

# %%
# load the atmospheric profiles
the_dir = co2_dict[co2_ppm.value]
keep_profs = dict()
profs=['mol_prof.pq','aero_prof.pq','o3_prof.pq']
for a_prof in profs:
    the_file = Path(the_dir) / a_prof
    key=the_file.stem
    keep_profs[key] = pd.read_parquet(the_file)

# %%
x2_values = keep_profs['mol_prof']['t']
y2_values = keep_profs['mol_prof']['z']
trace2 = go.Scatter(x=x2_values, y=y2_values, mode="lines")

# Now build the figure and define non-default parameters for this figure
g2 = go.FigureWidget(data=[trace2], 
                    layout=go.Layout(title=dict(text='Mol_prof')))
g2.layout.width = 300
g2.layout.height = 500
g2.layout.xaxis.title = dropdown_atoms_profiles.value
g2.layout.yaxis.title = 'Altitude z (km)'
#g2.layout.xaxis.range = [5.,25.]

# %%
# plt.plot(keep_profs['mol_prof']['t'], keep_profs['mol_prof']['z'])

# plt.plot(keep_profs['o3_prof']['mol_scat'], keep_profs['o3_prof']['z'])

# plt.plot(keep_profs['o3_prof']['o2'], keep_profs['o3_prof']['z'])

# plt.plot(keep_profs['o3_prof']['p'], keep_profs['aero_prof']['z'])

# plt.plot(keep_profs['o3_prof']['n2'], keep_profs['o3_prof']['z'])

# keep_profs.keys()

# %%

# %%

# %%
def rad_spec_1(change):
    dir_name = Path(co2_dict[co2_ppm.value])
    pqfile = dir_name / 'rad_spectrum.pq'
    df = pd.read_parquet(pqfile)
    wavelength_um = df[df.keys()[1]]
    tot_transm = df[df.keys()[-1]]
    total_rad = df[df.keys()[-3]]
    scaled_intensity = (tot_transm*planck(df[df.keys()[1]]*1e-6,300.))/1e6
    g.data[0].x = wavelength_um
    g.data[0].y = scaled_intensity
    g.layout.xaxis.gridwidth = 1
    g.layout.xaxis.title = r'Wavelength in $\mu$m'
    g.layout.xaxis.range = [5.,25.]

    
# The next few calls I don't really understand. 
# Presumably I have to look up what the "observe" method is for "widget" objects. 
# It seems as if the "observe" method needs two parameters: 1) the function to call and 2) the "names" parameters. 
# `names="value"` seems to be saying: "pass these parameters with their values into the 'response' function". 
# Or something like that.

co2_ppm.observe(rad_spec_1, names="value")


# %%
def rad_spec_2(change):
    dir_name = Path(co2_dict[co2_ppm.value])
    pqfile = dir_name / 'rad_spectrum.pq'
    df = pd.read_parquet(pqfile)
    wavelength_um = df[df.keys()[1]]
    tot_transm = df[df.keys()[-1]]
    total_rad = df[df.keys()[-3]]
    scaled_intensity = (tot_transm*planck(df[df.keys()[1]]*1e-6,300.))/1e6
    g1.data[0].x = wavelength_um
    g1.data[0].y = total_rad
    g1.layout.xaxis.title = r'Wavelength in $\mu$m'

    
# The next few calls I don't really understand. 
# Presumably I have to look up what the "observe" method is for "widget" objects. 
# It seems as if the "observe" method needs two parameters: 1) the function to call and 2) the "names" parameters. 
# `names="value"` seems to be saying: "pass these parameters with their values into the 'response' function". 
# Or something like that.

co2_ppm.observe(rad_spec_2, names="value")


# %%
def atmos_profile(change):
    the_dir = co2_dict[co2_ppm.value]
    keep_profs = dict()
    profs=['mol_prof.pq','aero_prof.pq','o3_prof.pq']
    for a_prof in profs:
        the_file = Path(the_dir) / a_prof
        key=the_file.stem
        keep_profs[key] = pd.read_parquet(the_file)
    
    x2_values = keep_profs['o3_prof'][dict_atmospheric[dropdown_atoms_profiles.value]]
    y2_values = keep_profs['o3_prof']['z']
    g2.data[0].x = x2_values
    g2.data[0].y = y2_values
    g2.layout.xaxis.title = dropdown_atoms_profiles.value
    g2.layout.yaxis.title = 'Altitude z (km'

#     plt.legend([220, 240, 260, 280, 300])

dropdown_atoms_profiles.observe(atmos_profile, names="value")
co2_ppm.observe(atmos_profile, names="value")

# %%
# dropdown_atoms_profiles.observe?

# %%
#keep_profs['o3_prof']

# %%
container2 = widgets.HBox([co2_ppm])
container3 = widgets.HBox([dropdown_atoms_profiles])
# Finally, run the dashboard. 
L = widgets.VBox([container2, g])
L1 = widgets.VBox([g1])
L2 = widgets.VBox([container3, g2])
spec = widgets.VBox([L, L1])
widgets.HBox([spec,L2])
