terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = ">= 3.8"
    }
  }

  backend "azurerm" {
        resource_group_name  = "Cohort28_KamAbo_ProjectExercise"
        storage_account_name = "kamiliastorageaccount"
        container_name       = "m12state"
        key                  = "terraform.tfstate"
  }
}

provider "azurerm" {
  features {}
}

data "azurerm_resource_group" "main" {
  name     = "Cohort28_KamAbo_ProjectExercise"
}

resource "azurerm_service_plan" "main" {
  name                = "${var.prefix}-asp"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  os_type             = "Linux"
  sku_name            = "B1"
}

resource "azurerm_linux_web_app" "main" {
  name                = "${var.prefix}-ka-todoapp"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  service_plan_id     = azurerm_service_plan.main.id

  site_config {
    application_stack {
      docker_image     = "kallya21/todo-app"
      docker_image_tag = "latest"
    }
  }

  app_settings = {
    "DOCKER_REGISTRY_SERVER_URL" = var.docker_registry_server_url
    "SECRET_KEY"                 = var.secret_key
    "PRIMARY_CONNECTION_STRING"  = azurerm_cosmosdb_account.main.primary_mongodb_connection_string
    "MONGO_DB_NAME"              = var.mongo_db_name
    "FLASK_APP"                  = var.flask_app
    "WEBSITES_PORT"              = var.websites_port
    "LOG_LEVEL"                  = var.log_level
    "LOGGLY_TOKEN"               = var.loggly_token
  }
}

resource "azurerm_cosmosdb_account" "main" {
  name                 = "${var.prefix}-todo-app-mongo-account"
  location             = data.azurerm_resource_group.main.location
  resource_group_name  = data.azurerm_resource_group.main.name
  offer_type           = "Standard"
  kind                 = "MongoDB"
  mongo_server_version = "4.2"

  capabilities {
    name = "EnableServerless"
  }

  capabilities {
    name = "EnableMongo"
  }

  consistency_policy {
    consistency_level       = "BoundedStaleness"
    max_interval_in_seconds = 300
    max_staleness_prefix    = 100000
  }

  geo_location {
    location          = "uksouth"
    failover_priority = 0
  }
}

resource "azurerm_cosmosdb_mongo_database" "main" {
  name                = "${var.prefix}-todo-app-db"
  resource_group_name = azurerm_cosmosdb_account.main.resource_group_name
  account_name        = azurerm_cosmosdb_account.main.name

  lifecycle { 
    prevent_destroy = true 
  }
}