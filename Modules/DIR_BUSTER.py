import requests, datetime, threading



def Get_Padding(arr):
    longest = 0
    for i in arr:
        if len(i) > longest:
            longest = len(i)
    return longest

def Check(domain, dir, padding):
    try:
        dir = dir.strip()
        name = domain + "/" + dir
        r = requests.get(name)
        if r.status_code == 200:
            while len(dir) < padding:
                dir += " "
            print("[+]\t[{}]\t {} : {}".format(datetime.datetime.now().strftime('%H:%M:%S'), domain + "/" + dir, r.status_code))
    except Exception as e:
        pass

def Dir_Scan(domain):
    with open("Assets/DIR.txt") as f:
        dirs = f.readlines()
    padding = Get_Padding(dirs)
    for dir in dirs:
        threading.Thread(target=Check, args=(domain, dir, padding)).start()