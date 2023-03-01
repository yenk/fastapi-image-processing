from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel 

app = FastAPI()

class item(BaseModel):
    """ This object leverages Pydantic basemodel for fastapi 
    typing invocation and type validation."""
    name: str
    price: float
    brand: Optional[str] = None # brand is an option or default to None

class UpdateItem(BaseModel):
    """ This sets instance objects with optional post input, else None."""
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None
    
inventory = {}
    
# create path endpoint
@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, description="The item ID to view.", gt=0)):
    """
    Parameters
    -----------
        item_id: type hint set to int
        path: must declared first arg, this is set to None, with a description, 
        and greater than 0 for item_id retrieval
    """
    return inventory[item_id]