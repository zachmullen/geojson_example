import girder_client
import girder_worker_utils
from script import largest_counties

API_KEY='8wqEZFR2aqwIZVLJbAPLK4zwq09NK3rV9ToyYD59'  # Set to your own API key
ITEM_ID='59a1ad244f2ae50460333137'  # Set to your own item ID

client = girder_client.GirderClient(apiUrl='https://resonant-demo.kitware.com/api/v1')
client.authenticate(apiKey=API_KEY)
girder_worker_utils.set_item_task(client=client, item_id=ITEM_ID, fn=largest_counties)
