from django.db import models


class FeedbackManager(models.Manager):
    def get_approved_feedbacks(self):
        return self.filter(approved=True)


class Feedback(models.Model):
    feedback_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    objects = FeedbackManager()
