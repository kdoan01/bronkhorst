# Import the propar module
import propar
import time
import numpy as np

# Connect to the local instrument, when no settings provided
# defaults to locally connected instrument (address=0x80, baudrate=38400)
cori_flow = propar.instrument('COM12')
# Prepare a list of parameters for a chained read containing:
# fmeasure, fsetpoint, temperature, valve output
params = [{'proc_nr':  33, 'parm_nr': 0, 'parm_type': propar.PP_TYPE_FLOAT},
          {'proc_nr':  33, 'parm_nr': 3, 'parm_type': propar.PP_TYPE_FLOAT},
          {'proc_nr':  33, 'parm_nr': 7, 'parm_type': propar.PP_TYPE_FLOAT},
          {'proc_nr': 114, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT32}]

# Note that this uses the read_parameters function.
values = cori_flow.read_parameters(params)

# The setpoint and measure parameters are available
# as properties, for ease of use.
#run the pump at 800 baudrates for 10 seconds
t_end = time.time() + 10
while time.time() < t_end:
    cori_flow.setpoint = 800
    np.savetxt('test.txt', values, fmt='%4s', delimiter=',')
    if time.time() >= t_end:
        cori_flow.setpoint = 0
