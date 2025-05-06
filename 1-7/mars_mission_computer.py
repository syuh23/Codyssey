import time
from dummy_sensor import DummySensor

class MissionComputer:
    def __init__(self):
        
        self.ds = DummySensor()
        
        self.env_values = {
            'mars_base_internal_temperature': None,
            'mars_base_external_temperature': None,
            'mars_base_internal_humidity': None,
            'mars_base_external_illuminance': None,
            'mars_base_internal_co2': None,
            'mars_base_internal_oxygen': None
        }

    def get_sensor_data(self):
        
        while True:
            
            self.ds.set_env()
            data = self.ds.get_env()
            self.env_values = data

            print('{\n')
            
            for key, value in self.env_values.items():
                if(key == 'mars_base_internal_oxygen'):
                    print(f"  \'{key}\' : {value}\n")
                else:
                    print(f"  \'{key}\' : {value},\n")
                
            print('}')
            
            time.sleep(5)

RunComputer = MissionComputer()

RunComputer.get_sensor_data()