from django.db import models

# Create your models here.
class Member (models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    interests = models.TextField()
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Message(models.Model):
    sender = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Message from {self.sender.name} to {self.receiver.name} at {self.timestamp}'
class Call(models.Model):
    caller = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='calls_made')
    receiver = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='calls_received')
    timestamp = models.DateTimeField(auto_now_add=True)
    duration = models.IntegerField()  # Duration in seconds
    def __str__(self):
        return f'Call from {self.caller.name} to {self.receiver.name} at {self.timestamp} lasting {self.duration} seconds'
