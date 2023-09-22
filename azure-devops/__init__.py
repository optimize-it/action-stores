from kubiya import ActionStore
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

logger.info("Loading Azure DevOps action store")
action_store = ActionStore("azure-devops", "0.1.0")

action_store.uses_secrets(["AZURE_CLIENT_SECRET", "AZURE_CLIENT_ID", "AZURE_TENANT_ID", "AZURE_SUBSCRIPTION_ID"])

logger.info("Connected to Azure Compute API")