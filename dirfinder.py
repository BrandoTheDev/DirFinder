import requests

def website_extraction(url):
        print(f"[*] Finding website: {url} ...")
        if url == "":
            print("Please enter a url or --help for options")
        elif url.startswith("www."):
            return f"https://{url}"
        elif url.startswith("http"):
            return url
        elif url == "-h" or url == "--help":
            help_options()
        else:
            return f"https://www.{url}"

def host_exists(url):
        print("[*] Checking websites status...")
        if url.status_code == 200:
            print(f"[*] {url} -> 200: Success!")
            return True
        elif url.status_code == 301:
            print(f"[*] {url} -> 301: Moved Permanently")
        elif url.status_code == 302:
            print(f"[*] {url} -> 302: Moved Temporarily")
        elif url.status_code == 403:
            print(f"[*] {url} -> 403: Forbidden")
        elif url.status_code == 404:
            print(f"[*] {url} -> 404: Not Found")
        elif url.status_code == 500:
            print(f"[*] {url} -> 500: Internal Server Error")
        elif url.status_code == 503:
            print(f"[*] {url} -> 503: Service Unavailable")
        return False
        



def help_options():
    pass
    