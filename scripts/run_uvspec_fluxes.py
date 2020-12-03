from jinja2 import Template
import sys
import argparse
import numpy as np
import subprocess
import matplotlib.pyplot as plt
from ubcplot.stdplot import simplots
from run_uvspec_radiances import get_templates

templates=get_templates()
template=Template(templates.flux_in)
the_dict={}
zout=np.linspace(3.1,3.2,25)
#upper=np.array([5.,6,7,12,15])
#zout=np.concatenate((zout,upper))
zout_text=" ".join(["%7.4f" % number for number in zout])
            
the_dict['zout']=zout_text
the_dict['cloud_file']='thin_cloud.dat'  
#the_dict['mie_file']='./tiny'
the_dict['mie_file']='./wc.sol'
the_dict['col_names']="zout sza clwd edir eglo edn eup enet"

#
# write them into the uvspec input file
#
rendered=template.render(the_dict)
print "rendered: ",rendered

uvspec_input="lrt_fluxes_in.txt"
uvspec_output="lrt_fluxes_out.txt"
uvspec_details="good_details.txt"
thedetails=open(uvspec_details,'w')
theout=open(uvspec_input,'w')
theout.write(rendered.lstrip())
theout.close()
#
# open input and output for uvspec and run
#
input=open(uvspec_input,'r')
output=open(uvspec_output,'w')
command='/home/phil/usr64/libradtran/bin/uvspec'
subprocess.call(command,stdin=input,stdout=output,
                stderr=thedetails)

#
# read in the cloud profile and convert
#
wc_file=open(the_dict['cloud_file'],'r')
wc_profile=wc_file.read()
wc_file.close()


wc_list=[]
for line in wc_profile.split('\n'):
    try:
        float_line=[float(x) for x in line.split()]
        if len(float_line) != 3:
            continue
        wc_list.append(float_line)
    except ValueError:
        pass
wc_array=np.array(wc_list)
cloud_rows,numcols=wc_array.shape

input=open(uvspec_output,'r')
data=input.read()
data=data.split('\n')

## out=np.core.records.fromarrays(rad_array.T,names=col_names)
#
# process the libradtran output from datafile
#
col_names=the_dict['col_names'].split()
out_array=[]
for line in data:
    items=line.split()
    print line
    if len(items) != len(col_names):
        continue
    out_array.append([float(i) for i in items])

out_array=np.array(out_array)
rad_rows,rad_cols=out_array.shape

plot_dat=np.core.records.fromarrays(
    out_array.T,names=col_names)

figfac=simplots()
figfac.fignum=1
ax1=figfac.singleplot()
edir=ax1.plot(plot_dat.edir,plot_dat.zout,'b-')
edn=ax1.plot(plot_dat.edn,plot_dat.zout,'r-')
eup=ax1.plot(plot_dat.eup,plot_dat.zout,'g-')
ax1.set_ylim([2.8,3.5])
ax1.set_xlim([-0.1,1.1])
ax1.set_title('using %s for phase function' % the_dict['mie_file'])
ax1.legend((edir,edn,eup),('edir','edn','eup'))
ax1.figure.savefig('thin2_cloud.png',dpi=150)
plt.show()







