#!/bin/bash -v
#!/bin/bash -n

echo ${@}
for i in $@; do touch $i.bash ; done
mkdir folder
for j in $@; do mv $j.bash folder ; done
cd folder
ls
set -v
set -n