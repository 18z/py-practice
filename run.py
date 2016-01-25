from insider import insider
import datetime
import argparse

host = insider("redbull")

#print host.check_ip(raw_input("Enter IP: "))

parser = argparse.ArgumentParser(description='check services.')
parser.add_argument("-v", "--volume", help="print string")
args = parser.parse_args()

if args.volume == "check":
    print host.check_volume()

#print host.check_firewall_log()
