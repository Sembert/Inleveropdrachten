from arduino_device import ArduinoVisaDevice, list_devices


class DiodeExperiment:
    def __init__(self):
        self.device = ArduinoVisaDevice(port="ASRL4::INSTR")

    def scan(self, start, stop):
        U_LED_list = []
        I_LED_list = []
        U_R_list = []

        for ADC in range(start, stop):
            self.device.set_output_value(ADC)

            V_LED = self.device.get_input_voltage(channel=1) - self.device.get_input_voltage(channel=2)
        
            I_LED = int(self.device.get_input_value(2))/220

            V_Res = self.device.get_input_voltage(channel=2)

            I_LED_list.append(I_LED)
            U_LED_list.append(V_LED)
            U_R_list.append(V_Res)

        self.device.set_output_value(0)
        return U_LED_list, U_R_list, I_LED_list

