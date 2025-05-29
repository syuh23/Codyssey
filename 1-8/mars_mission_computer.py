from dummy_sensor import DummySensor
import time
import platform
import os
import psutil

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
            
            
    def get_mission_computer_info(self):
        system_info = {
            "Operation System" : platform.system(),
            "Operation System Version" : platform.version(),
            "CPU Type" : platform.processor(),
            "CPU Core Count" : os.cpu_count(),
            "Memory Size" : round(psutil.virtual_memory().total / (1024 ** 3), 2)           
        }
        
        print("{")
        
        count = len(system_info)
        for i, (key, value) in enumerate(system_info.items()):
            comma = "," if i < count - 1 else ""
            print(f'    "{key}": "{value}"{comma}')
            
        print("}")
    
    
    def get_mission_computer_load(self):
        load_info = {
            "CPU Usage" : psutil.cpu_percent(interval=1),
            "Memory Usage" : psutil.virtual_memory().percent
        }
        
        print("{")
        
        count = len(load_info)
        for i, (key, value) in enumerate(load_info.items()):
            comma = "," if i < count - 1 else ""
            print(f'    "{key}": "{value}"{comma}')
            
        print("}")
    
runComputer = MissionComputer()
runComputer.get_mission_computer_info()
runComputer.get_mission_computer_load()
