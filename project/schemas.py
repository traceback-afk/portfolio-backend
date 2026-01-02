from ninja import ModelSchema
from core.models import Project, ProjectImage, Tag
from typing import List


class ProjectImageSchema(ModelSchema):
    class Meta:
        model = ProjectImage
        fields = [
            "id",
            "image",
        ]


class TagSchema(ModelSchema):
    class Meta:
        model = Tag
        fields = ["id", "name"]


class ListProjectSchema(ModelSchema):

    image: ProjectImageSchema
    tags: list[TagSchema]

    class Meta:
        model = Project
        fields = ["id", "name", "short_description", "slug", "tags", "created_at"]


class GetProjectSchema(ModelSchema):
    images: List[ProjectImageSchema]
    tags: list[TagSchema]

    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "short_description",
            "description",
            "created_at",
            "link",
            "tags",
        ]
