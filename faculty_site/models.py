from django.db import models

class MainPage(models.Model):
    title = models.CharField("Назва факультету",max_length=200,default="Факультет економічних наук")
    description = models.TextField("Опис Факультету")
    content = models.TextField()

    class Meta:
        verbose_name = "Інформація головної сторінки"
        verbose_name_plural = "Інформація головної сторінки"

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField("Назва кафедри", max_length=200)
    head_name = models.CharField("Завідувач кафедри", max_length=150)

    class Meta:
        verbose_name = "Кафедра"
        verbose_name_plural = "Кафедри"

    def __str__(self):
        return self.name

class Specialyty(models.Model):
    name = models.CharField("Назва спеціальності", max_length=200)
    code = models.CharField("Код спеціальності",max_length=200)
    description = models.TextField("Опис спеціальності")
    coordinator_name = models.CharField("Ім'я координатора набору", max_length=150)
    coordinator_contact = models.CharField("Контакт координатора", max_length=100)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="graduating_specialties",
        verbose_name="Випускова кафедра"
    )
    courses = models.TextField("Список дисциплін", blank=True)

    class Meta:
        verbose_name = "Спеціальність"
        verbose_name_plural = "Спеціальності"

    def __str__(self):
        return f"{self.code} {self.name}"

class Teacher(models.Model):
    name = models.CharField("Ім'я викладача", max_length=150)
    position = models.CharField("Посада", max_length=100)
    degree = models.CharField("Науковий ступінь", max_length=100)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="teachers",
        verbose_name="Кафедра"
    )

    class Meta:
        verbose_name = "Викладач"
        verbose_name_plural = "Викладачі"

    def __str__(self):
        return f"{self.name} ({self.position})"
