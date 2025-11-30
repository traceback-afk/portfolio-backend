from ninja import Schema


class CreateMessageResultSchema(Schema):
    result: str


class CreateMessageSchema(Schema):
    name: str
    email: str
    message: str
