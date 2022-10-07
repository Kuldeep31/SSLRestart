#!/bin/bash

#!/bin/bash
CURRENTPATH=$(cd $(dirname "$0") ; pwd)
cd ${CURRENTPATH}/../../bin
. ./setDomainEnv.sh
cd ${CURRENTPATH}


echo "Restart SSL script starting"
while read line; do
                IFS=';' tokens=( $line)
                java weblogic.WLST SSLRestart_Script.py ${tokens[0]} ${tokens[1]} ${tokens[2]} ${tokens[3]} ${tokens[4]}
done <domain_list.properties
