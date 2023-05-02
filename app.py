import time
from datetime import datetime as dt
import os

# Enter the site name which you want to block
sites_to_block = [
    "www.facebook.com",
    "facebook.com",
    "www.youtube.com",
    "youtube.com",
    "www.gmail.com",
    "gmail.com",
]

# different hosts for different os
Linux_host = "/etc/hosts"
Window_host = r"C:\Windows\System32\drivers\etc\hosts"
default_hoster = Linux_host # if you are on windows then change it to Window_host
redirect = "127.0.0.1"


if os.name == 'posix':
    default_hoster = Linux_host

elif os.name == 'nt':
    default_hoster = Window_host
else:
    print("OS Unknown")
    exit()


def block_websites(start_hour, end_hour):
    while True:
        try:
            if (
                    dt(dt.now().year, dt.now().month, dt.now().day, start_hour)
                    < dt.now()
                    < dt(dt.now().year, dt.now().month, dt.now().day, end_hour)
            ):
                print("Do the work ....")
                with open(default_hoster, "r+") as hostfile:
                    hosts = hostfile.read()
                    for site in sites_to_block:
                        if site not in hosts:
                            hostfile.write(redirect + " " + site + "\n")
            else:
                with open(default_hoster, "r+") as hostfile:
                    hosts = hostfile.readlines()
                    hostfile.seek(0)
                    for host in hosts:
                        if not any(site in host for site in sites_to_block):
                            hostfile.write(host)
                    hostfile.truncate()
                print("Good Time")
            time.sleep(3)
        except PermissionError as e:
            print(f"Caught a permission error: Try Running as Admin {e}")
            # handle the error here or exit the program gracefully
            break


if __name__ == "__main__":
    block_websites(9, 21)
