from django.db import models

email_authors = (

)

topics = (

)

explanation = ()

class EmailBody(models.Model):
    body_text = models.TextField()
    who_wrote_it = models.CharField(max_length=250, choices=email_authors, null=True)
    relation = models.CharField(max_length=250, choices=topics, null=True)
    relation_elaboration = models.TextField(null=True)

    def __str__(self):
        return self.body_text[:10]
