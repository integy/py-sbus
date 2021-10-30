# sbusPythonDriver
a Python driver for the SBUS protocol

derivated from
- [fifteenhex/python-sbus](https://github.com/fifteenhex/python-sbus)
- [Sokrates80/sbus_driver_micropython git hub](https://github.com/Sokrates80/sbus_driver_micropython)
- [https://os.mbed.com/users/Digixx/code/SBUS-Library_16channel/file/83e415034198/FutabaSBUS/FutabaSBUS.cpp/](os.mbed.com/users/Digixx/code/SBUS-Library_16channel)
- [https://os.mbed.com/users/Digixx/notebook/futaba-s-bus-controlled-by-mbed/](os.mbed.com/users/Digixx/notebook/futaba-s-bus-controlled-by-mbed/)
- [https://www.ordinoscope.net/index.php/Electronique/Protocoles/SBUS](ordinoscope.net/index.php/Electronique/Protocoles/SBUS)

This allow you to connect an SBUS receiver to your pi/jetson/computer (or any UART compatible port) and decode values

It supports 16 standard Channels plus 2 digitals.

It has been tested only on the below receivers:
- X8R
- XM+

Also work on TBS receivers with ni-sbus

You can check the example.py to use the library
You will need to install pyserial-asyncio and asyncio to use this library

