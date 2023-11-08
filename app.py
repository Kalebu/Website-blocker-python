"""Module providing a function printing python version."""
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
LINUX_HOST = "/etc/hosts"
WINDOW_HOST = r"C:\Windows\System32\drivers\etc\hosts"
DEFAULT_HOSTER = LINUX_HOST # if you are on windows then change it to WINDOW_HOST
REDIRECT = "127.0.0.1"


if os.name == 'posix':
    DEFAULT_HOSTER = LINUX_HOST

elif os.name == 'nt':
    DEFAULT_HOSTER = WINDOW_HOST
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
                with open(DEFAULT_HOSTER, "r+") as hostfile:
                    hosts = hostfile.read()
                    for site in sites_to_block:
                        if site not in hosts:
                            hostfile.write(REDIRECT + " " + site + "\n")
            else:
                with open(DEFAULT_HOSTER, "r+") as hostfile:
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
