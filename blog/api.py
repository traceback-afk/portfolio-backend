from ninja import Router
from blog.schemas import GetWriteUpSchema, ListWriteUpSchema, TagSchema
from core.models import WriteUp, Tag
from django.shortcuts import get_object_or_404


router = Router(tags=["Blog"])


@router.get("/", response={200: list[ListWriteUpSchema]})
def list_writeups(request, q: str = "", tags: str = "", limit: int = 0):
    qs = WriteUp.objects.filter(is_visible=True).order_by("-created_at")
    if q:
        qs = qs.filter(title__icontains=q)

    if tags:
        tag_list = [t.strip() for t in tags.split(",")]
        qs = qs.filter(tags__name__in=tag_list).distinct()

    qs = qs.order_by("-created_at")

    if limit:
        qs = qs[:limit]

    return qs


@router.get("/{slug}", response={200: GetWriteUpSchema})
def get_writeup(request, slug: str):
    writeup = get_object_or_404(WriteUp, slug=slug, is_visible=True)
    return writeup


@router.get("/tags/", response={200: list[TagSchema]})
def list_tags(request):
    qs = Tag.objects.filter(writeups__isnull=False).distinct()
    return list(qs)
