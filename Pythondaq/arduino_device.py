import pyvisa 


#----------------------------------------------------------------------------------------
# Ex 3.4

class ArduinoVisaDevice:
    def __init__(self, port):
        self.device = rm.open_resource(port, read_termination="\r\n", write_termination="\n")

    def get_identification(self):
        return self.device.query("*IDN?")

    def set_output_value(self, value):
        return self.device.query(f"OUT:CH0 {value}") 

    def get_output_value(self):
        return self.device.query(f"MEAS:CH0?")

    def get_input_value(self, channel):
        return self.device.query(f"MEAS:CH{channel}?")

    def get_input_voltage(self, channel):
        return (3.3/1000*int(self.device.query(f"MEAS:CH{channel}?")))

rm = pyvisa.ResourceManager("@py")
def list_devices():
    return rm.list_resources()