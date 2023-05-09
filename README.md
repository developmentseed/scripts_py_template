# Template to start python script project

This is a template designed to help you quickly start a Python scripting project in a Docker container. It follows best practices in Python coding and provides a standardized structure for organizing your code. This template was created by our team to help us streamline our coding process and maintain consistency across projects.

## How to install?

Operating system requirements
- [docker](https://www.docker.com/)
- [docker-compose](https://docs.docker.com/compose/)
- [git](https://github.com/git-guides/install-git)
- [pre-commit](https://pypi.org/project/pre-commit/)


```sh
export PROJECT_NAME=kiara_project
curl -s https://raw.githubusercontent.com/developmentseed/scripts_py_template/main/start_py_project.sh | bash /dev/stdin ${PROJECT_NAME}
```

**Note:**

Use underscores (`_`) in `PROJECT_NAME` when separating words, example `web_crawler` or `kiara_project`
