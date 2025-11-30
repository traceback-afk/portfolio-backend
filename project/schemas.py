from ninja import ModelSchema
from core.models import Project, ProjectImage
from typing import List, Optional


class ProjectImageSchema(ModelSchema):
    class Meta:
        model = ProjectImage
        fields = [
            "image",
        ]


class ListProjectSchema(ModelSchema):
    image: ProjectImageSchema

    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "short_description",
            "slug",
        ]


class GetProjectSchema(ModelSchema):
    images: List[ProjectImageSchema]

    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "short_description",
            "description",
            "created_at",
            "link",
        ]
