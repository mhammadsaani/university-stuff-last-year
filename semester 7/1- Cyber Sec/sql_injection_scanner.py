# import requests
# from bs4 import BeautifulSoup

# s = requests.Session()
# s.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'

# def get_all_forms(url):
#     soup = BeautifulSoup(s.get(url).content, "html.parser")
#     return soup.find_all("form")

# def form_details(form):
#     details = {}
#     try:
#         action = form.attrs.get("action").lower()
#     except:
#         action = None
#     method = form.attrs.get("method", "get").lower()
#     inputs = []
#     for input_tag in form.find_all("input"):
#         input_type = input_tag.attrs.get("type", "text")
#         input_name = input_tag.attrs.get("name")
#         input_value = input_tag.attrs.get("value", "")
#         inputs.append({"type": input_type, "name": input_name, "value": input_value})
#     details["action"] = action
#     details["method"] = method
#     details["inputs"] = inputs
#     return details

# def vulnerable(response):
#     errors = {
#         "you have an error in your sql syntax;",
#         "warning: mysql",
#         "unclosed quotation mark after the character string",
#         "quoted string not properly terminated",
#     }
#     for error in errors:
#         if error in response.text.lower():
#             return True
#     return False

# def sql_injection_scan(url):
#     forms = get_all_forms(url)
#     print(f"[+] Detected {len(forms)} forms on {url}.")

#     for form in forms:
#         try:
#             details = form_details(form)
#             data = {}
#             for i in "\"'":
#                 for input_tag in details["inputs"]:
#                     if input_tag["type"] == "hidden" or input_tag["value"]:
#                         try:
#                             data[input_tag["name"]] = input_tag["value"] + i
#                         except:
#                             pass
#                     elif input_tag["type"] != "submit":
#                         data[input_tag["name"]] = f"test{i}"
#                 if details["method"] == "post":
#                     res = s.post(details["action"], data=data)
#                 elif details["method"] == "get":
#                     res = s.get(details["action"], params=data)
#                 if vulnerable(res):
#                     print(f"[+] SQL Injection vulnerability detected, link: {url}")
#                 else:
#                     print(f"[-] No SQL Injection vulnerability detected, link: {url}")
#         except Exception as e:
#             print(f"[-] Error occurred while scanning form: {str(e)}")

# if __name__ == "__main__":
#     url_to_be_scanned = 'https://yahoo.com/'
#     sql_injection_scan(url_to_be_scanned) 



password = 'jawad'

def password_crack(password):
    import itertools
    import string
    for i in range(1, 9):
        for j in itertools.product(string.ascii_lowercase + string.ascii_uppercase + string.digits, repeat=i):
            if ''.join(j) == password:
                print('Password cracked: ' + ''.join(j))
                return
    print('Password not cracked')
    
password_crack(password)