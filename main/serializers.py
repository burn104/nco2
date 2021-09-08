from rest_framework import serializers
from main.models import News, ImageNews, FavouriteNews, LawType, Law, Publication


class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = 'id title publication_date short_description'.split()

    def add_to_favourite(self, obj):
        request = self.context['request']
        if request.user.is_anonymous:
            return False
        else:
            favourites = FavouriteNews.objects.filter(user=request.user, news=obj)
            count = favourites.count()
            print(count, favourites)
            if count > 0:
                return True
            else:
                return False


class ImageNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageNews
        fields = 'id image'.split()


class NewsItemSerializer(serializers.ModelSerializer):
    images = ImageNewsSerializer(many=True)

    class Meta:
        model = News
        fields = 'id title link full_description images'.split()


class LawTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LawType
        fields = 'id name'.split()


class LawsByTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Law
        fields = 'id title text'.split()


class LawItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Law
        fields = 'id title text law_type'.split()


class PublicationsByTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = 'id title text file'.split()


class PublicationItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = 'id title text file types'.split()