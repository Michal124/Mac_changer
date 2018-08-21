import subprocess #add python bash initializer
import optparse
import re


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="interface to change its mac addres")
    parser.add_option("-n", "--new_mac", dest="new_mac", help="new mac addres")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not options.new_mac:
        parser.error("[-] Please specify an new mac adddres, use --help for more info")
    return options

def changeMac(interface, new_mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    if_config_result = subprocess.check_output(["ifconfig", interface])
    mac_adress_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", if_config_result)
    if mac_adress_search_result:
        return mac_adress_search_result.group(0)
    else:
        print("[-] Could not read mac address")

options = get_arguments()
current_mac = get_current_mac(options.interface)
print("Current Mac = " + str(current_mac))
changeMac(options.interface, options.new_mac)
current_mac = get_current_mac(options.interface)
print("New Mac = " + str(current_mac))


