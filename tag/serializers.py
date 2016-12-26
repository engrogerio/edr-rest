from rest_framework import serializers
from .models import Unit, Tag, Value, FieldType
from rest_framework.reverse import reverse


class FieldTypeField(serializers.RelatedField):

    def to_representation(self, instance):
        return instance.name


class UnitSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()

    class Meta:
        model = Unit
        fields = ('id', 'name', 'symbol', 'unit_of', 'links',)

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('unit-detail',
                        kwargs={'pk': obj.pk}, request=request),
        }


class TagSerializer(serializers.ModelSerializer):

    #unit = serializers.SlugRelatedField(slug_field=Unit.name)
    links = serializers.SerializerMethodField()

    class Meta:
        model = Tag
        fields = ('id', 'name', 'type', 'unit', 'decimal_places', 'links',)

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('tag-detail',
                        kwargs={'pk': obj.pk}, request=request),
        }


class ValueSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()

    class Meta:
        model = Value
        fields = ('id', 'tag', 'numeric', 'text', 'inspection', 'links',)

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('value-detail',
                        kwargs={'pk': obj.pk}, request=request),
        }



class FieldTypeSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()

    class Meta:
        model = FieldType
        fields = ('id', 'name', 'links',)

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('field-detail',
                        kwargs={'pk': obj.pk}, request=request),
        }



