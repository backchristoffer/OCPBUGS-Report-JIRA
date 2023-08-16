# ocpbugpull

pulls ocpbugs from csv report

## How to use with docker - EXAMPLE
In this example, csvtest1.csv is located in /tmp and mounted to /app/csv in the container WITH --privileged so please be aware. This is just an example of how you could use it with a container, it's not a recommendation. 

$ docker run -v /tmp:/app/csv --privileged ghcr.io/backchristoffer/ocpbugpull:latest -f /app/csv/csvtest1.csv

## How to use with binary ocpbugpull
If you get permission denied: chmod 755 ocpbugpull

$ ./ocpbugpull -f csvtest1.csv
