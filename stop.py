# Import the propar module
import propar

# Connect to the local instrument, when no settings provided
# defaults to locally connected instrument (address=0x80, baudrate=38400)
cori_flow = propar.instrument('COM12')
cori_flow.setpoint = 0