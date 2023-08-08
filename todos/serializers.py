from rest_framework import serializers
from .models import Todo

# class TodoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Todo
#         fields = ['title','description','is_finished']
#         read_only_fields = ('author',)
#     def create(self, validated_data):
#         validated_data['author'] = self.context['request'].user
#         todo = Todo(
#             title = validated_data['title'],
#             description= validated_data['description'],
#         )
#         todo.save()
#         return super().create(validated_data)
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

