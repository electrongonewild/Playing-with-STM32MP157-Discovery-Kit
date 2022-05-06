# CAN Communication
CAN  stands for Controller Area network. It is an Asynchronous serial communication protocol introduced in 1986 by Robert Bosch.
CAN protocol is a message based protocol not address based means transmitted data is available for all nodes and its receiver’s choice to receive data or not.
In this project, we are going to see the following using STM32MP157x-DK1/2:
* Make changes to device tree to configure fdcan pins for CAN communication
* Flash autorun CAN config files on startup
* Use ```SocketCAN```  module to send and receive CAN frames using can-utils
* Send and receive CAN frames using python-can

## Table of Contents
* [Documentation](can/README.md#documentation)
* [Prerequisites](README.md#prerequisites)
* [Connection Diagram](README.md#connections)
* [Getting Started](README.md#getting-started)
* [Basic AT Commands](README.md#basic-at-commands)
* [Implementation](README.md#implementation)
* [Contributions](README.md#contributions)

## Documentation
It is highly recommended to go through the Documentation first.<br>
Here are direct links for same.<br>
* [Datasheet](https://www.quectel.com/ProductDownload/EC200T.zip) 
* [AT Command Manual](https://www.quectel.com/ProductDownload/EC200T.zip)
## Prerequisites
* [Realterm](https://realterm.sourceforge.io/index.html#downloads_Download) or any other serial terminal
* USB to TTL (CP2102)
* EC200 EVB
* Jumpers
* Basic knowledge of UART and serial communication
## Connections
![Alt text](Images/Schematic_EC200_2022-04-21.png?raw=true "Title")
* Rx(EC200) ---> Tx(USB to TTL)
* Tx(EC200) ---> Rx(USB to TTL)
* Power Supply(5V/3.3V and GND)
## Getting Started
Follow the steps for getting started:
* Connect the USB to TTL(CP2102) to USB port of PC and open device manager to check the port connected to serial bridge (USB to TTL).<br>
![Alt text](Images/deviceManager.png?raw=true "Title")
* Open Realterm or any other serial terminal you want to use.
* Open the port to which your serial device is connected make sure to check serial configuration as follows:<br>
   Baudrate : 115200<br>
   Data Bits : 8<br>
   Parity : None<br>
   Stopbits : 1<br> 
![Alt text](Images/serialConfig.PNG?raw=true "Title")
* That's it!!! Now you can send AT commands using realterm directly to GSM Module and also receive its response.
* Firstly check whether you receive ```OK``` in response to ```AT\r\n```, to make sure that your connections and configurations are fine.
* Now you can further proceed to other AT commands according to your application.
## Basic AT Commands
1. Basic AT Command: ```AT\r\n```
2. Deactivate PDP Context: ```AT+QIDEACT=1\r\n```
3. Set APN: (according to network operator)
  * ```AT+QICSGP=1,1,"JIONET","","",0\r\n``` for JIO SIM
  * ```AT+QICSGP=1,1,"airtelgprs.com","","",0\r\n``` for Airtel SIM
  * ```AT+QICSGP=1,1,"portalnmms","","",0\r\n``` for Vodafone SIM
  * ```AT+QICSGP=1,1,"bsnlnet","","",0\r\n``` for Airtel SIM
4. Activate PDP Context: ```AT+QIACT=1\r\n``` 
5. Ping Google to check internet availability: ```AT+QPING=1,"www.google.com"\r\n```
## Implementation
![Alt text](Images/gsmSerial.PNG?raw=true "Title")
## Contributions

For reporting any ```technical issue``` or proposing ```new feature```, please create new [issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-an-issue).


