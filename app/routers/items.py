from fastapi import APIRouter
from ..models import Item

router = APIRouter()

fake_items = [
    { 'id': 1, 'title': 'item1' },
    { 'id': 2, 'title': 'item2' },
    { 'id': 3, 'title': 'item3', 'description': 'Description' },
]

@router.get('/items')
def get_items():
    return fake_items

@router.post('/items')
def add_items(item: Item):
    fake_items.append(item)
    return fake_items