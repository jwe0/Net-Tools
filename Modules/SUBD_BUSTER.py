import socket, datetime, threading

def Get_Padding(arr):
    longest = 0
    for i in arr:
        if len(i) > longest:
            longest = len(i)
    return longest

def Check(domain, subdomain, ip, padding):
    try:
        subdomain = subdomain.strip()
        name = subdomain + "." + domain
        results = socket.gethostbyname_ex(name)
        if ip != None:
            if ip not in results[2]:
                return
        while len(name) < padding:
            name += " "
        print("[+]\t[{}]\t {} : {}".format(datetime.datetime.now().strftime('%H:%M:%S'), name, ", ".join(results[2])))
    except Exception as e:
        pass

def Sub_Scan(domain, ip):
    with open("Assets/SUBD.txt") as f:
        subdomains = f.readlines()
    padding = Get_Padding(subdomains)

    for subdomain in subdomains:
        threading.Thread(target=Check, args=(domain, subdomain, ip, padding)).start()