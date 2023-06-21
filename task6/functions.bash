Even() {
    space=" "
    if [ $2 -lt $1 ]; then
        return 
    fi
    if [[ $(( $2 % 2)) -eq 0 ]]; then
        Even $1 $(( $2-2 )) 
    else
        Even $1 $(( $2-1 )) 
    fi
    if [[ $(( $2 % 2)) -eq 0 ]]; then
        pr+=$space
        echo -e "$pr" $2 
    fi
    return 
}
main () {
    echo $FUNCNAME
    Even $1 $2
}
main $1 $2
