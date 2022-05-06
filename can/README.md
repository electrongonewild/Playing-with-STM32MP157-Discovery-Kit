# CAN Communication
CAN  stands for Controller Area network. It is an Asynchronous serial communication protocol introduced in 1986 by Robert Bosch.
CAN protocol is a message based protocol not address based means transmitted data is available for all nodes and its receiver’s choice to receive data or not.<br>
In this project, we are going to see the following using STM32MP157x-DK1/2:
* Make changes to device tree to configure fdcan pins for CAN communication
* Flash autorun CAN config files on startup
* Use ```SocketCAN```  module to send and receive CAN frames using can-utils
* Send and receive CAN frames using ```python-can``` 

## Table of Contents
* [Documentation](/can/README.md#documentation)
* [Prerequisites](/can/README.md#prerequisites)
* [Connection Diagram](/can/README.md#connections)
* [Implementation](/can/README.md#implementation)
* [Contributions](/can/README.md#contributions)

## Documentation
It is highly recommended to go through the Documentation first.<br>
Here are direct links for same.<br>
* [Datasheet](https://www.quectel.com/ProductDownload/EC200T.zip) 
## Prerequisites
* Basic knowledge of CAN communication(it's never too late you can checkout this [Link](https://embedclogic.com/can-protocol/))  
## Connections
* Power Supply(5V/3.3V and GND)
## Implementation
- Make changes to device tree to configure fdcan pins for CAN communication
The hardware for this port is m_can1 whose pins are PIN3-FD_CAN1TX(PA12), PIN5-FD_CAN1RX(PA11), more details can be seen in the below image: (Reference:- User Manual for STM32MP157C-DK2)
All M_CAN nodes are described in stm32mp153.dtsi [2] file with disabled status, change the status “disabled” to “okay” as shown below:
## Contributions

For reporting any ```technical issue``` or proposing ```new feature```, please create new [issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-an-issue).


