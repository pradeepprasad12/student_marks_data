from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)
    subject1 = models.CharField(max_length=50)
    subject2 = models.CharField(max_length=50)
    subject3 = models.CharField(max_length=50)
    subject4 = models.CharField(max_length=50)
    subject5 = models.CharField(max_length=50)
    subject1_score = models.IntegerField()
    subject2_score = models.IntegerField()
    subject3_score = models.IntegerField()
    subject4_score = models.IntegerField()
    subject5_score = models.IntegerField()
    image = models.ImageField(upload_to='student_images/')
    class_level = models.IntegerField(choices=[(i, i) for i in range(1, 13)])
    
    class Meta:
        unique_together = ['roll_number', 'class_level']

    def total_score(self):
        return self.subject1_score + self.subject2_score + self.subject3_score + self.subject4_score + self.subject5_score

    def __str__(self):
        return self.name
