echo ${@}
compliment=${@:2:2}
compliment=(I am ${compliment[@]} and $4 )
echo ${compliment[@]}