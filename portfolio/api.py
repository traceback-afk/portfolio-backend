from ninja import NinjaAPI
from blog.api import router as blog_router
from project.api import router as project_router


api = NinjaAPI(version="v0.1", urls_namespace="api")

api.add_router("/blog/", blog_router)
api.add_router("/project/", project_router)
