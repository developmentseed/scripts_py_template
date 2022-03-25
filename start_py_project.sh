#!/usr/bin/env bash
#This a script to start a simple Python scripts project with docker eviroment.
PROJECT_NAME=$1
######################################################
## Clone project
######################################################

git clone https://github.com/developmentseed/scripts_py_template.git ${PROJECT_NAME}

######################################################
## Rename files
######################################################
cd ${PROJECT_NAME}/
mv scripts_py_template ${PROJECT_NAME}
for filename in ./* ./*/*; do
    if [ -f "$filename" ]; then
        echo $filename
        sed -i -e 's/scripts_py_template/'${PROJECT_NAME}'/g' $filename
        rm $filename-e
    fi
done

######################################################
## Create Readme.md
######################################################
echo ${PROJECT_NAME} >README.md

######################################################
## Remove unnecessary files
######################################################
rm start_py_project.sh

######################################################
## Build Docker
######################################################
docker-compose build

######################################################
## Github section and linters
######################################################
rm -rf .git
git init

######################################################
## Github section and linters
######################################################
pre-commit install
pre-commit run --all-files
