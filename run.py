from insider import insider
import datetime

host = insider("redbull")

#print host.check_ip(raw_input("Enter IP: "))

#print host.check_volume()

print host.check_firewall_log()
