radiance_in="""
                         # Location of atmospheric profile file. 
atmosphere_file afglus.dat
                         # Location of the extraterrestrial spectrum
solar_file atlas_plus_modtran
day_of_year 170          # Correct for Earth-Sun distance
albedo 0.0               # Surface albedo
sza 0.0                 # Solar zenith angle
deltam  on               # delta-M scaling on
nstr  16                 # Number of streams

rte_solver disort2
# Wavelengths considered
wavelength 550    

# radiance angles  test=np.linspace(0.,80.,30)  -- 30 zenith angles
umu {{mus}}

# 20 phis
phi {{phis}}

output_user uu 

transmittance
#reflectivity

zout_sea {{z}}

no_rayleigh
no_absorption

# Location of water cloud file
wc_file thin_cloud.dat  
wc_properties ./wc.sol
#wc_properties ../examples/water_w164c.scat.cdf
#wc_properties ../examples/water_w055c

verbose

"""

flux_in="""
                         # Location of atmospheric profile file. 
atmosphere_file afglus.dat
                         # Location of the extraterrestrial spectrum
solar_file atlas_plus_modtran
day_of_year 170          # Correct for Earth-Sun distance
albedo 0.0               # Surface albedo
sza 0.0                 # Solar zenith angle
deltam  on               # delta-M scaling on
nstr  16                 # Number of streams

rte_solver disort2
# Wavelengths considered
wavelength 550    

# radiance angles  test=np.linspace(0.,80.,30)  -- 30 zenith angles
#umu 0.1736

# 20 phis
#phi 0.000

output_user zout sza clwd edir eglo edn  eup enet

transmittance
#reflectivity

zout_sea   {{zout}}

no_rayleigh
no_absorption

# Location of water cloud file
wc_file thin_cloud.dat  
wc_properties ./wc.sol
#wc_properties ../examples/water_w164c.scat.cdf
#wc_properties ../examples/water_w055c

verbose
"""

avhrr_chan3_thermal="""
# AVHRR parameterization by Kratz [1995]; data file to reproduce 
# Tables 2 and 3 of the publication. Note that an improved 
# extraterrestrial irradiance is used. To reproduce the 
# data in the paper, replace data/solar_flux/kratz with 
# data/solar_flux/kratz.org. Be aware that uvspec 
# automatically chooses to use data/solar_flux/kratz as 
# solar irradiance file if 'correlated_k AVHRR_KRATZ' is specified.

 
data_files_path ../data/ # Location of internal uvspec data files
                         # Location of atmospheric profile file. 
atmosphere_file ../examples/MLS70.UVSPEC

sza 53.1301

rte_solver disort2       # Radiative transfer equation solver


correlated_k AVHRR_KRATZ # Dave Kratz' AVHRR parameterization
wavelength_index 10 14          # Wavelength index range to be selected

no_rayleigh              # no Rayleigh scattering because 
                         # Rayleigh scattering was not included
                         # in the calculation for the 
                         # referenced publication

albedo 0                 # set albedo to 0, emissivity to 1
source thermal           # thermal

zout 0.0 70.0            # surface and top of the atmosphere

filter_function_file ../data/correlated_k/kratz/filter.ch3

output sum               # output sum of all wavelength bands
brightness               # output brightness temperatures

quiet
"""
