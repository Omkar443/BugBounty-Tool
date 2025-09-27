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
            timeout=timeout,
            headers={"User-Agent":settings.get_user_agent()}
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


def enumerate_from_wordlists(domain,wordlist,max_workers=10):

    found_subdomain = []
    try:
        with open(wordlist,'r') as lines:
            subdomains = [line.strip() for line in lines]

        print(f"checking {len(subdomains)} subdomains for {domain}")

        for subdomain in subdomains[:10]:
            if subdomain:
                result = check_subdoman(domain,subdomain)
                if(result['Exist']):
                   print(f"Found subdomain {result['subdomain']}")
                   found_subdomain.append(result)
                else:
                   print(f"Not Found: {subdoman}.{domain}")

    except FileNotFoundError:
                   print(f"Wordlist file not found {wordlist}")

    except Exception as e:
                   print(f"Unable to read wordlist file {e}")


    return found_subdomain





