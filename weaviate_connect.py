import weaviate;
import os;
from weaviate.classes.init import Auth;
import fashion_data;
from weaviate.classes.config import Configure as wvc;


print("Connecting to Weaviate...")

weaviate_api_url = os.environ["WCD_DEMO_URL"];
weaviate_api_key = os.environ["WCD_DEMO_RO_KEY"];
huggingface_api_token = os.environ["HUGGING_FACE_TOKEN"];


def ObtainWeaviateDBConnection():
    client = weaviate.connect_to_weaviate_cloud(
    cluster_url=weaviate_api_url,
    auth_credentials=Auth.api_key(weaviate_api_key),
    headers={
        "X-HuggingFace-Api-Key":huggingface_api_token
    }
    );
    client.is_ready();
    print("Successfully Connected to Weaviate DB");
    return client;