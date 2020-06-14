import time
import json
import random
#import socket
import asyncio
import requests

import ipaddress
import sys
import subprocess
from random import randint
from time import sleep

from walkoff_app_sdk.app_base import AppBase

class dig_domain_to_ip(AppBase):
    __version__ = "1.0.0"
    app_name = "dig_domain_to_ip"

    def __init__(self, redis, logger, console_logger=None):
        """
        Each app should have this __init__ to set up Redis and logging.
        :param redis:
        :param logger:
        :param console_logger:
        """
        super().__init__(redis, logger, console_logger)


    async def domain_to_ip(self,domain_names):
        domains = domain_names.splitlines()
        output_dig=[]
        for dom in domains:
            dig_record=(pydig.query(dom.rstrip(), 'A'))
            for dig in dig_record:
                try:
		    ip=ipaddress.ip_address(dig)
                    output_dig.append(dom + " #~# " + str(ip))
               except:
                   pass
    return "\n".join(output_dig)

def run(request):
    action = request.get_json() 
    print(action)
    print(type(action))
    authorization_key = action.get("authorization")
    current_execution_id = action.get("execution_id")
	
    if action and "name" in action and "app_name" in action:
        asyncio.run(dig_domain_to_ip.run(action), debug=True)
        return f'Attempting to execute function {action["name"]} in app {action["app_name"]}' 
    else:
        return f'Invalid action'
    
if __name__ == "__main__":
    asyncio.run(dig_domain_to_ip.run(), debug=True)
