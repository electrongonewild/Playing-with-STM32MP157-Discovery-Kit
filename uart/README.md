# UART Protocol
UART stands for Universal Asynchronous Receiver/Transmitter. It is a dedicated hardware associated with serial communication. UART is used in many applications like GPS Receivers, Bluetooth Modules, GSM and GPRS Modems, Wireless Communication Systems, RFID based applications etc.<br>
In this project, we are going to see the following using STM32MP157x-DK1/2:
* Make changes to device tree to configure pins for UART communication
* Send and receive data via UART using ```serial``` library in python 

## Table of Contents
* [Documentation](/uart/README.md#documentation)
* [Prerequisites](/uart/README.md#prerequisites)
* [Connection Diagram](/uart/README.md#connections)
* [Getting Started](/uart/README.md#getting-started)
* [Implementation](/uart/README.md#implementation)
* [Contributions](/uart/README.md#contributions)

## Documentation
It is highly recommended to go through the Documentation first.<br>
Here are direct links for same.<br>
* [st-wiki](https://wiki.stmicroelectronics.cn/stm32mpu/wiki/Getting_started)
* [Databrief](https://www.st.com/resource/en/data_brief/stm32mp157d-dk1.pdf)
* [Documentation](https://www.st.com/en/evaluation-tools/stm32mp157d-dk1.html#documentation)
## Prerequisites
* Basic knowledge of UART communication
## Connections
* Power Supply(5V/3.3V and GND)
## Getting Started
Follow the steps for getting started:
* Now you can further proceed according to your application.
## Implementation
* **Working directory:** STM32MPU_workspace/STM32MP15-Ecosystem-v2.0.0/Developer-Package/stm32mp1-openstlinux-5.10-dunfell-mp1-21-11-17/sources/arm-ostl-linux-gnueabi/linux-stm32mp-5.10.61-stm32mp-r2-r0/linux-5.10.61/arch/arm/boot/dts . <br>
* Changes in device tree to configure uart pins for UART communication. Open stm32mp157a-dk1.dts and add the following lines
```
&usart3 {
    pinctrl-names = "default", "sleep";
    pinctrl-0 = <&usart3_pins_b>;
    pinctrl-1 = <&usart3_sleep_pins_b>;
    status = "okay";
};
```
* Open file stm32mp15xx-dkx, make the following changes i.e. add uart3 as serial1.
```
	aliases {
		ethernet0 = &ethernet0;
		serial0 = &uart4;
		serial1 = &usart3;
	};
 ``` 
* These configurations are for pins ```PB10(USART3_TX)``` and ```PB12(USART3_RX)``` on GPIO connector
## Contributions

For reporting any ```technical issue``` or proposing ```new feature```, please create new [issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-an-issue).


