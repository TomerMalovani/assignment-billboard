from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.forms.models import model_to_dict
from .models import Post
import json


@require_http_methods(['POST'])
def create_new_post(request):
    try:
        data = json.loads(request.body)
        new_post = Post(
            post_title=data["post_title"],
            post_content=data["post_content"],
            post_author=data["post_author"])

        new_post.save()

        return JsonResponse(model_to_dict(new_post), status=201)
    except Exception as ex:
        return JsonResponse({"error", ex}, status=500)


@login_required(login_url='login/')
@require_http_methods(['GET'])
def index(request):
    posts = []
    for post in Post.objects.all():
        posts.append({"title": post.post_title,
                      "message": post.post_content, "author": post.post_author})
    context = {"posts": posts}
    return render(request, 'billboard/index.html', context=context)


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return HttpResponseRedirect(reverse("index"))
    else:
        form = UserCreationForm()
        return render(request, "registration/register.html", {"form": form})


@require_http_methods(['GET'])
def get_post(request):
    data = list(Post.objects.values())

    return JsonResponse({"all": data})


# @require_http_methods(['POST'])
# def create_new_activity(request):
#     try:
#         data = json.loads(request.body)
#         new_activity = Activity(
#             what=data["what"],
#             when=data["when"],
#             where=data["where"])

#         new_activity.save()

#         return JsonResponse(model_to_dict(new_activity), status=201)
