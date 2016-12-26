from rest_framework import serializers
from .models import Form, Inspection
from rest_framework.reverse import reverse


class InspectionSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()

    class Meta:
        model = Inspection
        fields = ('id', 'form', 'links', )

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('inspection-detail',
                            kwargs={'pk': obj.pk}, request=request),
        }


class FormSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()

    class Meta:
        model = Form
        fields = ('id', 'parent', 'name', 'tag', 'links', )

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('form-detail',
                            kwargs={'pk': obj.pk}, request=request),
        }