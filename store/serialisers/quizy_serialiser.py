from rest_framework import serializers
from store.models.quizy_models import Quiz


class QuizySerialiser(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ("id", "question", "description", "answer", "picture")

        def create(self, validated_data):
            return Quiz.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.question = validated_data.get("question", instance.question)
            instance.description = validated_data.get(
                "description", instance.description
            )
            instance.answer = validated_data.get("answer", instance.answer)
            instance.picture = validated_data.get("picture", instance.picture)
            instance.save()
            return instance

        def delete(self, instance):
            instance.delete()
            return instance

        def get(self, instance):
            return instance
