from  fastapi import FastAPI, Path

# Init fastAPI in app
app = FastAPI()

from typing import Optional

inventory = {
    1:{
        'name':'Milk',
        'price':'3.99',
        'brand':'regular'
    },
     2:{
        'name':'Milk',
        'price':'3.99',
        'brand':'regular'
    },
      3:{
        'name':'Milk',
        'price':'3.99',
        'brand':'regular'
    }

}

@app.get('/get_item/{item_id}')
def get_time(item_id: int =Path(None, description = 'The Id of the item you like' )):
    return inventory[item_id]

@app.get('/get_by_name/{item_id}')
def get_time(*, item_id: int,  name: Optional [str] = None, test: int):
    for item_id in inventory:
        if inventory [item_id] ['name'] == name:
            return inventory [item_id]
    return {'data':'Not found'}