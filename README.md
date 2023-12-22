# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.8+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

In order to populate the `TRELLO_KEY`, `TRELLO_TOKEN`, `BOARD_ID`, `TO_DO_LIST_ID` and `DONE_LIST_ID` variables, you will need to create a Trello account [here](https://trello.com/signup). Follow [these instructions](https://trello.com/app-key) to get the values for the `TRELLO_KEY` and `TRELLO_TOKEN`. Create a Trello board with a to do list and a done list in order to get the `BOARD_ID`, `TO_DO_LIST_ID` and `DONE_LIST_ID`.

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Running the Tests

In order to run the unit and integration tests from a terminal, ensure that you navigate to the route folder and install pytest by running the following command:
```bash
$ poetry install pytest
```
Once pytest is installed, you can run all of the tests using the following command:
```bash
$ poetry run pytest
```
To run all the tests in a specific test file, run the following command:
```bash
$ poetry run pytest path/to/test_file.py
```
To run a specific test function within a test file, run the following command:
```bash
$ poetry run pytest path/to/test_file.py::test_function_name
```
## Building and Running Containers

### Development Container
Ensure you have Docker installed and properly configured on your machine before running these commands.

To build the development container, run the following command:
```bash
$ docker build --target development --tag todo-app:dev .
```
Run the development container, mounting the project for Flask auto-reloading using the following command:
```bash
$ docker run --env-file .env -p 5100:80 --mount type=bind,source="$(pwd)"/todo_app,target=/app/todo_app todo-app:dev
```
### Production Container
To build the production container, run the following command:
```bash
$ docker build --target production --tag todo-app:prod .
```
Run the production container using the following command:
```bash
$ docker run --env-file .env -p 8000:8000 todo-app:prod
```
### Test Container
The test container is used to run the unit and integration tests for the To Do App. To build the test container, run the following command:
```bash
$ docker build --target test --tag my-test-image .
```
Run the test container using the following command:
```bash
$ docker run --env-file .env.test  my-test-image
```