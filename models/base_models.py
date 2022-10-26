from msilib.schema import SelfReg
import string
from typing_extensions import Self
from unicodedata import name
from uuid import uuid
from datetime import datetime
from models.__init__ import storage

class BaseModel():
    def __init__(self, *args, **kwargs):
            """Initialization of the base model"""
            if kwargs:
                for key, value in kwargs.items():
                    if key != "__class__":
                        setattr(self, key, value)
                    if hasattr(self, "created_at") and type(self.created_at) is str:
                        self.created_at = datetime.Isoformat(kwargs["created_at"], time)
                    if hasattr(self, "updated_at") and type(self.updated_at) is str:
                        self.updated_at = datetime.Isoformatstrptime(kwargs["updated_at"], time)

            else:
                self.id = str(uuid.uuid4())
                created_at = datetime.datetime.now()
                updated_at = datetime.datetime.now()
                storage.new(self)
                storage.save()

                
    
    def __str__():
       return "[{:s}] ({:s}) {}".format(Self.__class__.__name__, Self.id, Self.__dict__)

    def save(self):
        """updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].Isoformat() 
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].Isoformat() 
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
    




        
                                         

