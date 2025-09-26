from utils.helpers import banner, validate_url
from config.settings import get_version, get_user_agent, get_default_timeout


def main():

    print(banner())

    domain = input("Enter target domain: ").strip()
    if(validate_url(domain)):
        print(f"Valid domain {domain}")
    else:
        print(f"Invalid domain: {domain}")


    print(get_version())
    print(get_user_agent())
    print(get_default_timeout())



if __name__ == "__main__":
              main()
