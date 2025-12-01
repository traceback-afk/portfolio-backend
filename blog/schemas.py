from ninja import ModelSchema
from core.models import WriteUp, Tag


class ListWriteUpSchema(ModelSchema):
    class Meta:
        model = WriteUp
        fields = ["id", "title", "description", "slug", "created_at", "tags"]


class GetWriteUpSchema(ModelSchema):
    class Meta:
        model = WriteUp
        fields = ["id", "title", "description", "created_at", "content", "url", "tags"]


class TagSchema(ModelSchema):
    class Meta:
        model = Tag
        fields = [
            "name",
        ]
