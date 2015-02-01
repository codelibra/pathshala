from django.db import models

class Student(models.Model):
    '''
    student model which represents a single student
    the id of the student is the email address
    '''
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField()
    def __unicode__(self):
        return self.first_name + self.last_name + self.email

class Coaching(models.Model):
    '''
    coaching model which represents the problem setter
    the id of the coaching is the email address
    '''
    name = models.CharField(max_length = 30)
    email = models.EmailField()
    def __unicode__(self):
        return self.name + self.email

class Question(models.Model):
    '''
    question model represents a question in a test
    A question will be part of a single testID which is foreign key
    '''
    text = models.CharField(max_length = 300)
    options = models.CharField(max_length = 300)
    answer = models.CharField(max_length = 300)
    test_id = models.ForeignKey('Test')
    def __unicode__(self):
        return self.text + self.answer

class Test(models.Model):
    '''
    test model represents a test
    there a list of questions in a test
    '''
    title = models.CharField(max_length = 300)
    start_time = models.DateField()
    end_time = models.DateField()
    def __unicode__(self):
        return self.title

