# Basic template to start a python scripts

This is a template to quickly start a python scripting projects in a docker container. In the data-team we continuously write scripts, we have created this template to standardize our code and follow the best practices in python coding.

## Template

```sh
    git clone git@github.com:developmentseed/abc_scripts.git
    export PROJECT_NAME=kiara
    ## Rename folders and files
    mv scripts_py_template ${PROJECT_NAME}
    ## Remove .git folder
    cd ${PROJECT_NAME}
    ./project.sh
```
