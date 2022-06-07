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
* [python-can lib](https://python-can.readthedocs.io/en/master/)
* [STWiki official website](https://wiki.st.com/stm32mpu/wiki/CAN_overview)
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
   ```Board $>  dmesg | grep m_can```<br>
   ```
      [    1.327824] m_can 4400e000.can: m_can device registered (irq=30, version=32)
      [   25.560759] m_can 4400e000.can can0: bitrate error 0.3%
      [   25.564630] m_can 4400e000.can can0: bitrate error 1.6%
   ```
* <b>Use ```SocketCAN```  module to send and receive CAN frames using can-utils</b><br><br>  
   The available CAN devices are listed in /sys/class/net/:<br> 
   ```Board $>  ls /sys/class/net```<br>
   ```
      can0  eth0                 /* can0 interface is available but not necessarily active */
   ```
   One can also display all the available network interfaces to find out the available CAN devices:<br>
   ```Board $>  ifconfig -a```<br>
   ```
      can0      Link encap:UNSPEC  HWaddr 00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00
                NOARP  MTU:16  Metric:1
                RX packets:0 errors:0 dropped:0 overruns:0 frame:0
                TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
                collisions:0 txqueuelen:10
                RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
                Interrupt:30

      eth0      Link encap:Ethernet  HWaddr 00:80:E1:42:45:EC
                UP BROADCAST MULTICAST  MTU:1500  Metric:1
                RX packets:0 errors:0 dropped:0 overruns:0 frame:0
                TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
                collisions:0 txqueuelen:1000
                RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
                Interrupt:54 Base address:0x6000
   ```
   
   Configure the available SocketCAN interface using the ip link command line as follow:<br>
   ```Board $>  ip link set can0 type can bitrate 1000000 dbitrate 2000000 fd on```<br>
   ```
      [ 78.700698] m_can 4400e000.can can0: bitrate error 0.3%
      [ 78.704568] m_can 4400e000.can can0: bitrate error 1.6%
   ```
   To list CAN user-configurable options, use the following command line: <br>
   ```Board $>  ip link set can0 type can help```<br>
   ```
      Usage: ip link set DEVICE type can
        [ bitrate BITRATE [ sample-point SAMPLE-POINT] ] |
        [ tq TQ prop-seg PROP_SEG phase-seg1 PHASE-SEG1
          phase-seg2 PHASE-SEG2 [ sjw SJW ] ]

        [ dbitrate BITRATE [ dsample-point SAMPLE-POINT] ] |
        [ dtq TQ dprop-seg PROP_SEG dphase-seg1 PHASE-SEG1
          dphase-seg2 PHASE-SEG2 [ dsjw SJW ] ]

        [ loopback { on | off } ]
        [ listen-only { on | off } ]
        [ triple-sampling { on | off } ]
        [ one-shot { on | off } ]
        [ berr-reporting { on | off } ]
        [ fd { on | off } ]
        [ fd-non-iso { on | off } ]
        [ presume-ack { on | off } ]

        [ restart-ms TIME-MS ]
        [ restart ]

        Where: BITRATE  := { 1..1000000 }
                  SAMPLE-POINT  := { 0.000..0.999 }
                  TQ            := { NUMBER }
                  PROP-SEG      := { 1..8 }
                  PHASE-SEG1    := { 1..8 }
                  PHASE-SEG2    := { 1..8 }
                  SJW           := { 1..4 }
                  RESTART-MS    := { 0 | NUMBER }
   ```
   To get a detailed status of the SocketCAN link, use the following command line: <br>
    ```Board $> ip -details link show can0```<br>
    ```
      2: can0: <NOARP,ECHO> mtu 72 qdisc pfifo_fast state DOWN mode DEFAULT group default qlen 10
          link/can  promiscuity 0
          can <FD> state STOPPED (berr-counter tx 0 rx 0) restart-ms 0
                bitrate 996078 sample-point 0.745
                tq 19 prop-seg 18 phase-seg1 19 phase-seg2 13 sjw 1
                m_can: tseg1 2..256 tseg2 1..128 sjw 1..128 brp 1..512 brp-inc 1
                dbitrate 2032000 dsample-point 0.720
                dtq 19 dprop-seg 8 dphase-seg1 9 dphase-seg2 7 dsjw 1
                m_can: dtseg1 1..32 dtseg2 1..16 dsjw 1..16 dbrp 1..32 dbrp-inc 1
                clock 50800000numtxqueues 1 numrxqueues 1 gso_max_size 65536 gso_max_segs 65535
   ```
   Then enable the connection by bringing the SocketCAN interface up: <br>
    ```Board $> ip link set can0 up```<br>
   You can check that the interface is up by printing the netlink status:<br>
    ```Board $> ip -details link show can0```<br>
    ```
      2: can0: <NOARP,UP,LOWER_UP,ECHO> mtu 72 qdisc pfifo_fast state UNKNOWN mode DEFAULT group default qlen 10
          link/can  promiscuity 0
          can <FD> state ERROR-ACTIVE (berr-counter tx 0 rx 0) restart-ms 0
                bitrate 996078 sample-point 0.745
      ...
   ```
   One can disable the connection by bringing the SocketCAN interface down. This command is useful when you need to reconfigure the SocketCAN interface: <br>
    ```Board $>  ip link set can0 down```<br>
    
    To send a single frame, use the cansend utility: <br>
     ```Board $> cansend can0 123#1122334455667788```<br>
    To print help on cansend utility: <br>
    ```
    Board $>  cansend -h
   Usage: cansend <device> <can_frame>
   ```
    To display in real-time the list of messages received on the bus, use the candump utility: <br>
     ```Board $>   candump can0```<br>
     ```
      can0  123   [8] 11 22 33 44 55 66 77 88
     ```
     To print help on candump utility: <br>
      ```Board $>   candump -h```<br>
     ```
      Usage: candump [options] <CAN interface>+
         (use CTRL-C to terminate candump)

      Options: -t <type>   (timestamp: (a)bsolute/(d)elta/(z)ero/(A)bsolute w date)
               -c          (increment color mode level)
               -i          (binary output - may exceed 80 chars/line)
               -a          (enable additional ASCII output)
               -S          (swap byte order in printed CAN data[] - marked with '`' )
               -s <level>  (silent mode - 0: off (default) 1: animation 2: silent)
               -b <can>    (bridge mode - send received frames to <can>)
               -B <can>    (bridge mode - like '-b' with disabled loopback)
               -u <usecs>  (delay bridge forwarding by <usecs> microseconds)
               -l          (log CAN-frames into file. Sets '-s 2' by default)
               -L          (use log file format on stdout)
               -n <count>  (terminate after receiption of <count> CAN frames)
               -r <size>   (set socket receive buffer to <size>)
               -D          (Don't exit if a "detected" can device goes down.
               -d          (monitor dropped CAN frames)
               -e          (dump CAN error frames in human-readable format)
               -x          (print extra message infos, rx/tx brs esi)
               -T <msecs>  (terminate after <msecs> without any reception)

      Up to 16 CAN interfaces with optional filter sets can be specified on the commandline in the form: <ifname>[,filter]*

      Comma separated filters can be specified for each given CAN interface:
       <can_id>:<can_mask> (matches when <received_can_id> & mask == can_id & mask)
       <can_id>~<can_mask> (matches when <received_can_id> & mask != can_id & mask)
       #<error_mask>       (set error frame filter, see include/linux/can/error.h)
       [j|J]               (join the given CAN filters - logical AND semantic)

      CAN IDs, masks and data content are given and expected in hexadecimal values.
      When can_id and can_mask are both 8 digits, they are assumed to be 29 bit EFF.
      Without any given filter all data frames are received ('0:0' default filter).

      Use interface name 'any' to receive from all CAN interfaces.

      Examples:
      candump -c -c -ta can0,123:7FF,400:700,#000000FF can2,400~7F0 can3 can8
      candump -l any,0~0,#FFFFFFFF    (log only error frames but no(!) data frames)
      candump -l any,0:0,#FFFFFFFF    (log error frames and also all data frames)
      candump vcan2,92345678:DFFFFFFF (match only for extended CAN ID 12345678)
      candump vcan2,123:7FF (matches CAN ID 123 - including EFF and RTR frames)
      candump vcan2,123:C00007FF (matches CAN ID 123 - only SFF and non-RTR frames)
     ```
* <b>Send and receive CAN frames using ```python-can```</b><br><br>
   Brief example of the library in action: connecting to a CAN bus, creating and sending a message:<br>
   ```testCAN.py

   ```
## Contributions

For reporting any ```technical issue``` or proposing ```new feature```, please create new [issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-an-issue).


