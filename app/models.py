from sqlmodel import Field, SQLModel, Relationship
from typing import Optional
from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()

class User(SQLModel, table=True):
    id: Optional[int] =  Field(default=None, primary_key=True)
    username:str = Field(index=True, unique=True)
    email:str = Field(index=True, unique=True)
    password:str

    todos: list['Todo'] = Relationship(back_populates="user")

    def set_password(self, plaintext_password):
        self.password = password_hash.hash(plaintext_password)

    def __str__(self) -> str:
        return f"(User id={self.id}, username={self.username} ,email={self.email})"

class TodoCategory(SQLModel, table=True):
    # Implementation of the TodoCategory model from task 5.1 here
    pass


class Todo(SQLModel, table=True):
    id: Optional[int] =  Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key='user.id') #set user_id as a foreign key to user.id 
    text: str = Field(max_length=255)
    done: bool = Field(default=False)
    # done: bool = False  # <---- can also be written this way if you prefer a pythonic default

    user: User = Relationship(back_populates="todos")

    def toggle(self):
        self.done = not self.done

    ## Task 3.4 implementation should go here as well

    # Task 5.2 code should go here
    
    
class Category(SQLModel, table=True):
    # Implementation of the Category model from task 5.1 here
    pass