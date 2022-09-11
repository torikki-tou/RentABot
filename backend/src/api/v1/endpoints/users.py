from fastapi import APIRouter

router = APIRouter()


@router.get('/{user_id}')
def read_user():
    ...


@router.post('/')
def create_user():
    ...


@router.put('/{user_id}')
def update_user():
    ...


@router.delete('/{user_id}')
def remove_user():
    ...
