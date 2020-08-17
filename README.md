# AWS - IoT Core

## install manual
*    Regist device on **AWS IoT device management**,you will attain above item:

       1. Public key & Private key & certification 
       
       2. **Amazon Root CA 1** file

       3. Thing name & Rest API 

*    Install prerequisite library on Device

       1. sudo pip3 install paho-mqtt
       
*    Download Link-file from GitHub and setup the above peremeter.

```awshost = "Rest_API"
awshost = "Rest_API"
awsport = 8883                                             
clientId = "Thing_Name"                                    
thingName = "Thing_Name"                                   
caPath = "CA_Path"                           
certPath = "Certificate_Path"                           
keyPath = "private_key_Path" 
```

資料來源：https://www.apdaga.com/2018/02/install-aws-amazon-sdk-on-raspberry-pi.html
