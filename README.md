# Template to start python script project

This is a template to quickly start a python scripting projects in a docker container. In the data-team we continuously write scripts, we have created this template to standardize our code and follow the best practices in python coding.

## How to install?

Requirements on your operating system:

- [docker](https://www.docker.com/)
- [ docker-compose](https://docs.docker.com/compose/)
- [git](https://github.com/git-guides/install-git)
- [pre-commit](https://pypi.org/project/pre-commit/)

```sh
export PROJECT_NAME=kiara_project
curl -s https://raw.githubusercontent.com/developmentseed/scripts_py_template/main/start_py_project.sh | bash /dev/stdin ${PROJECT_NAME}
```
