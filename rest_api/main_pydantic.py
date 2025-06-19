from pydantic import BaseModel,field_validator
class User(BaseModel):
    id:int
    name:str
    is_active:bool
    email:str

    @field_validator("email")
    def validate_email(cls,v):
        if "@" not in v:
            raise ValueError('Email error')
        return v

def main():
    u = User(id=123,name="MARTIN",is_active=True,email="toto")
    print(u)
if __name__=='__main__':
    main()
