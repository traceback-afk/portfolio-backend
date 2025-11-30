from ninja import ModelSchema
from core.models import WriteUp


class ListWriteUpSchema(ModelSchema):
    class Meta:
        model = WriteUp
        fields = ["id", "title", "description", "slug"]


class GetWriteUpSchema(ModelSchema):
    class Meta:
        model = WriteUp
        fields = ["id", "title", "description", "created_at", "content"]
