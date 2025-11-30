from ninja import Router
from blog.schemas import GetWriteUpSchema, ListWriteUpSchema
from core.models import WriteUp
from django.shortcuts import get_list_or_404, get_object_or_404
from typing import List

router = Router(tags=["Blog"])


@router.get("/", response={201: List[ListWriteUpSchema]})
def list_writeups(response):
    writeups = get_list_or_404(WriteUp, is_visible=True, order_by="-created_at")
    return writeups


@router.get("/{slug}", response={201: GetWriteUpSchema})
def get_writeup(response, slug: str):
    writeup = get_object_or_404(WriteUp, slug=slug, is_visible=True)
    return writeup
