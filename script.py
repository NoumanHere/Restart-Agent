from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication

# Replace with your organization URL
organization_url = 'http://or-url-here'


# Replace with your personal access token (PAT)
personal_access_token = "pat_here"

# Create a connection object
credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)

agent_client = connection.clients.get_task_agent_client()

# Agent and Pool ID here
agent_pool_id = 283  
agent_id=371
# Restart the agent
# Get the agent
agent = agent_client.get_agent(pool_id=agent_pool_id, agent_id=agent_id)

# Update the agent status
agent.status = "offline"
agent_client.update_agent(pool_id=agent_pool_id, agent_id=agent_id, agent=agent)

# Update the agent back to "online"
agent.status = "online"
agent_client.update_agent(pool_id=agent_pool_id, agent_id=agent_id, agent=agent)
