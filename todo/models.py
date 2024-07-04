from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=255)
    created_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
