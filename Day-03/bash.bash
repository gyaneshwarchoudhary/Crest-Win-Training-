#!/bin/bash

MESSAGE="Starting the counter"
echo $MESSAGE


echo "Enter a number greater than 0:"
read LIMIT

if [ $LIMIT -gt 0 ]; then
    echo "now i will count to $LIMIT."
    
    for (( i=1; i<=$LIMIT; i++ )); do
        echo "Number: $i"
    done

else
    echo "Error: not a postive number"
fi

echo "done 🔥🔥"