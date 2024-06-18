from os import getenv

from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient


class Database:



    # Develop a database interface class
    def __init__(self):

        # Load environment variables
        load_dotenv()
        db_url = getenv("DB_URL")
        # Connect to the database
        self.database = MongoClient(db_url, tlsCAfile=where())["Database"]
        self.collection = self.database.get_collection("Collection")

    def seed(self, amount=1000):
        # Populate the database with a specified amount of Monsters
        self.collection.insert_many([Monster().to_dict() for _ in range(amount)])

        return 'Seed successful'
    
    def reset(self):
        # Delete all documents from the collection
        return self.collection.delete_many({})

    def count(self) -> int:
        # Return the number of documents in the collection
        return self.collection.count_documents({})

    def dataframe(self) -> DataFrame:
        # Return a DataFrame excluding the _id field
        df = DataFrame(self.collection.find({}, {"_id": False}))
        return df

    def html_table(self) -> str:
        # Return an HTML table representation of the DataFrame
        if self.count() > 0:
            return self.dataframe().to_html(index=False)
        else:
            return "None"

if __name__ == '__main__':
    db = Database()
    db.reset()
    db.seed()
