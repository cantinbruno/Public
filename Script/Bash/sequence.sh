#!/bin/bash

error=0

for dir in "$@"
do
    if [[ ! -d $dir ]]; then
        echo "$dir n'est pas un répertoire, ignoré." >&2
        error=1
    else
        if [[ $(ls -A $dir) ]]; then
            echo "Le répertoire $dir n'est pas vide, ignoré." >&2
        else
            read -p "Le répertoire $dir est vide, voulez-vous le supprimer (o/n) ? " response
            if [[ $response =~ ^[Oo]$ ]]; then
                rm -r $dir
                echo "Le répertoire $dir a été supprimé."
            else
                echo "Le répertoire $dir n'a pas été supprimé."
            fi
        fi
    fi
done

exit $error
