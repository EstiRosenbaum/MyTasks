if [ $1 -lt 0 -o $1 -gt 24 ]; then echo "Error!"
elif [[ $1 -lt 12 ]]; then echo "Good morning!" 
elif [ $1 -ge 12 -a $1 -lt 18 ] ; then echo "Good Afternoon!"
else echo "Good evening!"; fi
