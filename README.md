# Basic template to start a python scripts

This is a template to quickly start a python scripting projects in a docker container. In the data-team we continuously write scripts, we have created this template to standardize our code and follow the best practices in python coding.

## Template

```sh
git clone git@github.com:developmentseed/scripts_py_template.git
export project_name=abc_scripts
## Rename folders
mv scripts_py_template ${project_name}
mv ${project_name}/scripts_py_template ${project_name}/${project_name}
## Remove .git folder
cd ${project_name} 
rm -rf .git

```
