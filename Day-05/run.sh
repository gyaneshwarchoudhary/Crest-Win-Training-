#!/bin/sh

echo "enter the command you want to run and save into a file"
read command 

output_file="command_output.txt"

if eval "$command" > "$output_file" 2>&1; then
    echo "Successfully executed '$user_command'"
    echo "Output saved to '$output_file'"
else
    echo "Failed to execute '$user_command'"
    echo "Error details saved to '$output_file'"
fi
