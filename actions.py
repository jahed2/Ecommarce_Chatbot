# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List

# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher


# class ActionService(Action):

#     def name(self) -> Text:
#         return "action_service"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         buttons=[
#             {"payload":"/docs", "title":"Documentation"},
#             {"payload":"/vedio", "title":"vedio content"},
#         ]

#         dispatcher.utter_message(text="Hello World!")

#         return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher
import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import asyncio
from twilio.rest import Client
import os

class ValidateRestaurantForm(Action):
    def name(self)-> Text:
        return "user_details_form"
    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    )->List[EventType]:
       required_slots = ["name","number","address","email"]

       for slot_name in required_slots:
           if tracker.slots.get(slot_name) is None:
               #the slot is not filled yet,Request the user to filled this slot next
               return [SlotSet("requested_slot",slot_name)]
       return [SlotSet("requested_slot",None)]

class ActionSubmit(Action):
    def name(self) ->Text:
        return "action_submit"
    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",

    ) -> List[Dict[Text,Any]]:
        
        # SendEmail(
        #     tracker.get_slot("email"),
        #     tracker.get_slot("subject"),
        #     tracker.get_slot("message")
        
        dispatcher.utter_message(template="utter_details_thanks",
                                 Name=tracker.get_slot("name"),
                                 Mobile_number=tracker.get_slot("number"),
                                 Address=tracker.get_slot("address"),
                                 Email=tracker.get_slot("email"))

# def SendEmail(toaddr,subject,message):
#     fromaddr =  "nomansiddique719@gmail.com"     
#     msg  =  MIMEMultipart()
#     msg['From']   = fromaddr
#     #storing the reciver email address
#     msg['to']   = toaddr
#     #storing the subject
#     msg['subject'] = subject
#     #string to store the body of the mail
#     body = message
#     #attach the body with the message instance
#     msg.attach(MIMEText(body,'plain'))

#     s = smtplib.SMTP('smtp.gmail.com',587)

#     #start tls for the security
#     s.starttls()
    
#     #authenticatim 
#     try:
#         s.login(fromaddr,"123456")
#         #convert the mulitpart meesahge into string
#         text = msg.as_string()
#         #sending the email
#         s.sendmail(fromaddr,toaddr,text)
#     except:
#         print("An error occured while sending the mail")
#     finally:
#         #terminating the session
#         s.quit()

class ActionSubmit1(Action):
    def name(self)->Text:
        return "action_submit1"
    def run(self,dispatcher:CollectingDispatcher,
            tracker:Tracker,
            domain:Dict[Text,Any])->List[Dict[Text,Any]]:
        account_sid = 'AC0a537871c48bdd27906cd28e6ef3be00'
        auth_token = '179f8472bd7b694f111f07058c0dbc48'
        client = Client(account_sid,auth_token)

        message = client.messages.create(
            messaging_service_sid = 'MGe0a8893417375dc25ce04458c37643b9',
            body = tracker.get_slot('message'),
            to = tracker.get_slot("mobile_number")

        )

        print(message.sid)
        dispatcher.utter_message(text="Message has been sent successfully to {}".format(tracker.get_slot("mobile_number")))
        return []



