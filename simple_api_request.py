import requests #time

req = requests.get("https://google.com")
print(req.status_code)

# while True:
#     req = requests.get("https://google.com")
#     print(req.status_code)
#     if req.status_code != 200:
#         pass
#     time.sleep(3)


