resource "azurerm_resource_group" "lab" {
  name     = var.resource_group_name
  location = var.location
}

resource "azurerm_storage_account" "insecure" {
  name                     = "aisecuritylab100"
  location                 = azurerm_resource_group.lab.location
  resource_group_name      = azurerm_resource_group.lab.name
  account_tier             = "Standard"
  account_replication_type = "LRS"
  
  public_network_access_enabled = true
}