### Description
Will take column "Resource URL" from a .csv and format that into a JIRA query like this. 
~~~
project = OCPBUGS AND issuekey in (OCPBUGS-1234, OCPBUGS-1234, OCPBUGS-1234, OCPBUGS-1234, OCPBUGS-1234, OCPBUGS-1234, OCPBUGSM-1234)
~~~
### How to use
~~~
./ocpbr -project=RHEL,OCPBUGS,RHEPLAN data.csv
~~~