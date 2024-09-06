import weaviate;
import weaviate.classes as wvc;
from weaviate_connect import ObtainWeaviateDBConnection;

try:
    
    client = ObtainWeaviateDBConnection();
    client.is_ready();
    print(f"Is Client Ready? {client.is_ready()}");
    products = client.collections.get("Products");
    
    response = products.query.near_text(
        query = "Red T-Shirt",
        return_metadata=wvc.query.MetadataQuery(distance = True),
        limit = 2,
        return_properties=["name", "family", "color"]
    )
    #print(f"Result=={response.objects}")
    for o in response.objects:
        print(o.properties);
        print(o.metadata.distance);
    
    pass
finally:
    client.close();