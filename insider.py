import subprocess

class insider(object):
    def __init__(self, name):
        self.name = name

    def check_volume(self):
        try:
            volume_state = subprocess.check_output("df -h /home|awk '{print $5}'|tail -n 1|cut -d'%' -f 1", shell = True)
            if int(volume_state) == 70:
                return "volume is full"
            else:
                return "volume is enough use"
        except:
            print "see if df dies"

    def check_ip(self, ip):
        try:
            received = subprocess.check_output("ping "+ ip + \
                " -c 1 |grep -E -o '[0-9]+ received'| cut -f1 -d' '", shell = True)
            if int(received) == 1:
                response = ip + " is Up"
            else:
                response = ip + " is Down"
            return response
        except:
            print "see if ping dies"

    # def check_disk_health(self, hd):
    #     try:
    #         health = subprocess.check_output("sudo smartctl -q errorsonly -H -A -a " + \
    #             hd, shell = True)
    #         good = ""
    #         if health == good:
    #             health_st = "Good"
    #         else:
    #             helth_st = "Bad"
    #         return health_st
    #     except:
    #         print "exit status = 1"

    def check_firewall_log(self):
        try:
            log_num = subprocess.check_output("grep iptables /var/log/syslog|wc -l", shell = True)
            if int(log_num) == 0:
                log_status = "no logs yet"
            else:
                log_status = "logs exits"
            return log_status
        except:
            print "check iptable log"
