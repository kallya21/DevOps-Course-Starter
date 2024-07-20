variable "prefix" {
  description = "The prefix used for all resources in this environment"
}

variable "docker_registry_server_url" {
  description = "Url for docker registry server"
  type        = string
}

variable "secret_key" {
  description = "Secret key for the web application"
  type        = string
  sensitive   = true
}

variable "mongo_db_name" {
  description = "Name for the MongoDB database"
  type        = string
}

variable "flask_app" {
  description = "Path to the Flask app"
  type        = string
}

variable "websites_port" {
  description = "Port website is hosted on"
  type        = string
}

variable "log_level" {
  description = "Log level for logs"
  type        = string
}

variable "loggly_token" {
  description = "Token for Loggly"
  type        = string
  sensitive   = true
}