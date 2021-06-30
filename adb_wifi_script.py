import os
import re
import sys


def exec_cmd(cmd):
    cmd = os.popen(cmd)
    cmd_result = cmd.read()
    cmd.close()
    return cmd_result


def start_adb_server():
    os.system("adb start-server")


def filter_device_list(device):
    return device != ''


def get_connected_devices():
    devices_ret = exec_cmd('adb devices')
    device_list = list(filter(filter_device_list, devices_ret.split('\n')))
    del device_list[0]
    final_device_list = []
    for item in device_list:
        final_device_list.append(item.split('device')[0].strip())
    return final_device_list


def check_connection_over_wifi(device_list):
    for item in device_list:
        match_obj = re.search(r'.*?(\d+\.\d+\.\d+\.\d+):.*', item)
        if match_obj and match_obj.group(1):
            return match_obj.group(1)
    return None


def get_device_ip():
    ip_ret = exec_cmd('adb shell ip addr show wlan0')
    math_obj = re.search(r'inet (\d+\.\d+\.\d+\.\d+).*?wlan0', ip_ret)
    if math_obj and math_obj.group(1):
        return math_obj.group(1)
    return None


def connect_device(ip):
    tcpip_ret = exec_cmd('adb tcpip 5555')
    print(tcpip_ret)
    connect_ret = exec_cmd('adb connect ' + ip + ':5555')
    print(connect_ret)


if __name__ == '__main__':
    start_adb_server()

    connected_device_list = get_connected_devices()
    if len(connected_device_list) == 0:
        print('No devices connected, please connect your Android device to your computer via USB.')
        sys.exit(0)

    print('Device id: ' + connected_device_list[0])

    connected_ip = check_connection_over_wifi(connected_device_list)
    if connected_ip is not None:
        disconnect_ret = exec_cmd('adb disconnect ' + connected_ip)
        print(disconnect_ret)
        sys.exit(0)

    wlan0_ip = get_device_ip()

    if wlan0_ip is None:
        print('No IP address available, is your phone in the same Wifi network with your computer?')
        sys.exit(0)

    print("IP address: " + wlan0_ip)

    connect_device(wlan0_ip)
