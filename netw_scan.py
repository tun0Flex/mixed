import scapy.all as scapy
import optparse
from colorama import Fore,init
from scapy.ansmachine import AnsweringMachine

#netw_scan.py -i  111.111.111.111/24
def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--ipadress", dest="ip_adress", help="enter ip adress")
    (user_input,arguments) = parse_object.parse_args()
    if not user_input.ip_adress:
        print(f"{Fore.RED}Enter IP Adress !!")
    return user_input

def scan_network(ip):
    arp_request_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packet = broadcast_packet/arp_request_packet
    (answered_list,unanswered_list) = scapy.srp(combined_packet , timeout=2)
    answered_list.summary()

scan_network(get_user_input().ip_adress)