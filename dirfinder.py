import requests
import sys

success_sites = []

def website_extraction(website):
        print(f"[*] Finding website: {website}")
        if website == "":
            print("Please enter a url")
        elif website.startswith("www."):
            url = requests.get(f"https://{website}")
            return url
        elif website.startswith("http"):
            url = requests.get(website)
            return url
        else:
            url = requests.get(f"https://www.{website}")
            return url

def host_exists(url):
        print("[*] Checking website status...")
        if url.status_code == 200:
            print(f"[*] 200 -> Success!")
            return True
        elif url.status_code == 301:
            print(f"[*] 301 -> Moved Permanently")
        elif url.status_code == 302:
            print(f"[*] 302 -> Moved Temporarily")
        elif url.status_code == 400:
            print(f"[*] 400 -> Bad Request")
        elif url.status_code == 403:
            print(f"[*] 403 -> Forbidden")
        elif url.status_code == 404:
            print(f"[*] 404 -> Not Found")
        elif url.status_code == 500:
            print(f"[*] 500 -> Internal Server Error")
        elif url.status_code == 503:
            print(f"[*] 503 -> Service Unavailable")
        return False
        

def check_dirs(website):
    with open("namelist.txt") as namelist:
        for ext in namelist:
            if host_exists(website_extraction(f"{website}/{ext}")):
                success_sites.append(f"{website}/{ext}")
        print(f"[*] Found {len(success_sites)} directories for {website}")
        if len(success_sites) >= 50:
            print("Results over 50. Possible false positives. Manually Review!")
        elif len(success_sites) >= 1:
            for site in success_sites:
                print(f"[*] Discovered: {site}")


check_dirs(str(sys.argv[1]))