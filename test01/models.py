from django.db import models


class PersonInfo(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    hireDate = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '人员信息'
        verbose_name_plural = verbose_name


class Vocation(models.Model):
    job = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    payment = models.IntegerField(null=True, blank=True)
    name = models.ForeignKey(PersonInfo, on_delete=models.CASCADE, related_name='ps')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = '职业信息'
        verbose_name_plural = verbose_name


class Province(models.Model):
    name = models.CharField(max_length=5)

    def __str__(self):
        return str(self.name)


class City(models.Model):
    name = models.CharField(max_length=5)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Person(models.Model):
    name = models.CharField(max_length=10)
    living = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Performer(models.Model):
    name = models.CharField(max_length=20)
    nationality = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)


class Program(models.Model):
    name = models.CharField(max_length=20)
    performer = models.ManyToManyField(Performer)

    def __str__(self):
        return self.name