from ninja import Router
from project.schemas import ListProjectSchema, GetProjectSchema
from core.models import Project
from django.shortcuts import get_object_or_404

router = Router(tags=["Project"])


@router.get("/", response=list[ListProjectSchema])
def list_projects(request, q: str = "", tags: str = "", limit: int = 0):
    qs = Project.objects.filter(is_visible=True).prefetch_related("images")

    if q:
        qs = qs.filter(name__icontains=q)

    if tags:
        tag_list = [t.strip() for t in tags.split(",")]
        qs = qs.filter(tags__name__in=tag_list).distinct()

    qs = qs.order_by("-created_at")

    if limit:
        qs = qs[:limit]

    return list(qs)


@router.get("/{slug}", response=GetProjectSchema)
def get_project(request, slug: str):
    project = get_object_or_404(
        Project.objects.prefetch_related("images"), is_visible=True, slug=slug
    )
    return project
