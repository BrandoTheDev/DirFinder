import requests

def website_extraction(url):
        print(f"Finding website: {url} ...")
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

def host_exists():
    pass

def help_options():
    pass
    