class ActionCarousel(Action):
    def name(self) -> Text:
        return "action_carousels"
    
    def run(self, dispatcher, tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        message = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "HP",
                        "subtitle": "HP ZBook Firefly 15 G7 Core i7 10th Gen 15inch FHD Mobile Workstation Laptop ",
                        "subtitle": "$13711.91",
                        "image_url": "https://www.startech.com.bd/image/cache/catalog/workstation/hp-brand/zbook-firefly-15-g7/zbook-firefly-15-g7-01-500x500.jpg",
                        "buttons": [ 
                            {
                            "title": "Shop Now",
                            "payload": "/buy",
                            "type": "postback"
                            },
                            {
                            "title": "View Details",
                            "payload": "/deny",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "HP",
                        "subtitle":"HP 15s-du1088TU Intel Pentium N5030 15.6 inch FHD Laptop with Win 10",
                        "subtitle": "$435.49",
                        "image_url": "https://www.startech.com.bd/image/cache/catalog/laptop/hp-laptop/15s-du1088tu/hp-15s-du1088tu-500x500.jpg",
                        "buttons": [ 
                              {
                            "title": "Shop Now",
                            "payload": "/buy",
                            "type": "postback"
                            },
                            {
                            "title": "View Details",
                            "payload": "/deny",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "HP",
                        "subtitle": "HP 15S-GU0008AU AMD Athlon 15.6inch HD Laptop with Windows 10",
                        "subtitle": "$478.92",
                        "image_url": "https://www.startech.com.bd/hp-15s-gu0008au-hd-laptop",
                        "buttons": [ 
                            {
                            "title": "Click here",
                            "url": "https://i.gadgets360cdn.com/products/laptops/large/1525206065_635_inspiron-5559.jpg",
                            "type": "web_url"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(attachment=message)
        return []











class ActionCarouse2(Action):
    def name(self) -> Text:
        return "action_carousels2"
    
    def run(self, dispatcher, tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        message = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Asus",
                        "subtitle": "Asus Vivobook E410MA Celeron N4020 14inch FHD Laptop",
                        "subtitle": "$578.86",
                        "image_url": "https://www.startech.com.bd/image/cache/catalog/laptop/asus/e410ma/e410ma-01-500x500.jpg",
                        "buttons": [ 
                            {
                            "title": "Shop Now",
                            "payload": "/buy",
                            "type": "postback"
                            },
                            {
                            "title": "View Details",
                            "payload": "/deny",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Asus",
                        "subtitle":"Asus Vivobook X415MA Celeron N4020 14inch FHD Laptop",
                        "subtitle": "$437.10",
                        "image_url": "https://www.startech.com.bd/image/cache/catalog/laptop/asus/x415ma/x415ma-010-500x500.jpg",
                        "buttons": [ 
                              {
                            "title": "Shop Now",
                            "payload": "/buy",
                            "type": "postback"
                            },
                            {
                            "title": "View Details",
                            "payload": "/deny",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Asus",
                        "subtitle": "Asus VivoBook 15 K513EA Core i5 11th Gen 15.6inch FHD Laptop",
                        "subtitle": "$850.56",
                        "image_url": "https://www.startech.com.bd/image/cache/catalog/laptop/asus/vivobook-15/vivobook-15-1-500x500.jpg",
                        "buttons": [ 
                            {
                            "title": "Click here",
                            "url": "https://i.gadgets360cdn.com/products/laptops/large/1525206065_635_inspiron-5559.jpg",
                            "type": "web_url"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(attachment=message)
        return []



class ActionCarouse1(Action):
    def name(self) -> Text:
        return "action_carousels1"
    
    def run(self, dispatcher, tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        message = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "DELL",
                        "subtitle": "Dell Latitude 15 3510 Core i3 10th Gen 15.6inch HD Laptop",
                        "subtitle": "$443.00",
                        "image_url": "https://www.startech.com.bd/image/cache/catalog/laptop/dell/latitude-3510/latitude-3510-1-500x500.jpg",
                        "buttons": [ 
                            {
                            "title": "Shop Now",
                            "payload": "/buy",
                            "type": "postback"
                            },
                            {
                            "title": "View Details",
                            "payload": "/deny",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "DELL",
                        "subtitle":"Dell Vostro 14 3400 Core i3 11th Gen 14inch HD Laptop",
                        "subtitle": "$567.04",
                        "image_url": "https://www.startech.com.bd/image/cache/catalog/laptop/dell/14-3400/vostro-14-3400-black-front-500x500.jpg",
                        "buttons": [ 
                              {
                            "title": "Shop Now",
                            "payload": "/buy",
                            "type": "postback"
                            },
                            {
                            "title": "View Details",
                            "payload": "/deny",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "DELL",
                        "subtitle": "Dell Inspiron 15-3583 Pentium Gold 5405U 15.6inch HD Laptop",
                        "subtitle": "$464.82",
                        "image_url": "https://www.startech.com.bd/image/cache/catalog/laptop/dell/15-3583/15-3583-01-500x500.jpg",
                        "buttons": [ 
                            {
                            "title": "Click here",
                            "url": "https://i.gadgets360cdn.com/products/laptops/large/1525206065_635_inspiron-5559.jpg",
                            "type": "web_url"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(attachment=message)
        return []



class ActionCarouse3(Action):
    def name(self) -> Text:
        return "action_carousels3"
    
    def run(self, dispatcher, tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        message = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "sweater",
                        "subtitle": "Tommy Hilfiger Men's Pullover Pacific V-Nk, Purple, V-Neck, Long Sleeve",
                        "subtitle": "$95.55",
                        "image_url": "https://i.ebayimg.com/images/g/DOoAAOSw~llg0acF/s-l500.jpg",
                        "buttons": [ 
                            {
                            "title": "Shop Now",
                            "payload": "/buy",
                            "type": "postback"
                            },
                            {
                            "title": "View Details",
                            "payload": "/deny",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "sweater",
                        "subtitle":"Tommy Hilfiger Men's Striped Blue Long Sleeve Sweater Pullover Size Large",
                        "subtitle": "$33.35",
                        "image_url": "https://i.ebayimg.com/images/g/BcgAAOSwGlZggDU7/s-l500.jpg",
                        "buttons": [ 
                              {
                            "title": "Shop Now",
                            "payload": "/buy",
                            "type": "postback"
                            },
                            {
                            "title": "View Details",
                            "payload": "/deny",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "sweater",
                        "subtitle": "sweater for mens",
                        "subtitle": "$464.82",
                        "image_url": "https://i.ebayimg.com/images/g/7IoAAOSwLqBhAlza/s-l500.jpg",
                        "buttons": [ 
                            {
                            "title": "Click here",
                            "url": "https://i.ebayimg.com/images/g/DOoAAOSw~llg0acF/s-l500.jpg",
                            "type": "web_url"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(attachment=message)
        return []




class ActionCarouse4(Action):
    def name(self) -> Text:
        return "action_carousels4"
    
    def run(self, dispatcher, tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        message = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "dress",
                        "subtitle": "Tommy Hilfiger Men's Pullover Pacific V-Nk, Purple, V-Neck, Long Sleeve",
                        "subtitle": "$95.55",
                        "image_url": "https://i.ebayimg.com/images/g/nRoAAOSwWv1hDE9N/s-l500.jpg",
                        "buttons": [ 
                            {
                            "title": "Shop Now",
                            "payload": "/buy",
                            "type": "postback"
                            },
                            {
                            "title": "View Details",
                            "payload": "/deny",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "dress",
                        "subtitle":"Tommy Hilfiger Men's Striped Blue Long Sleeve Sweater Pullover Size Large",
                        "subtitle": "$33.35",
                        "image_url": "https://i.ebayimg.com/images/g/nRoAAOSwWv1hDE9N/s-l500.jpg",
                        "buttons": [ 
                              {
                            "title": "Shop Now",
                            "payload": "/buy",
                            "type": "postback"
                            },
                            {
                            "title": "View Details",
                            "payload": "/deny",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "dress",
                        "subtitle": "sweater for mens",
                        "subtitle": "$464.82",
                        "image_url": "https://i.ebayimg.com/images/g/nRoAAOSwWv1hDE9N/s-l500.jpg",
                        "buttons": [ 
                            {
                            "title": "Click here",
                            "url": "https://i.ebayimg.com/images/g/DOoAAOSw~llg0acF/s-l500.jpg",
                            "type": "web_url"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(attachment=message)
        return []




class ActionCarouse5(Action):
    def name(self) -> Text:
        return "action_carousels5"
    
    def run(self, dispatcher, tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        message = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Hoodies",
                        "subtitle": "Nike Men's Sportswear Just do it Swoosh Logo Graphic Active Pullover Hoodie",
                        "subtitle": "$39.88",
                        "image_url": "https://i.ebayimg.com/images/g/bEAAAOSwamRdHn3n/s-l500.jpg",
                        "buttons": [ 
                            {
                            "title": "Shop Now",
                            "payload": "/buy",
                            "type": "postback"
                            },
                            {
                            "title": "View Details",
                            "payload": "/deny",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Hoodies",
                        "subtitle":"Lucid Mens Size M Black Long Sleeve Kangaroo Pocket Hoodie Ribbed Sweater",
                        "subtitle": "$56.60",
                        "image_url": "https://i.ebayimg.com/images/g/sWcAAOSw3WZgKhgE/s-l500.jpg",
                        "buttons": [ 
                              {
                            "title": "Shop Now",
                            "payload": "/buy",
                            "type": "postback"
                            },
                            {
                            "title": "View Details",
                            "payload": "/deny",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Hoodies",
                        "subtitle": "hoodies for mens",
                        "subtitle": " $39.99",
                        "image_url": "https://i.ebayimg.com/images/g/ZLAAAOSwWmZhDFfu/s-l500.jpg",
                        "buttons": [ 
                            {
                            "title": "Click here",
                            "url": "https://i.ebayimg.com/images/g/ZLAAAOSwWmZhDFfu/s-l500.jpg",
                            "type": "web_url"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(attachment=message)
        return []





class ActionCarouse6(Action):
    def name(self) -> Text:
        return "action_carousels6"
    
    def run(self, dispatcher, tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        message = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Shirt",
                        "subtitle": "Mens Grandad Casual Shirts Mandarin Smart Shirt Long Sleeve Top RH07",
                        "subtitle": " $16.71",
                        "image_url": "https://i.ebayimg.com/images/g/JzwAAOSwGKJfxtYL/s-l500.jpg",
                        "buttons": [ 
                            {
                            "title": "Shop Now",
                            "payload": "/buy",
                            "type": "postback"
                            },
                            {
                            "title": "View Details",
                            "payload": "/deny",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "shirt",
                        "subtitle":"EQ Mens Linen Dress Shirt. Beige/Tan Striped. Lightweight. Size Large",
                        "subtitle": "$27.00",
                        "image_url": "https://i.ebayimg.com/images/g/Mm0AAOSwqCZg~ftn/s-l500.jpg",
                        "buttons": [ 
                              {
                            "title": "Shop Now",
                            "payload": "/buy",
                            "type": "postback"
                            },
                            {
                            "title": "View Details",
                            "payload": "/deny",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "shirt",
                        "subtitle": "shirt for mens",
                        "subtitle": " $34.80",
                        "image_url": "https://i.ebayimg.com/images/g/cUsAAOSwvo5hDGV3/s-l500.jpg",
                        "buttons": [ 
                            {
                            "title": "Click here",
                            "url": "https://i.ebayimg.com/images/g/cUsAAOSwvo5hDGV3/s-l500.jpg",
                            "type": "web_url"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(attachment=message)
        return []





class ActionCarouse7(Action):
    def name(self) -> Text:
        return "action_carousels7"
    
    def run(self, dispatcher, tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        message = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "T-Shirt",
                        "subtitle": "Eisbrecher Black Men's Round Neck T-shirt New",
                        "subtitle": " $12.53",
                        "image_url": "https://i.ebayimg.com/images/g/DhEAAOSwJrdeY7n1/s-l500.jpg",
                        "buttons": [ 
                            {
                            "title": "Shop Now",
                            "payload": "/buy",
                            "type": "postback"
                            },
                            {
                            "title": "View Details",
                            "payload": "/deny",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "T-shirt",
                        "subtitle":"Factory Effex FX Diamond T-Shirt Motorcycle Street Bike",
                        "subtitle": "$9.95",
                        "image_url": "https://i.ebayimg.com/images/g/lvwAAOSwYblhBaId/s-l500.jpg",
                        "buttons": [ 
                              {
                            "title": "Shop Now",
                            "payload": "/buy",
                            "type": "postback"
                            },
                            {
                            "title": "View Details",
                            "payload": "/deny",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "T-shirt",
                        "subtitle": "T-shirt for mens",
                        "subtitle": "$14.99",
                        "image_url": "https://i.ebayimg.com/images/g/DVMAAOSwZQRYdp-7/s-l500.jpg",
                        "buttons": [ 
                            {
                            "title": "Click here",
                            "url": "https://i.ebayimg.com/images/g/DVMAAOSwZQRYdp-7/s-l500.jpg",
                            "type": "web_url"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(attachment=message)
        return []






class ActionCarouse8(Action):
    def name(self) -> Text:
        return "action_carousels8"
    
    def run(self, dispatcher, tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        message = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Jeans",
                        "subtitle": "Mens levis 511 jeans slim fit stretch W30 L30 in very good used condition",
                        "subtitle": "14.60",
                        "image_url": "https://i.ebayimg.com/images/g/LccAAOSwxZ1hDXyA/s-l500.jpg",
                        "buttons": [ 
                            {
                            "title": "Shop Now",
                            "payload": "/buy",
                            "type": "postback"
                            },
                            {
                            "title": "View Details",
                            "payload": "/deny",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Jeans",
                        "subtitle":"Factory Effex FX Diamond T-Shirt Motorcycle Street Bike",
                        "subtitle": "$9.95",
                        "image_url": "https://i.ebayimg.com/images/g/2YMAAOSwjWlhDSh4/s-l500.jpg",
                        "buttons": [ 
                              {
                            "title": "Shop Now",
                            "payload": "/buy",
                            "type": "postback"
                            },
                            {
                            "title": "View Details",
                            "payload": "/deny",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Jeans",
                        "subtitle": "jeans for mens",
                        "subtitle": " $24.95",
                        "image_url": "https://i.ebayimg.com/images/g/2YMAAOSwjWlhDSh4/s-l500.jpg",
                        "buttons": [ 
                            {
                            "title": "Click here",
                            "url": "https://i.ebayimg.com/images/g/DVMAAOSwZQRYdp-7/s-l500.jpg",
                            "type": "web_url"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(attachment=message)
        return []







class ActionCarouse9(Action):
    def name(self) -> Text:
        return "action_carousels9"
    
    def run(self, dispatcher, tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        message = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "samsung",
                        "subtitle": "Galaxy S21 Ultra 5G",
                        "subtitle": "$399.99",
                        "image_url": "https://image-us.samsung.com/SamsungUS/configurator/060321/Configurator-S21-ULTRA-group-765_CNET.jpg",
                        "buttons": [ 
                            {
                            "title": "Shop Now",
                            "payload": "/buy",
                            "type": "postback"
                            },
                            {
                            "title": "View Details",
                            "payload": "/deny",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "samsung",
                        "subtitle":"Galaxy S20 FE 5G",
                        "subtitle": "$349",
                        "image_url": "https://image-us.samsung.com/SamsungUS/home/mobile/phones/galaxy-s/galaxy-s20-fe-5g-images/cloud-mint/PDP-GALLERY-S20-FE-cloud-mint-Lockup-01-1600x1200.jpg?$product-details-jpg$",
                        "buttons": [ 
                              {
                            "title": "Shop Now",
                            "payload": "/buy",
                            "type": "postback"
                            },
                            {
                            "title": "View Details",
                            "payload": "/deny",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "samsung",
                        "subtitle": "samsung galaxy",
                        "subtitle": " $99.95",
                        "image_url": "https://image-us.samsung.com/us/smartphones/galaxy-s21/Gallery-images-Palette/O1-Grey/PDP-O1-Grey-lockup-01-1600x1200.jpg?$product-details-jpg$?$product-details-jpg$",
                        "buttons": [ 
                            {
                            "title": "Click here",
                            "url": "https://image-us.samsung.com/us/smartphones/galaxy-s21/Gallery-images-Palette/O1-Grey/PDP-O1-Grey-lockup-01-1600x1200.jpg?$product-details-jpg$?$product-details-jpg$",
                            "type": "web_url"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(attachment=message)
        return []








class ActionCarouse10(Action):
    def name(self) -> Text:
        return "action_carousels10"
    
    def run(self, dispatcher, tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        message = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Iphone",
                        "subtitle": "Apple iPhone 12 Pro Max",
                        "subtitle": "$1099",
                        "image_url": "https://www.mobiledokan.com/wp-content/uploads/2020/10/Apple-iphone-12-Pro-Max.jpg",
                        "buttons": [ 
                            {
                            "title": "Shop Now",
                            "payload": "/buy",
                            "type": "postback"
                            },
                            {
                            "title": "View Details",
                            "payload": "/deny",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Iphone",
                        "subtitle":"Refurbished iPhone 11 Pro 256GB - Midnight Green (Unlocked)",
                        "subtitle": "$849.00",
                        "image_url": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/refurb-iphone-11-pro-midnight-green-2019?wid=572&hei=572&fmt=jpeg&qlt=95&.v=1611101526000",
                        "buttons": [ 
                              {
                            "title": "Shop Now",
                            "payload": "/buy",
                            "type": "postback"
                            },
                            {
                            "title": "View Details",
                            "payload": "/deny",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Iphone",
                        "subtitle": "iphone11 pro",
                        "subtitle": " $99.95",
                        "image_url": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/refurb-iphone-11-pro-silver-2019?wid=572&hei=572&fmt=jpeg&qlt=95&.v=1611101533000",
                        "buttons": [ 
                            {
                            "title": "Click here",
                            "url": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/refurb-iphone-11-pro-silver-2019?wid=572&hei=572&fmt=jpeg&qlt=95&.v=1611101533000",
                            "type": "web_url"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(attachment=message)
        return []



# class ActionCarouse11(Action):
#     def name(self) -> Text:
#         return "action_carousels11"
    
#     def run(self, dispatcher, tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
#         message = {
#             "type": "template",
#             "payload": {
#                 "template_type": "generic",
#                 "elements": [
#                     {
#                         "title": "Iphone",
#                         "subtitle": "Apple iPhone 12 Pro Max",
#                         "subtitle": "$1099",
#                         "image_url": "https://www.mobiledokan.com/wp-content/uploads/2020/10/Apple-iphone-12-Pro-Max.jpg",
#                         "buttons": [ 
#                             {
#                             "title": "View Details",
#                             "payload": "/buy",
#                             "type": "postback"
#                             },
#                             {
#                             "title": "Shop Now",
#                             "payload": "/deny",
#                             "type": "postback"
#                             }
#                         ]
#                     },
#                     {
#                         "title": "Iphone",
#                         "subtitle":"Refurbished iPhone 11 Pro 256GB - Midnight Green (Unlocked)",
#                         "subtitle": "$849.00",
#                         "image_url": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/refurb-iphone-11-pro-midnight-green-2019?wid=572&hei=572&fmt=jpeg&qlt=95&.v=1611101526000",
#                         "buttons": [ 
#                               {
#                             "title": "View Details",
#                             "payload": "/buy",
#                             "type": "postback"
#                             },
#                             {
#                             "title": "Shop Now",
#                             "payload": "/deny",
#                             "type": "postback"
#                             }
#                         ]
#                     },
#                     {
#                         "title": "samsung",
#                         "subtitle": "samsung galaxy",
#                         "subtitle": " $99.95",
#                         "image_url": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/refurb-iphone-11-pro-silver-2019?wid=572&hei=572&fmt=jpeg&qlt=95&.v=1611101533000",
#                         "buttons": [ 
#                             {
#                             "title": "Click here",
#                             "url": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/refurb-iphone-11-pro-silver-2019?wid=572&hei=572&fmt=jpeg&qlt=95&.v=1611101533000",
#                             "type": "web_url"
#                             }
#                         ]
#                     }
#                 ]
#                 }
#         }
#         dispatcher.utter_message(attachment=message)
#         return []



class ActionCarouse12(Action):
    def name(self) -> Text:
        return "action_carousels12"
    
    def run(self, dispatcher, tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        message = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Huawei",
                        "subtitle": "Apple iPhone 12 Pro Max",
                        "subtitle": "$1099",
                        "image_url": "https://consumer-img.huawei.com/content/dam/huawei-cbg-site/common/mkt/pdp/phones/y5p/img/huawei-y5p-kv.jpg",
                        "buttons": [ 
                            {
                            "title": "Shop Now",
                            "payload": "/buy",
                            "type": "postback"
                            },
                            {
                            "title": "View Details",
                            "payload": "/deny",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Huawei",
                        "subtitle":"huawei y9",
                        "subtitle": "$215",
                        "image_url": "https://consumer-img.huawei.com/content/dam/huawei-cbg-site/common/mkt/pdp/phones/y9s/img/pc/huawei-y9s-pc.jpg",
                        "buttons": [ 
                              {
                            "title": "Shop Now",
                            "payload": "/buy",
                            "type": "postback"
                            },
                            {
                            "title": "View Details",
                            "payload": "/deny",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Huawie",
                        "subtitle": "huawie Nova-8i",
                        "subtitle": " $400",
                        "image_url": "https://www.mobiledokan.co/wp-content/uploads/2021/06/Huawei-Nova-8i-Interstellar-Blue.jpg",
                        "buttons": [ 
                            {
                            "title": "Click here",
                            "url": "https://www.mobiledokan.co/wp-content/uploads/2021/06/Huawei-Nova-8i-Interstellar-Blue.jpg",
                            "type": "web_url"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(attachment=message)
        return []





class ActionCarouse13(Action):
    def name(self) -> Text:
        return "action_carousels13"
    
    def run(self, dispatcher, tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        message = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Sony TVs",
                        "subtitle": "BRAVIA XR Z9J 8K HDR Full Array LED with Smart Google TV (2021)",
                        "subtitle": "$9,999.99",
                        "image_url": "https://d13o3tuo14g2wf.cloudfront.net/thumbnails%2Flarge%2FAsset+Hierarchy%2FConsumer+Assets%2FTelevision+%28Assets%29%2FBRAVIA%C3%82%C2%AE+LCD+HDTV%2FFY+21%2FZ9J+Series%2FeComm+Images%2FXR75Z9J_0000_001_a3d125c00da05c06159fd24740c0bd69.png.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9kMTNvM3R1bzE0ZzJ3Zi5jbG91ZGZyb250Lm5ldC90aHVtYm5haWxzJTJGbGFyZ2UlMkZBc3NldCtIaWVyYXJjaHklMkZDb25zdW1lcitBc3NldHMlMkZUZWxldmlzaW9uKyUyOEFzc2V0cyUyOSUyRkJSQVZJQSVDMyU4MiVDMiVBRStMQ0QrSERUViUyRkZZKzIxJTJGWjlKK1NlcmllcyUyRmVDb21tK0ltYWdlcyUyRlhSNzVaOUpfMDAwMF8wMDFfYTNkMTI1YzAwZGEwNWMwNjE1OWZkMjQ3NDBjMGJkNjkucG5nLnBuZyIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MjE0NTc2MjAwMH19fV19&Signature=cnRUgtKdg5PiDtpNEzjwELT-re-9ztz3TSelzhgt60Am1ILZiB570cioRrJ~boQfcu7G9TapVowvdEpfqpWgD-XfB2hVROy41ZqJfH6fQ95lWaQg-zYVg3sXvW5WHfytrg~EJq6oxTYI2lmgjGDDuLhoudf5PlNWAmySOb0JqKeS7WoCB~aRFvPHb3it5j69rdLV0NvHYGA7H1LwvXHvRqGtZZtEVRhA1d3Hv65QdlD0mIQwfaeZINpyxHsAVYU2hdgH3FcJfurBOVQeBHqXsoRk9CqqaEJRIVzA9wRx35FiybAy8wkKLzAL~tFN~9fpyNQ4GOt78zX0pt3iGGvcWg__&Key-Pair-Id=K37BLT9C6HMMJ0",
                        "buttons": [ 
                            {
                            "title": "Shop Now",
                            "payload": "/buy",
                            "type": "postback"
                            },
                            {
                            "title": "View Details",
                            "payload": "/deny",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Sony TVs",
                        "subtitle":"BRAVIA XR A80J 4K HDR OLED with Smart Google TV (2021)",
                        "subtitle": "$3,499.99",
                        "image_url": "https://d13o3tuo14g2wf.cloudfront.net/thumbnails%2Flarge%2FAsset+Hierarchy%2FConsumer+Assets%2FTelevision+%28Assets%29%2FBRAVIA%C3%82%C2%AE+LCD+HDTV%2FFY+21%2FA80J+Series%2FEcom+Images%2FA80J_0000_001_cf24b41374702061b74b577da50a329d.png.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9kMTNvM3R1bzE0ZzJ3Zi5jbG91ZGZyb250Lm5ldC90aHVtYm5haWxzJTJGbGFyZ2UlMkZBc3NldCtIaWVyYXJjaHklMkZDb25zdW1lcitBc3NldHMlMkZUZWxldmlzaW9uKyUyOEFzc2V0cyUyOSUyRkJSQVZJQSVDMyU4MiVDMiVBRStMQ0QrSERUViUyRkZZKzIxJTJGQTgwSitTZXJpZXMlMkZFY29tK0ltYWdlcyUyRkE4MEpfMDAwMF8wMDFfY2YyNGI0MTM3NDcwMjA2MWI3NGI1NzdkYTUwYTMyOWQucG5nLnBuZyIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MjE0NTc2MjAwMH19fV19&Signature=LpP6h65U~HgANKlqD5yzEjOa7Xd~bl8q2jVXJgbfpk9NwtPh3HvHdI3DSjlkY6sT~XTfo5mWvBWxiRJqKdKWMvdYQMDmzkBrRpVf724BSNDi-ST1wUKTXfvs0NeaehFcZIg~viECkiSdjHNrQ-Ugx0dVg2pJStGHbqX2Xm7eghZ1hqvNLSn8-u5olPOKTnhcd9aMCi9U~8J9rtL3lp7qqYA9dFyDdL0tTdEySwtK9AlPNQnwZyMMxGOP4kOC5OAgwfJQfVmKOslPZQDws4kiaJkCI8qIKuj7jktyLnn-joDfOMxT80wYnCLzaaDvdtuVrkUzrHK49cc79OzhPmVEqw__&Key-Pair-Id=K37BLT9C6HMMJ0",
                        "buttons": [ 
                              {
                            "title": "Shop Now",
                            "payload": "/buy",
                            "type": "postback"
                            },
                            {
                            "title": "View Details",
                            "payload": "/deny",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Sony TVs",
                        "subtitle": "BRAVIA XR A90J 4K HDR OLED with Smart Google TV (2021)",
                        "subtitle": "$3,799.99",
                        "image_url": "https://d13o3tuo14g2wf.cloudfront.net/thumbnails%2Flarge%2F_default_upload_bucket%2F1-+A90J+Hero_1.png.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9kMTNvM3R1bzE0ZzJ3Zi5jbG91ZGZyb250Lm5ldC90aHVtYm5haWxzJTJGbGFyZ2UlMkZfZGVmYXVsdF91cGxvYWRfYnVja2V0JTJGMS0rQTkwSitIZXJvXzEucG5nLnBuZyIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MjE0NTc2MjAwMH19fV19&Signature=d-VxROCSZBfQdJeJmdUkpSmbo01l1UZobtswBhxdOs~3MC27k30o7pq9ufeafET15UInL3SCdXU1VH-CBbcP6~9P5RIEwc1rkZ~119FS0sTY~TPiRWTYS4tQpQ4C~3irHBF0oDHwVbuoqCI0WfIp-KSFessz0ilM9O9u2UbPWHGnaPaazQ48QXQAf0V2M4ZF8cs~9u5i4~qdpTCji-dn9zPPt0tV8E3jLzyFJMMCz0zQehFMnB~7VHm4vhKMeY6U3GkINi1hLhSqPADgp7XTCCwz28EIwwVWPgJIuibZyeaBR8Jwg2iXj4hEUE0HmuHeaDpBID0fWW9ItVTpPhgRLw__&Key-Pair-Id=K37BLT9C6HMMJ0",
                        "buttons": [ 
                            {
                            "title": "Click here",
                            "url": "https://electronics.sony.com/tv-video/televisions/oled/p/xr77a80j",
                            "type": "web_url"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(attachment=message)
        return []





class ActionCarouse14(Action):
    def name(self) -> Text:
        return "action_carousels14"
    
    def run(self, dispatcher, tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        message = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "LG TVs",
                        "subtitle": "LG B1 65 inch Class 4K Smart OLED TV w/AI",
                        "subtitle": "$2,099.99",
                        "image_url": "https://www.lg.com/us/images/tvs/md08000710/gallery/D-01.jpg",
                        "buttons": [ 
                            {
                            "title": "Shop Now",
                            "payload": "/buy",
                            "type": "postback"
                            },
                            {
                            "title": "View Details",
                            "payload": "/deny",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "LG TVs",
                        "subtitle":"LG NanoCell 90 Series 2021 75 inch 4K Smart UHD TV w/ AI ThinQ®",
                        "subtitle": "$2,199.99",
                        "image_url": "https://www.lg.com/us/images/tvs/md07521512/gallery/desktop-01.jpg",
                        "buttons": [ 
                              {
                            "title": "Shop Now",
                            "payload": "/buy",
                            "type": "postback"
                            },
                            {
                            "title": "View Details",
                            "payload": "/deny",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "LG TVs",
                        "subtitle": "LG NanoCell 85 Series 2020 65 inch Class 4K Smart UHD NanoCell TV w/ AI ThinQ®",
                        "subtitle": "$999.99",
                        "image_url": "https://www.lg.com/us/images/tvs/md07500054/gallery/desktop-01.jpg",
                        "buttons": [ 
                            {
                            "title": "Click here",
                            "url": "https://www.lg.com/us/images/tvs/md07500054/gallery/desktop-01.jpg",
                            "type": "web_url"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(attachment=message)
        return []




class ActionCarouse15(Action):
    def name(self) -> Text:
        return "action_carousels15"
    
    def run(self, dispatcher, tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        message = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Samsung TVs",
                        "subtitle": "Samsung 40M5100 40inch Full HD Non Smart LED TV",
                        "subtitle": "$400",
                        "image_url": "https://www.startech.com.bd/image/cache/catalog/television/samsung/40m5100/40m5100-500x500.jpeg",
                        "buttons": [ 
                            {
                            "title": "Shop Now",
                            "payload": "/buy",
                            "type": "postback"
                            },
                            {
                            "title": "View Details",
                            "payload": "/deny",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Samsung TVs",
                        "subtitle":"Samsung 43T4500 43inch HD Smart LED TV",
                        "subtitle": "$565",
                        "image_url": "https://www.startech.com.bd/image/cache/catalog/television/samsung/43t4500/43t4500-500x500.jpeg",
                        "buttons": [ 
                              {
                            "title": "Shop Now",
                            "payload": "/buy",
                            "type": "postback"
                            },
                            {
                            "title": "View Details",
                            "payload": "/deny",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Samsung TVs",
                        "subtitle": "Samsung 43TU7000 43inch Crystal UHD 4K Smart LED TV",
                        "subtitle": " $620",
                        "image_url": "https://www.startech.com.bd/image/cache/catalog/television/samsung/tu7000/tu7000-500x500.jpg",
                        "buttons": [ 
                            {
                            "title": "Click here",
                            "url": "https://www.startech.com.bd/image/cache/catalog/television/samsung/tu7000/tu7000-500x500.jpg",
                            "type": "web_url"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(attachment=message)
        return []




