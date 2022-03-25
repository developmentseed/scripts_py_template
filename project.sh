#!/usr/bin/env bash
######################################################
## Rename files
######################################################
mv scripts_py_template ${PROJECT_NAME}
for filename in ./* ./*/*; do
    if [ -f "$filename" ]; then
        echo $filename
        sed -i -e 's/scripts_py_template/'${PROJECT_NAME}'/g' $filename
    fi
done

######################################################
## Create Readme.md
######################################################
echo ${PROJECT_NAME} >README.md

######################################################
## Github section and linters
######################################################
rm -rf .git
git init
