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

In order to populate the `PRIMARY_CONNECTION_STRING`, `MONGO_DB_NAME`, you will need to create a CosmosDB instance in Azure in order to create a MongoDB database. Once you have created a MongoDB instance, you can find the `PRIMARY_CONNECTION_STRING` for your CosmosDB cluster under Settings -> Connection String from your CosmosDB account page in the Azure portal, or via the CLI:
```bash
$ az cosmosdb keys list -n <cosmos_account_name> -g <resource_group_name> --type connection-strings
```
You can populate the `MONGO_DB_NAME` with the name you want to give your MongoDB database.

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
## Manual Deployment
Find the Docker images for this project [here](https://hub.docker.com/repository/docker/kallya21/todo-app/).
### Release Docker Image to DockerHub
To release the Docker image to DockerHub, you first need to build the production container using the following command:
```bash
$ docker build --target production --tag kallya21/todo-app:prod .
```
Then you need to push the image to docker using the following command:
```bash
$ docker push kallya21/todo-app:prod
```
### Deploy App on Azure
#### Get the Webhook URL:
Ensure you have Terraform and Azure CLI installed and run the following command to log into Azure: 
```bash
$ az login
```
Navigate to the terraform folder and run the following command:
```bash
$ terraform init
```
Once that command has run successfully run the following:
```bash
$ terraform apply
```
This should output the obfuscated webhook url.
#### Test the Webhook:
Run the following command:
```bash
$ curl -dH -X POST "$(terraform output -raw cd_webhook)"
```
Upon successfully triggering the webhook, you should receive a link to a log-stream related to the re-pulling of the image and restarting the app. Find the deployed website [here](https://terraformed-ka-todoapp.azurewebsites.net/).

## Encryption Status
Encryption-at-rest is a security measure used for persisted data, such as data stored on hard drives, solid-state drives (SSDs), databases, or cloud storage. It involves encrypting the data before it is written to the storage medium, ensuring that the data remains encrypted while at rest or not actively being accessed.

Azure Cosmos DB stores its primary databases on SSDs. It uses AES-256 encryption on all regions where the account is running. Encryption-at-rest is "on" by default. There are no controls to turn it off or on. For more detailed information on encryption-at-rest in CosmosDB, refer to the [official Microsoft documentation](https://learn.microsoft.com/en-us/azure/cosmos-db/database-encryption-at-rest).