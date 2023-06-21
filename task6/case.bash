case $1 in
 ( jpg | jpeg )
    echo "It's jpeg."
  ;;
  ( png )
    echo "It's png."
  ;;
  ( gif )
    echo "It's gif."
  ;;
  *)
    echo " $1 It's not image!"
  ;;
esac