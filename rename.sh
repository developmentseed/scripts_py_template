#!/usr/bin/env bash
mv scripts_py_template ${PROJECT_NAME}
for filename in ./* ./*/*
do
    if [ -f "$filename" ]; then
        echo $filename
        sed -i -e 's/scripts_py_template/'${PROJECT_NAME}'/g' $filename
        rm $filename-e
    fi
done
rm -rf .git