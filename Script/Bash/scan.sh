#!/bin/bash
p=0
if test $1 = "-p"; then
        p=1
        shift
fi

if test $1 = "-o"; then 
        exec > $2
        shift
        shift
fi

ip=$(echo "$1" | cut -d'/' -f1)
mask=$(echo "$1" | cut -d'/' -f2)

if [[ "$mask" -eq "16" || "$mask" -eq "24" || "$mask" -eq "32" ]]; then
  if [[ $ip =~ ^([0-9]{1,3}\.){3}[0-9]{1,3}$ ]]; then
        ping -c 1 -w 1 "$ip"
        if [ $? -eq 0 ]; then
                echo "La machine $ip/$mask a répondu au ping"
        elif [ $? -ne 0 ] && [ "$p" -eq 1 ]; then
                echo "La machine $ip/$mask n'a pas répondu au ping"
        fi
  else
    echo "L'adresse IP: $ip n'est pas valide."
  fi
else
  echo "Le masque $mask n'est pas valide. Veuillez utiliser un masque égal à 16, 24 ou 32."
fi
