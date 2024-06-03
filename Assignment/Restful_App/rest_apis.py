import requests
from  config import API_BASE_URL
from auth import get_access_token
from logger import logger

class RestAPI:
    def __init__(self) -> None:
        self.access_token = get_access_token()
        self.headers = {
            "Authorization": f'Bearer {self.access_token}',
            "Content-Type" : 'application/json'
        }
        self.update_delete_headers = {
            "Content-Type" : 'application/json',
            "Accept": 'application/json',
            "Cookie": f'token={self.access_token}'
        }
        
        self.endpoint = 'booking'
        logger.info("Intialized RestAPI with Access Token")
    
  
    # Call to get booking Ids API.
    def get_booking_ids(self):
        try:
            logger.info(f"-----------------------------------------------------------------------------")
            logger.info(f"Getting All Booking Ids...")
            response = requests.get(f'{API_BASE_URL}/{self.endpoint}', headers=self.headers, verify=False)
            logger.info("All the available Booking Ids are: {}".format(' '.join(map(str, response.json()))))
            logger.info(f"-----------------------------------------------------------------------------")
            return response.json()
        except Exception as e:
            logger.error(e)
            raise e
        
    
    # Call to get booking details API for specific Id.
    def get_booking(self, id):
        try:
            logger.info(f"-----------------------------------------------------------------------------")
            logger.info(f"Getting details for Booking Id - {id}:")
            response = requests.get(f'{API_BASE_URL}/{self.endpoint}/{id}', headers=self.headers, verify=False)
            logger.info(f"Details for the Booking Id - {id}:")
            logger.info(response.json())
            logger.info(f"-----------------------------------------------------------------------------")
            return response.json()
        except Exception as e:
            logger.error(e)
            raise e
    
    
    # Call to creating booking API.
    def create_booking(self, data):
        try:
            logger.info(f"-----------------------------------------------------------------------------")
            logger.info(f"Creating a Booking....")
            response = requests.post(f'{API_BASE_URL}/{self.endpoint}', json=data, headers=self.headers, verify=False)
            logger.info(f"Booking Created Successfully, Below are the booking details:")
            logger.info(response.json())
            logger.info(f"-----------------------------------------------------------------------------")
            return response.json()
        except Exception as e:
            logger.error(e)
            raise e
    
    
    # Call to update booking details API for specific Id.
    def update_booking(self, data, id):
        try:
            logger.info(f"-----------------------------------------------------------------------------")
            logger.info(f"Updating a Booking....")
            response = requests.put(f'{API_BASE_URL}/{self.endpoint}/{id}', json=data, headers=self.update_delete_headers, verify=False)
            logger.info(f"Booking Updated Successfully, Below are the booking details for id - {id}")
            logger.info(response.json())
            logger.info(f"-----------------------------------------------------------------------------")
            return response.json()
        except Exception as e:
            logger.error(e)
            raise e
        
        
    # Call to Partially updating booking details API for specific Id.    
    def partial_update_booking(self, data, id):
        try:
            logger.info(f"-----------------------------------------------------------------------------")
            logger.info(f"Partially Updating a Booking....")
            response = requests.patch(f'{API_BASE_URL}/{self.endpoint}/{id}', json=data, headers=self.update_delete_headers, verify=False)
            logger.info(f"Booking Updated Partially, Below are the booking details for id - {id}")
            logger.info(response.json())
            logger.info(f"-----------------------------------------------------------------------------")
            return response.json()
        except Exception as e:
            logger.error(e)
            raise e
        
    # Call to delete booking API.    
    def delete_booking(self, id):
        try:
            logger.info(f"-----------------------------------------------------------------------------")
            logger.info(f"Deleting a Booking....")
            response = requests.delete(f'{API_BASE_URL}/{self.endpoint}/{id}', headers=self.update_delete_headers, verify=False)
            logger.info(f"Booking deleted successfully with booking id - {id}")
            logger.info(response)
            logger.info(f"-----------------------------------------------------------------------------")
            return response
        except Exception as e:
            logger.error(e)
            raise e
    
    # Call to Health Check API.
    def health_check(self):
        try:
            logger.info(f"-----------------------------------------------------------------------------")
            logger.info(f"Checking Health....")
            response = requests.get(f'{API_BASE_URL}/ping', headers=self.headers, verify=False)
            logger.info(response)
            logger.info(f"-----------------------------------------------------------------------------")
            return response
        except Exception as e:
            logger.error(e)
            raise e
