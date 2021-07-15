import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "ci6mm1",#place you're crednetials 
        "typeId": "iotedevice",
        "deviceId":"1008"
    },
    "auth": {
        "token": "7569767364"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()


while True:
    temp = round(random.uniform(99.9,105.2), 2)
    pulse=random.randint(65,80)
    bp=random.randint(120,140)
    
    myData={'temperature': temp,'pulse':pulse, 'Blood_Pressure':bp}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    client.commandCallback = myCommandCallback
    time.sleep(5)
                
  
    
client.disconnect()
#**dont connect to ibm watson simulator**#

