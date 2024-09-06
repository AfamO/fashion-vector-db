import weaviate;
import os;
from weaviate.classes.init import Auth;
import fashion_data;
from weaviate_connect import ObtainWeaviateDBConnection;
import weaviate.classes as wvc;


try:
    pass
    client = ObtainWeaviateDBConnection();
    client.is_ready();
    products_data = fashion_data.prepareAndgetFashionData();
    print(f"Fashion Data is::{products_data}")
    # Creates Weaviate Connections
    products_collection = client.collections.create(
        name="Products",
        vectorizer_config=wvc.config.Configure.Vectorizer.text2vec_huggingface(
            vectorize_collection_name=True
        )
    );
    products_obj = list();
    
    for i, d in enumerate(products_data):
        products_obj.append({
            "name":d['name'],
            "section":d['section'],
            "family":d['family'],
            "fit":d["fit"],
            "composition":d["composition"],
            "color":d["color"]
        });
    products_collection.data.insert_many(products_obj);
    print("Successfully Indexed Fashion Products Collection to DB");


finally:
    client.close();