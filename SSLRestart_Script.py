import weblogic.management.mbeanservers.domainruntime
from com.bea.wli.sb.management.configuration import ALSBConfigurationMBean
from java.util import Hashtable
from java.util import *
from javax.management import *
import javax.management.Attribute
print 'starting the script .... '

uname=sys.argv[1]
pword=sys.argv[2]
adminIP=sys.argv[3]
adminPort=int(sys.argv[4])
managedServerList=sys.argv[5]
#split it and make it as a list
managedServers=managedServerList.split(',')
for item in managedServers:
        try:
                connect(username=uname, password=pword, url='t3://'+adminIP+':'+str(adminPort))
                domainRuntime()
                Managedserver=str(item)
                state(Managedserver)
                cd('/ServerRuntimes/'+Managedserver)
                print ' Restarting SSL for Managed Server...'
                cmo.restartSSLChannels() 
        except Exception:
                print 'SSL Restart FAILED () for',adminIP.strip(),',',adminPort.strip(),',Failed'
                disconnect()
print 'End of script ...'
disconnect()
exit()
