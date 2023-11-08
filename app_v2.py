import time
import ctypes

# Add the websites that you want to block to this list
websites_to_block = ["www.facebook.com", "www.twitter.com", "www.instagram.com"]

while True:
    current_time = time.localtime()
    # Set the time range in which the websites should be blocked
    if current_time.tm_hour >= 9 and current_time.tm_hour < 18:
        for website in websites_to_block:
            # Use the Windows hosts file to block the website
            # This will only work on Windows systems
            ctypes.windll.wininet.InternetSetOptionW(0, 39, ctypes.c_void_p(0), 0)
            with open(r"C:\Windows\System32\drivers\etc\hosts", "a") as file:
                file.write(f"127.0.0.1 {website}\n")
    else:
        # Remove the website block if it's outside the set time range
        with open(r"C:\Windows\System32\drivers\etc\hosts", "r+") as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if not any(website in line for website in websites_to_block):
                    file.write(line)
            file.truncate()
    # Set the time interval at which to check the current time
    time.sleep(60)
