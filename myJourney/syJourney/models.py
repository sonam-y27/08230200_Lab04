from django.db import models

# ===========================
# Models for index.html page
# ===========================

class Skill(models.Model):
    title = models.CharField(max_length=100)  # e.g., "Lesson Planning"
    description = models.TextField()          # e.g., "Designing clear, student-centered lessons"

    def __str__(self):
        return self.title


class LearningExperience(models.Model):
    title = models.CharField(max_length=150)  # e.g., "Micro Teaching: Files and Folders"
    description = models.TextField()          # Details about the experience
    order = models.PositiveIntegerField(default=0)  # To control display order

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Challenge(models.Model):
    title = models.CharField(max_length=150)  # e.g., "Stage Fright"
    description = models.TextField()          # e.g., "Felt nervous during the first micro teach but improved with practice"

    def __str__(self):
        return self.title


class Reflection(models.Model):
    content = models.TextField()  # Reflection text

    def __str__(self):
        return f"Reflection {self.id}"


# ===========================
# Models for aboutMe.html page
# ===========================

class Hobby(models.Model):
    name = models.CharField(max_length=100)   # e.g., "Creating short vlogs"

    def __str__(self):
        return self.name


class Strength(models.Model):
    name = models.CharField(max_length=100)   # e.g., "Patience with learners"

    def __str__(self):
        return self.name


class Weakness(models.Model):
    name = models.CharField(max_length=100)   # e.g., "Stage fright during presentations"

    def __str__(self):
        return self.name
