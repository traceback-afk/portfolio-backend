from ninja import Router
from blog.schemas import GetWriteUpSchema, ListWriteUpSchema
from core.models import WriteUp
from django.shortcuts import get_list_or_404, get_object_or_404
from typing import List
from django.http import Http404

router = Router(tags=["Blog"])


@router.get("/", response={200: List[ListWriteUpSchema]})
def list_writeups(request):
    writeups = WriteUp.objects.filter(is_visible=True).order_by("-created_at")
    if not writeups:
        raise Http404
    return writeups


@router.get("/{slug}", response={200: GetWriteUpSchema})
def get_writeup(request, slug: str):
    writeup = get_object_or_404(WriteUp, slug=slug, is_visible=True)
    return writeup
