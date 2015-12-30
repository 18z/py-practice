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
