import time
from datetime import datetime as dt
import pyuac

# Enter the site name which you want to block
sites_to_block = [
    "www.facebook.com",
    "facebook.com",
    "instagram.com",
    "www.instagram.com",
    "youtube.com",
    "www.youtube.com"
]


# different hosts for different os
Linux_host = r"/etc/hosts"
Window_host = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

def block_websites(default_hoster):
    with open(default_hoster, "r+") as hostfile:
                hosts = hostfile.read()
                for site in sites_to_block:
                    if site not in hosts:
                        hostfile.write(redirect + " " + site + "\n")

def open_websites(default_hoster):
     with open(default_hoster, "r+") as hostfile:
                hosts = hostfile.readlines()
                hostfile.seek(0)
                for host in hosts:
                    if not any(site in host for site in sites_to_block):
                        hostfile.write(host)
                hostfile.truncate()

def check(start_hour, start_minute, end_hour, end_minute):
    counter1 = 0
    counter2 = 0 
  
    while True:
        if (
            dt(dt.now().year, dt.now().month, dt.now().day, start_hour, start_minute)
            < dt.now()
            < dt(dt.now().year, dt.now().month, dt.now().day, end_hour, end_minute)
        ):
            if (counter1 == 0):
                block_websites(default_hoster)
                counter1 += 1
            print("Do the work ....")

        else:
            if counter2 == 0 :
                open_websites(default_hoster)
                counter2 += 1
            print("Good Time")

        time.sleep(5)


if __name__ == "__main__":

    device = input("Enter your OS Name ( Windows / Linux ) :")

    if device.upper() == "WINDOWS":
        default_hoster = Window_host
        if not pyuac.isUserAdmin():
          print("Re-launching as admin!")
          pyuac.runAsAdmin()
 

    elif device.upper() == "LINUX":
        default_hoster = Linux_host

    else:
        print("Not available in this OS")   
        exit(1)
   
    print("Hope you write the sites in sites_to_block field"
          "\n\nNow write the times in 24 hour clock format")

    start_hour, start_minute = [int(x) for x in input("Enter Starting Time in hh:mm format = ").split(':')]
    end_hour, end_minute = [int(x) for x in input("Enter Ending Time in hh:mm format = ").split(':')]
    
    check(start_hour, start_minute, end_hour, end_minute)