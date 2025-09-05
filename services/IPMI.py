from pyghmi.ipmi import command
from config import Config

cmd = command.Command(
    bmc=Config.IPMI_IP,
    userid=Config.IPMI_USER,
    password=Config.IPMI_PASS
)

def get_power_status():
    return cmd.get_power()['powerstate']

def set_power(state):
    if state == "on":
        cmd.set_power("on")
    elif state == "off":
        cmd.set_power("off")
    else:
        cmd.set_power("reset")
