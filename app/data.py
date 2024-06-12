from os import getenv

from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient


class Database:
    """Develop a database interface class"""

    def __init__(self):

        """Create random monster data with the MonsterLab library"""

        load_dotenv()
        db_url = getenv("DB_URL")
        self.database = MongoClient(db_url, tlsCAfile=where())["Bandersnatch"]
        self.collection = self.database.get_collection("Monsters")

    def seed(self, amount=1000):

        """Populate the database with 1000 Monsters"""
        monster = []
        for _ in range(1000):
            monster.append(Monster().to_dict())

        return self.collection.insert_many(monster)

    def reset(self):
        pass

        """The reset() function correctly deletes 
        all documents from the collection."""

        self.collection.delete_many({})

    def count(self) -> int:
        pass
        
        """The count() function correctly returns
        the number of documents in the collection."""
        
        return self.collection.count_documents({})

    def dataframe(self) -> DataFrame:
        pass

        """This method will return a DataFrame excluding the _id field"""
       
        df = DataFrame(self.collection.find({}, {"_id" : False}))

        return df

    def html_table(self) -> str:
        pass
       
        """The html_table() function correctly returns an HTML table representation of the DataFrame,
        or None if the collection is empty."""

        if self.count() > 0:
            return self.dataframe().to_html(index=False)
        else:
            return "None"
