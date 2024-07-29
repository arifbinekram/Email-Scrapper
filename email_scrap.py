import urllib.request
import re
import time
from random import randint

# Regular expression for extracting emails
regex = re.compile(
    r"([a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*(@|\sat\s)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.|dot))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"
)

# Open the file containing URLs
with open("urls.txt", "r") as tarurl:
    for line in tarurl:
        with open("emails.txt", "a") as output:
            time.sleep(randint(10, 100))  # Sleep for a random amount of time
            try:
                # Fetch the content of the URL
                url = urllib.request.urlopen(line.strip()).read().decode('utf-8')
                # Write the URL to the output file
                output.write(line)
                # Find all emails in the content
                emails = re.findall(regex, url)
                for email in emails:
                    # Write each email to the output file
                    output.write(email[0] + "\r\n")
                    print(email[0])
            except Exception as e:
                print(f"Error: {e}")

