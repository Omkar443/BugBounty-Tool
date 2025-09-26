#This module check whether a domain exist or not by making request to it

import requests
from utils import helpers
from config import settings

def check_subdomains(domain,subdomain,timeout=10):
    full_domain=f"{domain}.{subdomain}"

    result={
        "subdomain":full_domain,
        "exist":False,
        "ip_address":None,
        "error":None,
        "status_code":None,
    }

    try:
        response = requests.get(
            f"http://{full_domain}",
            timeout:timeout,
            headers={"User-Agent":settings.get_user_agents()}
        )
        
        result["exist"]=True
        result["status_code"]=response.status_code

        import socket
        try:
            ip = socket.gethostbyname(full_domain)
            result["ip_address"]=ip
        except socket.gaierror:
            result["ip_address"]="Not Resolved"

    except requests.exceptions.RequestException as e:
        result["error"]=str(e)
        
    return result




        ip = socket.gethostbyname(full_domain)
        


