import os
import unittest
from azure.identity import ClientSecretCredential
from azure.mgmt.keyvault import KeyVaultManagementClient

class TestTerraformModule(unittest.TestCase):

    def setUp(self):
        subscription_id = os.environ.get('AZURE_SUBSCRIPTION_ID')
        credentials = ClientSecretCredential(
            client_id=os.environ['AZURE_CLIENT_ID'],
            client_secret=os.environ['AZURE_CLIENT_SECRET'],
            tenant_id=os.environ['AZURE_TENANT_ID']
        )
        self.client = KeyVaultManagementClient(credentials, subscription_id)
        # from azure.common.client_factory import get_client_from_cli_profile
        # self.client = get_client_from_cli_profile(KeyVaultManagementClient)

        resource_group = "test"
        keyvault_name = "kitchentestpaulo" # can be tested before using it
        self.keyvault = self.client.vaults.get(resource_group, keyvault_name)

    def test_location(self):
        self.assertEqual(self.keyvault.location, "westeurope")

    def test_softDeleteProrperty(self):
        self.assertEqual(self.keyvault.properties.enable_soft_delete, True)

if __name__ == '__main__':
    unittest.main()
