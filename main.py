from src.portscan import PortScan
def main(): 
    while True:
        print("==================================================")
        print("Port Scanner - By Zhuowen Dong")
        print("Enter -1 for either the IP or Port Number to Quit")
        print("==================================================")
        ip = getIP()
        port = getPort()

        if ip == -1 or port == -1:
            print("Quiting...")
            return
    
        scanner = PortScan(ip, port)
        scanner.scan()

def getIP():
    while True:
        user_input = input("IP Address: ")
        if user_input is not None:
            return user_input
def getPort():
    while True:
        user_input = input("Port Number: ")
        if user_input is not None:
            return user_input
        
if __name__ == "__main__":
    main()
