import time

# Add the websites that you want to block to this list
websites_to_block = ["www.facebook.com", "www.twitter.com", "www.instagram.com"]

while True:
    current_time = time.localtime()
    # Set the time range in which the websites should be blocked
    if current_time.tm_hour >= 9 and current_time.tm_hour < 18:
        with open(r"C:\Windows\System32\drivers\etc\hosts", "w") as file:
            for website in websites_to_block:
                file.write(f"127.0.0.1 {website}\n")
    else:
        # Remove the website block if it's outside the set time range
        with open(r"C:\Windows\System32\drivers\etc\hosts", "w+") as file:
            lines = file.readlines()
            for line in lines:
                if not any(website in line for website in websites_to_block):
                    file.write(line)
            file.truncate()
    # Set the time interval at which to check the current time
    time.sleep(60)
