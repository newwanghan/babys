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
