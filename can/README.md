# CAN Communication
CAN  stands for Controller Area network. It is an Asynchronous serial communication protocol introduced in 1986 by Robert Bosch.
CAN protocol is a message based protocol not address based means transmitted data is available for all nodes and its receiver’s choice to receive data or not.<br>
In this project, we are going to see the following using STM32MP157x-DK1/2:
* Make changes in device tree to configure fdcan pins for CAN communication
* Flash autorun CAN config files on startup
* How to trace
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
* <b>Changes in device tree to configure fdcan pins for CAN communication</b><br>
   The hardware for this port is m_can1 whose pins are PIN3-FD_CAN1TX(PA12), PIN5-FD_CAN1RX(PA11)<br>
   All M_CAN nodes are described in stm32mp153.dtsi file with disabled status, change the status “disabled” to “okay” as shown below:<br><br>
   ```
   m_can1: can@4400e000 {
     compatible = "bosch,m_can";                       
     reg = <0x4400e000 0x400>, <0x44011000 0x1400>;   
     reg-names = "m_can", "message_ram";
     interrupts = <GIC_SPI 19 IRQ_TYPE_LEVEL_HIGH>,
              <GIC_SPI 21 IRQ_TYPE_LEVEL_HIGH>;
     interrupt-names = "int0", "int1";
     clocks = <&rcc CK_HSE>, <&rcc FDCAN_K>;
     clock-names = "hclk", "cclk";
     bosch,mram-cfg = <0x0 0 0 32 0 0 2 2>;
     status = "okay";
   };
 
 Build .dtbs, Push the devicetree into the board.<br>
 Make sure to connect an external CAN transceiver circuit for communicating over a CAN bus.<br><br>
![Alt text](https://github.com/electrongonewild/Playing-with-STM32MP157-Discovery-Kit/blob/main/Images/CANOverview.PNG?raw=true "Title")<br>
(Image referred from [STWiki official website](https://wiki.st.com/stm32mpu/wiki/CAN_overview))
* <b>Flash autorun CAN config files on startup</b><br><br>
   Execute following commands:<br>
   -```Board $> cd /etc/profile.d/```<br>
   -```Board $> nano weston.sh```<br><br>
   Paste the following lines along with already present code at last to enable CAN with bit rate 500kpbs:<br>
   ```
      ip link set can0 down
      ip link set can0 up type can bitrate 500000
      ip link set can0 up
   ```
   Press CTRL+S and CTRL+X to save and exit the text editor.<br>
* <b>How to trace</b><br><br>
   CAN Framework, specifically M_CAN driver, print out info and error messages. You can display them with dmesg command:<br>
   -```Board $>  dmesg | grep m_can```<br>
   ```
      [    1.327824] m_can 4400e000.can: m_can device registered (irq=30, version=32)
      [   25.560759] m_can 4400e000.can can0: bitrate error 0.3%
      [   25.564630] m_can 4400e000.can can0: bitrate error 1.6%
   ```
*<b>Use ```SocketCAN```  module to send and receive CAN frames using can-utils<br>
   

## Contributions

For reporting any ```technical issue``` or proposing ```new feature```, please create new [issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-an-issue).


