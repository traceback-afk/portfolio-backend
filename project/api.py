from ninja import Router
from project.schemas import ListProjectSchema, GetProjectSchema
from typing import List
from core.models import Project
from django.shortcuts import get_list_or_404, get_object_or_404

router = Router(tags=["Project"])


@router.get("/", response=List[ListProjectSchema])
def list_projects(request):
    projects = get_list_or_404(
        Project.objects.prefetch_related("images").order_by("-created_at"),
        is_visible=True,
    )
    return list(projects)


@router.get("/{slug}", response=GetProjectSchema)
def get_project(request, slug: str):
    project = get_object_or_404(
        Project.objects.prefetch_related("images"), is_visible=True, slug=slug
    )
    return project
