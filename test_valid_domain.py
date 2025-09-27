from modules.subdomain_enum import check_subdomains

def basic_subdomain_test():
    ip = check_subdomains("www","google.com")
    print(ip)
    ip = check_subdomains("hllo","google.com")
    print(ip)


if __name__ == "__main__":
    basic_subdomain_test()
