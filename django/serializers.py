from rest_framework import serializers
import re
LEARNING_DIFFICULTY_CHOICES = [
                ("Autism", "Autism"),
                ("ADHD", "ADHD"),
                ("Dyslexia", "Dyslexia"),
                ("Speech Delay", "Speech Delay"),
                ("Other", "Other"),
]

class StudentOnboardingSerializer(serializers.Serializer):
    """
    Serializer responsible for validating incoming
    student onboarding requests before processing.
    """
    student_name = serializers.CharField(
        max_length=100,
        min_length=3,
        required=True,
        trim_whitespace=True
    )
    age = serializers.IntegerField(
        min_value=5,
        max_value=25,
        required=True
    )
    parent_name = serializers.CharField(
        max_length=100,
        required=True,
        trim_whitespace=True
    )
    email = serializers.EmailField(
        required=True
    )

    phone = serializers.RegexField(
        regex=r'^\d{10}$',
        required=True,
        error_messages={
            "invalid": "Phone number must contain exactly 10 digits."
        }
    )
    consent_given = serializers.BooleanField(
        required=True
    )
    learning_difficulty = serializers.ChoiceField(
        choices=LEARNING_DIFFICULTY_CHOICES,
        required=True
    )
    requires_lsa = serializers.BooleanField(
        required=True
    )

    def validate_student_name(self, value):
        if not re.fullmatch(r"^[A-Za-z ]+$", value):
            raise serializers.ValidationError("Student name should contain only letters and spaces.")
        return value
    
    def validate(self, data):
        if (data.get("requires_lsa") and data.get("learning_difficulty") == "Other"):
            raise serializers.ValidationError("Learning difficulty must be specified when LSA support is requested.")
        return data