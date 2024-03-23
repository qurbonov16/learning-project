from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from sign_up.models import CustomUser
from learning_center.models import TeacherModel, StudentModel


@receiver(post_save, sender=CustomUser)
def tch(sender, instance, created, **kwargs):
    if created:
        if instance.is_teacher == True:
            # s = instance.id
            # TeacherModel.teacher = str(instance.id)
            teacher = TeacherModel(teacher=instance)
            teacher.save()

        # else:
        #     student = StudentModel(student=instance)
        #     student.save()
    else:
        if instance.is_teacher == True:
            # s = instance.id
            # TeacherModel.teacher = str(instance.id)
            teacher = TeacherModel(teacher=instance)
            teacher.save()

