import requests

# import os
# print(os.listdir())

def request(url):
    try:
        result =requests.get("http://" + url)
        print(url)
    except:
        pass

def main():
    target_url="35.78.168.38"

    with open("list.txt",'r') as wordlist:
        for line in wordlist:
            word=line.strip()
            test_url= word + "."+target_url
            request(test_url)
        print("enumration ended")

main()