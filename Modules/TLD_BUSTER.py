import socket, datetime, threading

def Get_Padding(arr):
    longest = 0
    for i in arr:
        if len(i) > longest:
            longest = len(i)
    return longest

def Check(domain, tld, ip, padding):
    try:
        tld = tld.strip()
        name = domain + "." + tld
        results = socket.gethostbyname_ex(name)
        if ip != None:
            if ip not in results[2]:
                return
        while len(tld) < padding:
            tld += " "
        print("[+]\t[{}]\t {} : {}".format(datetime.datetime.now().strftime('%H:%M:%S'), domain + "." + tld, ", ".join(results[2])))
    except Exception as e:
        pass 

def Tld_Scan(domain, ip):
    with open("Assets/TLDS.txt") as f:
        tlds = f.readlines()
    padding = Get_Padding(tlds)

    for tld in tlds:
        threading.Thread(target=Check, args=(domain, tld, ip, padding)).start()
        