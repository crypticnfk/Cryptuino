from pycoingecko import CoinGeckoAPI
from time import sleep
import serial

cg = CoinGeckoAPI()
serialInst = serial.Serial("COM3", baudrate=9600, timeout=1)


def main():
    while True:
        try:
            message = ""
            priceList = cg.get_price(ids=["bitcoin", "ethereum", "matic-network"], vs_currencies="usd")
            for token in priceList:
            
                symbol = None
                if token == "bitcoin":
                    symbol = "BTC"
                elif token == "ethereum":
                    symbol = "ETH"
                elif token == "matic-network":
                    symbol = "MATIC"
                
                message = symbol + "$" + str("{:,}".format(round(priceList[token]['usd'], 2))) + "Rs." + str("{:,}".format(round(priceList[token]['inr'], 2)))
                serialInst.write(message.encode())
                sleep(5)
        
        except Exception as e:
            print("Error: ", e)
            sleep(10)
            

if __name__ == "__main__":
    main()
