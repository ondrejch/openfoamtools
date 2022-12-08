#!/bin/bash
#
# Removes all timesteps but the latest in a decomposed case
#
# Ondrej Chvala, ondrejch@gmail.com
#
#
command -v foamListTimes >/dev/null && continue || { echo "OpenFOAM not loaded."; exit 1; }

last_time=$(foamListTimes -latestTime -processor)

echo "Last time: $last_time"

for t in $(foamListTimes  -processor) ; do
    if [ $t != $last_time ] ; then
        echo $t
        if [ "$1" == "del" ] ; then
            rm -rf processor*/$t/
        fi
    fi
done

if [ "$1" != "del" ] ; then
   echo "To remove the timesteps, add 'del' command line argument"
fi

