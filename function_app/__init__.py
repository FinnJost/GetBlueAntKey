import logging
import azure.functions as func
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Function triggered.")
    try:
        # Replace with your Key Vault name
        key_vault_url = "https://newblueant.vault.azure.net/"

        # Authenticate using the Managed Identity (this will automatically use Managed Identity in Azure)
        credential = DefaultAzureCredential()

        # Create a client to interact with the Key Vault
        client = SecretClient(vault_url=key_vault_url, credential=credential)

        # Replace with the name of your secret stored in the Key Vault
        secret_name = "BlueAntKey"

        # Retrieve the secret from the Key Vault
        retrieved_secret = client.get_secret(secret_name)

        # Use the secret value
        api_key = retrieved_secret.value

        # Log the retrieved API Key for debugging purposes
        logging.info(f"API Key: {api_key}")

        # Return the API Key (just as an example)
        return func.HttpResponse(f"The API Key is: {api_key}", status_code=200)

    except Exception as e:
        # In case of any errors, log and return a 500 error
        logging.error(f"Error: {str(e)}")
        return func.HttpResponse("Error accessing Key Vault.", status_code=500)
