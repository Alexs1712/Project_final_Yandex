import configuration
import data
import requests

def create_order(body):
    return requests.post(configuration.MAIN_URL + configuration.CREATE_ORDER,
                         json=body,
                         headers=data.header)
def get_order(parameters):
    return requests.get(configuration.MAIN_URL + configuration.GET_ORDER_TRACK,
                        params=parameters)