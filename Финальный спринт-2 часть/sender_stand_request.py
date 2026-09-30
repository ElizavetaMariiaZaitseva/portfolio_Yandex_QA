import requests 
import configuration          
import request_data as data   
#Создание заказа
def post_new_order(body): 
    url = configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH 
    return requests.post(url, json=body, timeout=10)
#Получить заказ по треку ?t=...
def get_track_order(track): 
    url = configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH 
    return requests.get(url, params={"t": str(track)}, timeout=10)