# ADBWifiScript
A python script that runs several adb commands to connect the Android device over wifi.

## Environment:

Python 2/3, ADB tools.

## Phone Setting:

USB debug mode must be turned on in the Developer options from phone setting.

Connect your Android device to your PC with data cable, and make sure they are in the same Wifi network.
Then execute this script, the script will obtain the IP address of your phone via adb command,
and connect your phone to your PC over Wifi. Last, the wireless debugging is available.

## The used adb commands in this script:

`adb version`

`adb start-server`

`adb devices`

`adb shell ip addr show wlan0`

`adb tcpip {port}`

`adb connect {ip}:{port}`

`adb disconnect {ip}:{port}`

## ADB commands reference:

https://adbshell.com/commands

## Screenshots:

### connected:
![Connected](https://raw.githubusercontent.com/congshengwu/ADBWifiScript/master/connected.png)

### disconnected:
![Disconnected](https://raw.githubusercontent.com/congshengwu/ADBWifiScript/master/disconnected.png)
