from rest_framework import serializers
from .models import CheckList, CheckListItem


class CheckListItemSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        fields = '__all__'
        model = CheckListItem


class CheckListSerializers(serializers.ModelSerializer):
    items = CheckListItemSerializer(source='checklistitem_set', many=True, read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        # fields = (
        #     'id',
        #     'title',
        #     'is_deleted',
        #     'is_archived',
        #     'created_on',
        #     'updated_on',
        # )
        fields = '__all__'
        model = CheckList
