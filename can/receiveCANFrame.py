#!/usr/bin/env python

"""
This example demonstrates how to use async IO with python-can.
"""

import asyncio
from typing import List

import can
from can.notifier import MessageRecipient

def print_message(msg: can.Message) -> None:
    a= ""
    a += str(msg)
    print(a)
    msg_id = a[a.find('ID:')+3 :a.find('S')]
    print(msg_id)
    can_data = a[a.find('DL:')+3 :a.find('Channel')]
    # print(can_data)
    data_len = int(can_data[0:7])
    # print(data_len)
    can_data1 = can_data[7:7+3*data_len-1]
    array = can_data1.split()

    print(array)
    for x in range(data_len):
        data_byte = int(array[x],16)
        print(data_byte)

async def main() -> None:
    """The main function that runs in the loop."""
    with can.Bus(  # type: ignore
        interface="socketcan",
        channel="can0",
        receive_own_messages=False,
        bitrate = 500000
    ) as bus:
        reader = can.AsyncBufferedReader()
        # logger = can.Logger("logfile.asc")

        listeners: List[MessageRecipient] = [
            print_message,  # Callback function
            reader,  # AsyncBufferedReader() listener
        ]
        # Create Notifier with an explicit loop to use for scheduling of callbacks
        loop = asyncio.get_running_loop()
        notifier = can.Notifier(bus, listeners, loop=loop)
        while True:
            # Wait for message from AsyncBufferedReader
            msg = await reader.get_message()
            await asyncio.sleep(2)



if __name__ == "__main__":
    asyncio.run(main())
