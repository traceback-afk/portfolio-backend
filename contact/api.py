from ninja import Router
from core.schemas import ErrorSchema
from contact.schemas import CreateMessageResultSchema, CreateMessageSchema
from core.models import Message

router = Router(tags=["Contact"])


@router.post("/", response={400: ErrorSchema, 200: CreateMessageResultSchema})
def create_message(request, payload: CreateMessageSchema):
    name = payload.name
    email = payload.email
    message = payload.message
    try:
        Message.objects.create(name=name, email=email, message=message)
    except:
        return 400, {"detail": "message creation failed"}

    return 200, {"result": "successful"}
