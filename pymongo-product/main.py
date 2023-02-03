from dotenv import load_dotenv
from fastapi import FastAPI
from mongo_db_manager import MongoDbManager
import os

load_dotenv()

def main():
  
    print(os.getenv("MONGO_URI"))
    print(os.getenv("MONGO_DBNAME"))
    MongoDbManager.initialize(os.getenv("MONGO_URI"),os.getenv("MONGO_DBNAME"))
    
    #result=MongoDbManager.find_one('products')
    
    
    result=MongoDbManager.find('products',{'platformId':'woocommerce'})
         
    #print(result)
    
    
    
    print(MongoDbManager.count('products',{'platformId':"'woocommerce'"}))
    
    for doc in MongoDbManager.find('products',{'platformId':"'woocommerce'"}):
        print(doc)
    
if __name__ == "__main__":
    main()
    
#app = FastAPI()


