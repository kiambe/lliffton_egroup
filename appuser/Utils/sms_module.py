import requests
import json
url = "https://service.textpie.co.ke/api/v1/customer/sms"
from datetime import datetime


class App_SMS():
    
    
    def __init__(self,phone,msg):
        self.phone = phone
        self.msg = msg
        
    
    def print_phone(self):
        print(f'Phone is  {self.phone}')
    
    

        
    def send_sms(self):
        current_time = datetime.now()
        current_time = current_time.strftime("%m/%d/%Y, %H:%M:%S")
        
        print(current_time)
            
        try:
            headers={
            'X-API-KEY':"neMctHAFYdxExZfKU38kBSDzuJ",
            'Content-Type': 'application/json'
            }

            payload = json.dumps({
            "phone": [
                self.phone
            ],
            "api_username": "ybybyAaltae",
            "campaign_name": "08-Sep-07:58",
            "sender_id": "Lliffton",
            "send_at": current_time,
            "message": self.msg
            })
            

            response = requests.request("POST", url, headers=headers, data=payload)

            data = response.json() 
            print(data)
            print("message has been sent!")
            
        except Exception as e:
            print(e)
            
        
  
    

# p = App_SMS("0791836987","Hello world")



# p.send_sms()

#
    
    # try:
    #     headers={
    #     'X-API-KEY':"neMctHAFYdxExZfKU38kBSDzuJ"
    #     }

    #     payload = json.dumps({
    #     "phone": [
    #         "0791836987"
    #     ],
    #     "api_username": "ybybyAaltae",
    #     "campaign_name": "08-Sep-07:58",
    #     "sender_id": "Lliffton",
    #     "send_at": "2023-09-08 07:55",
    #     "message": "This is a test message"
    #     })
        

    #     response = requests.request("POST", url, headers=headers, data=payload)

    #     data = response.json() 
    #     print(data)
    #     print("message has been sent!")
        
    # except Exception as e:
    #     print(e)