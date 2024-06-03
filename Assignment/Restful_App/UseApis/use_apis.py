import json
from rest_apis import RestAPI
from logger import logger

class UseAPI:
    def __init__(self) -> None:
        self.client = RestAPI()
        self.ids = []
        with open('test_data\\create.json', 'r') as file_data:  
            self.create_data = json.load(file_data) 
        
        with open('test_data\\update_test1.json', 'r') as file_data:  
            self.test1_data = json.load(file_data) 
        
        with open('test_data\\update_test2.json', 'r') as file_data:  
            self.test2_data = json.load(file_data) 


    def execute(self): 
        try:
            health_response = self.client.health_check()
            if health_response.status_code == 201 or health_response.status_code == 200:
                for data in self.create_data:  
                    response = self.client.create_booking(data)
                    self.ids.append(response['bookingid'])
            
                self.client.get_booking_ids()
                
                for id in self.ids:
                    self.client.get_booking(id)
                
                self.client.partial_update_booking(self.test1_data, self.ids[0])
                self.client.partial_update_booking(self.test2_data, self.ids[1])
                
                self.client.delete_booking(self.ids[0])
            else:
               logger.info("Health check was not successful. Please try again later.") 
        except Exception as e:
            raise e
            
            
class_obj = UseAPI()
class_obj.execute()
