from django.contrib.auth import get_user_model

from favorites.models import FavoriteList

User = get_user_model()


def create_favorite_list(user: User) -> FavoriteList:
    return FavoriteList.objects.create(owner=user)
