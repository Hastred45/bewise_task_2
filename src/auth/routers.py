from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.auth.crud import _create_user
from src.auth.schemas import User
from src.utils import get_db

router_auth = APIRouter(prefix='/auth', tags=['auth'])


@router_auth.post('/',
                  summary='Создание пользоватея',
                  response_model=User)
def create_user(username: str,
                db: Annotated[Session, Depends(get_db)]) -> User:
    """
    Создание пользователя. В ответе получаем id и UUID.
    """
    user = _create_user(username, db)
    return user
