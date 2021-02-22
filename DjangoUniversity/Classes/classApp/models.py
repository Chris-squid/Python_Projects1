from django.db import models
# import all models to DB




# create class djangoClasses,assign attributes and set variables

class DjangoClasses(models.Model):
    course_title = models.CharField(max_length=60,)
    course_number = models.IntegerField()
    instructor_name = models.CharField(max_length=60)
    course_duration = models.DecimalField(max_digits=10000, decimal_places=2)

    objects = models.Manager()# object manager for query into DB

    def __str__(self):# set to return self arg*
        return self.course_title
        # returns selected coulmn from DB to alter on Site