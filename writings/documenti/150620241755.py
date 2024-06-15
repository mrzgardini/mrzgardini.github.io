import os

os.system('/usr/bin/rsync -av --delete /media/disco1 /media/disco2/backup/disco1')
os.system('/usr/bin/docker export miniflux > miniflux.tar')
os.system('/usr/bin/docker export radicale > radicale.tar')
os.system('/usr/bin/rsync -av --delete --exclude /home/mrz/disco1 root@calcolatore1:/home/mrz /media/disco2/backup/calcolatore1')
os.system('/usr/bin/rsync -av --delete --exclude /home/mrz/disco1 root@calcolatore2:/home/mrz /media/disco2/backup/calcolatore2')
