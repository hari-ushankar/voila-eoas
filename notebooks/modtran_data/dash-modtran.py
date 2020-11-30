# -*- coding: utf-8 -*-


import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import numpy as np
####--import libraries for modtran stuff
import scipy as sp
import math
import matplotlib.pyplot as plt
import numpy as np
import json
from pathlib import Path
import pandas as pd
pi = np.pi
h = 6.626e-34
c = 3.0e+8
k = 1.38e-23

def planck(wav, T):
    a = 2.0*h*pi*c**2
    b = h*c/(wav*k*T)
    intensity = a/ ( (wav**5)*(math.e**b - 1.0) )
    return intensity



# load the index json file-- for different co2 conc
with open('toc_files.json','r') as infile:
    co2_dict = json.load(infile)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


####-----App layout----####

app.layout=html.Div([
    dcc.Markdown('''
        ### MODTRAN Infrared Light in the Atmosphere

        ----------
        '''),
html.Div([
    dcc.Markdown('''
        **Select CO2 ppm**
        '''),
    dcc.Dropdown(
			id='co2',
			options=[
						{'label':'0 ppm','value': '0'},
						{'label':'10 ppm','value': '10'},
						{'label':'100 ppm','value': '100'},
						{'label':'1000 ppm','value': '1000'},
					],
			value='0',
			placeholder="Select CO2 concentration "
		),
    dcc.Graph(id ='rad-spec-1'),
    dcc.Markdown('''### Total radiance plot:'''),
    dcc.Graph(id='total-radiance'),
    dcc.Markdown('''
        **Select X-axis data:**
        '''),
        dcc.Dropdown(
            id='xaxis_data',
            options=[
                {'label': 'T(K)', 'value':'t'},
                {'label':'Pressure(mbar)', 'value':'p'},
                {'label':'O2(atm cm/km)', 'value':'o2'},
                {'label':'N2(mol/cm2)','value':'n2'}
            ],
            value=['t'],
            placeholder="Select X-axis data"
        ),
    ], style={'width': '78%', 'display': 'inline-block'}),
    dcc.Markdown('''
    Generate Atmospheric profiles
    '''),
    dcc.Graph(id ='atmospheric-profiles')
]
)

@app.callback(
    Output('rad-spec-1', 'figure'),
    Input('co2','value'),
    )  

def rad_spec_1(co2):
    dir_name = Path(co2_dict[co2])
    pqfile = dir_name / 'rad_spectrum.pq'
    df = pd.read_parquet(pqfile)
    wavelength_um = df[df.keys()[1]]
    tot_transm = df[df.keys()[-1]]
    total_rad = df[df.keys()[-3]]
    scaled_intensity = (tot_transm*planck(df[df.keys()[1]]*1e-6,300.))/1e6

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=wavelength_um, y=tot_transm,
                    mode='lines',
                    name='Model'))

    

    fig.update_layout(xaxis_title=r'Wavelength in $\mu$ m', yaxis_title='Total transmisivity')
    fig.update_xaxes(range=[0, 30])
    fig.layout.height = 600
    fig.layout.width = 600
    return fig

@app.callback(
    Output('total-radiance', 'figure'),
    Input('co2','value'),
    )  
def rad_spec_2(co2):
    dir_name = Path(co2_dict[co2])
    pqfile = dir_name / 'rad_spectrum.pq'
    df = pd.read_parquet(pqfile)
    wavelength_um = df[df.keys()[1]]
    total_rad = df[df.keys()[-3]]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=wavelength_um, y=total_rad*np.pi*1e4,
                    mode='lines',
                    name='Model'))
    wavelengths = np.arange(1e-6, 30e-6, 2e-7) 
    
    #intensity at 220, 240, 260, 280 and 300 K
    intensity220 = planck(wavelengths, 220.)/(1e6)
    intensity240 = planck(wavelengths, 240.)/(1e6)
    intensity260 = planck(wavelengths, 260.)/(1e6)
    intensity280 = planck(wavelengths, 280.)/(1e6)
    intensity300 = planck(wavelengths, 300.)/(1e6)
    
    fig.add_trace(go.Scatter(x=wavelengths*1e6, y=intensity220,
                    mode='lines',
                    name='220 K'))
    fig.add_trace(go.Scatter(x=wavelengths*1e6, y=intensity240,
                mode='lines',
                name='240 K'))
    fig.add_trace(go.Scatter(x=wavelengths*1e6, y=intensity260,
                mode='lines',
                name='260 K'))
    fig.add_trace(go.Scatter(x=wavelengths*1e6, y=intensity280,
                mode='lines',
                name='280 K'))
    fig.add_trace(go.Scatter(x=wavelengths*1e6, y=intensity300,
                mode='lines',
                name='300 K'))
 
    fig.update_layout(xaxis_title='Wavelength in $$\mu$$ m', yaxis_title='Intensity W m-2 um-1')
    fig.update_xaxes(range=[0, 30])
    fig.layout.height = 600
    fig.layout.width = 600
    return fig
            

@app.callback(
    Output('atmospheric-profiles', 'figure'),
    [Input('co2','value'),
    Input('xaxis_data','value')]
    )  

# %%
def atmos_profile(co2,xaxis_data):
    options_gases = ['T(K)','Pressure(mbar)','O2(atm cm/km)','N2(mol/cm2)']
    dict_atmospheric = {'t':options_gases[0],'p':options_gases[1],'o2':options_gases[2],'n2':options_gases[3] }
    the_dir = co2_dict[co2]
    keep_profs = dict()
    profs=['mol_prof.pq','aero_prof.pq','o3_prof.pq']
    for a_prof in profs:
        the_file = Path(the_dir) / a_prof
        key=the_file.stem
        keep_profs[key] = pd.read_parquet(the_file)
    x2_values = keep_profs['o3_prof'][xaxis_data]
    y2_values = keep_profs['o3_prof']['z']
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x2_values, y=y2_values,
                    mode='lines'))
    fig.update_layout(xaxis_title='{}'.format(dict_atmospheric[xaxis_data]), yaxis_title='Altitude z (km)')
    fig.layout.height = 800
    fig.layout.width = 400
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)