import nicehash
import time
from playsound2 import playsound
import os


if __name__ == "__main__":
    host = 'https://api2.nicehash.com'
    filename = os.path.dirname(__file__)+"\smw_coin.wav"

    period = 360 #Refresh rate
    limit = 0.00000016 #This is rough estimate for btc -> US 1 Cent

    key = input("Enter your Public API Key: ")
    secret = input("Enter your API Secret: ")
    rigId = input("Enter your Rig ID: ")
    organisation_id = input("Input your organization ID: ")

    private_api = nicehash.private_api(host, organisation_id, key, secret)
    balance = float(private_api.get_rig_stat_1(rigId)['algorithms']['DAGGERHASHIMOTO']['unpaid'])

    print("SHEKL is running")
    playsound(filename)




    while True:
        minerStatus = private_api.get_rig_stat_1(rigId)
        newBalance = float(minerStatus['algorithms']['DAGGERHASHIMOTO']['unpaid'])

        if (newBalance > balance):
            centGain = int((newBalance-balance)/limit)

            for i in range (centGain):
                print("+1 Cent")
                playsound(filename)
                time.sleep(0.1)

            if (centGain > 0):
                balance = newBalance

        elif (newBalance < balance):
            print(nodol)
            balance = newBalance

        time.sleep(period)






