data "azurerm_resource_group" "example" {
  name     = "test"
}

data "azurerm_client_config" "current" {}

resource "azurerm_key_vault" "example" {
  name                        = "kitchentestpaulo"
  location                    = data.azurerm_resource_group.example.location
  resource_group_name         = data.azurerm_resource_group.example.name
  tenant_id                   = data.azurerm_client_config.current.tenant_id
  enabled_for_disk_encryption = true
  soft_delete_enabled         = true
  soft_delete_retention_days  = 7
  purge_protection_enabled    = false

  sku_name = "standard"
  tags = {
    environment = "Testing"
  }
}