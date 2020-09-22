import requests
import sys

success_sites = []


http_codes = {
    200 : "-> Success!",
    301 : "-> Moved Permanently",
    302 : "-> Moved Temporarily",
    400 : "-> Bad Request",
    403 : "-> Forbidden",
    404 : "-> Not Found",
    500 : "-> Internal Server Error",
    503 :" -> Service Unavailable"
}


def website_extraction(website):
        print(f"[*] Finding website: {website}")
        if website == "":
            print("Please enter a url")
        elif website.startswith("www."):
            website_to_get = f"https://{website}"
        elif website.startswith("http"):
            site = website_to_get
        else:
            website_to_get = f"https://www.{website}"
        url = requests.get(website_to_get)
        return url


def host_exists(url):
        print("[*] Checking website status...")
        if url.status_code == 200:
            print(f"[*] {http_codes[200]}")
            return True
        else:
            print(f"[*] {http_codes[url.status_code]}")
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