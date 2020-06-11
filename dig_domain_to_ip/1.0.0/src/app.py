import time
import json
import random
import socket
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
    app_name = "lastline"

    def __init__(self, redis, logger, console_logger=None):
        """
        Each app should have this __init__ to set up Redis and logging.
        :param redis:
        :param logger:
        :param console_logger:
        """
        super().__init__(redis, logger, console_logger)


    async def single_domain_to_ip(domain_name):
        domain = domain_name
        dig_output_list = subprocess.getoutput("dig +short " + domain).splitlines()
        for dig_record in dig_output_list:
            try:
                # Using 'ipaddress' library (https://docs.python.org/3/library/ipaddress.html), validate IP Address
                ipaddress.ip_address(dig_record)
                return (domain + " #~# " + dig_record)
            except:
                pass

if __name__ == "__main__":
    asyncio.run(dig_domain_to_ip.run(), debug=True)
