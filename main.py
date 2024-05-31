from Modules.TLD_BUSTER import Tld_Scan
from Modules.SUBD_BUSTER import Sub_Scan
from Modules.DIR_BUSTER import Dir_Scan

class Main:
    def Art():
        print("""

    _   __     __    ______            __    
   / | / /__  / /_  /_  __/___  ____  / /____
  /  |/ / _ \/ __/   / / / __ \/ __ \/ / ___/
 / /|  /  __/ /_    / / / /_/ / /_/ / (__  ) 
/_/ |_/\___/\__/   /_/  \____/\____/_/____/  

> /jwe0""")
    def Main():
        Main.Art()
        ip = None
        print("""
1 > TLD BUSTER
2 > SUB BUSTER
3 > DIR BUSTER
        """)

        mode     = input("Mode         : ")
        name     = input("Target       : ")
        check_ip = input("Check IP y/n : ")

        if check_ip == "y":
            ip   = input("IP           : ")

        if mode == "1":
            Tld_Scan(name, ip)
        elif mode == "2":
            Sub_Scan(name, ip)
        elif mode == "3":
            Dir_Scan(name)




if __name__ == "__main__":
    Main.Main()