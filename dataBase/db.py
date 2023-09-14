import os
from pymongo import MongoClient, errors


class MongoDB:
    def __init__(self) -> None:
        """
        Initializes the MongoDB client instance with None values.
        """
        self.Client = None
        self.DataBase = None
    def CreateOne(self, object : dict, collection : str, retries = 3):
        """
        Insert a single document into the specified collection.

        Args:
        - object (dict): The document to be inserted.
        - collection (str): The name of the collection into which the document should be inserted.
        - retries (int): Number of times to retry the operation in case of a DuplicateKeyError.

        Returns:
        - ObjectId of the inserted document if successful, None otherwise.
        """
        for attempt in range(retries):
            try:
                collection = self.DataBase[collection]
                result = collection.insert_one(object)
                return result.inserted_id
            except errors.DuplicateKeyError as dke:
                if "_id_" in str(dke):
                    print(f"Attempt {attempt+1}: Duplicate _id error. Retrying...")
                else:
                    print("Duplicate key error on a field other than _id. Not retrying.")
                    return None
            except errors.CollectionInvalid:
                print("Invalid collection name or options.")
                return None
            except errors.WriteError as we:
                # Catch general write errors
                print(f"Write error: {we}")
                return None
            except errors.ServerSelectionTimeoutError:
                # Catch errors related to server selection (e.g., no available servers)
                print("Server selection error. Could not connect to the server.")
                return None
            except errors.PyMongoError as e:
                # Catch any other generic PyMongo errors
                print(f"MongoDB error: {e}")
                return None
    def CreateMany(self, objects: list, collection: str, retries=3):
        """
        Insert multiple documents into the specified collection.

        Args:
        - objects (list): A list of dictionaries representing the documents to be inserted.
        - collection (str): The name of the collection into which the documents should be inserted.
        - retries (int): Number of times to retry the operation in case of a DuplicateKeyError.

        Returns:
        - List of ObjectIds of the inserted documents if successful, None otherwise.
        """
        for attempt in range(retries):
            try:
                coll = self.DataBase[collection]
                result = coll.insert_many(objects)
                return result.inserted_ids
            except errors.BulkWriteError as bwe:
                errors_list = bwe.details.get("writeErrors", [])
                for error in errors_list:
                    if error.get("code") == 11000:
                        if "_id_" in error.get("errmsg", ""):
                            print(f"Attempt {attempt + 1}: Duplicate _id error in bulk write. Retrying...")
                        else:
                            print("Duplicate key error on a field other than _id in bulk write. Not retrying.")
                            return None
            except errors.CollectionInvalid:
                print("Invalid collection name or options.")
                return None
            except errors.WriteError as we:
                # Catch general write errors
                print(f"Write error: {we}")
                return None
            except errors.ServerSelectionTimeoutError:
                # Catch errors related to server selection (e.g., no available servers)
                print("Server selection error. Could not connect to the server.")
                return None
            except errors.PyMongoError as e:
                # Catch any other generic PyMongo errors
                print(f"MongoDB error: {e}")
                return None
    def Connect(self):
        """
        Connects to a MongoDB instance using environment variables for URI and database name.
        
        Utilizes:
        - URI: The connection URI for the MongoDB instance.
        - DBNAME: The name of the database to connect to.
        
        Raises:
        - ValueError: If either the URI or DBNAME environment variables are not set.
        """
        uri = os.environ.get("URI")
        if not uri:
            raise ValueError("URI environment variable not set!")

        dbName = os.environ.get("DBNAME")
        if not dbName:
            raise ValueError("DBNAME environment variable not set!")

        self.Client = MongoClient(uri)
        try:
            self.Client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print("Error connecting to MongoDB.")
            raise e
        self.DataBase = self.Client[dbName]
    def Disconnect(self):
        """
        Disconnects from the current MongoDB instance.
        
        Note:
        - If already disconnected or not connected, this method is safe to call.
        """
        if self.Client:
            self.Client.close()
            print("Disconnected from MongoDB.")