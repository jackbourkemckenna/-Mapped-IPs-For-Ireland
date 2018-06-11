import subprocess
print "start"
subprocess.call("/var/www/html/python/shit/masscan/bin/masscan -c /var/www/html/python/shit/masscan/bin/scanConf.conf -oX /var/www/html/python/shit/masscan/bin/scan.xml ",  shell=True)
print "end"
