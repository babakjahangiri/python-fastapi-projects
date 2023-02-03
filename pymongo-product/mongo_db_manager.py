import pymongo

class MongoDbManager(object):
    _db = None

    @staticmethod
    def initialize(uri:str,dbname:str):
        client = pymongo.MongoClient(uri)
    
        print('Connecting ..')
        try:
            client.admin.command('ping')
            print('Server is available')
            MongoDbManager._db = client[dbname]
        except pymongo.errors.ConnectionFailure as err:
            print (err)
        
    @staticmethod
    def insert(collection,document):
       return MongoDbManager._db[collection].insert_one(document)
       
    @staticmethod
    def insert_many(collection,documents):
       return MongoDbManager._db[collection].insert_many(documents)
        
    @staticmethod
    def find_one(collection,query=None):
       return MongoDbManager._db[collection].find_one(query)

    @staticmethod
    def find(collection,query):
       return MongoDbManager._db[collection].find(query)

    @staticmethod
    def count(collection,query):
        return MongoDbManager._db[collection].count_documents(query)


    @staticmethod
    def aggregate(collection,pipline):
        return MongoDbManager._db[collection].aggregate(pipline)
        
        
    @staticmethod
    def explain_aggregate(collection,pipline):
        return MongoDbManager._db.command('aggregate',collection,pipline=pipline,explain=True)
          
          
            
       
        