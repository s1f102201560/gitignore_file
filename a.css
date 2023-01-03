from django.db import models

# Create your models here.

class Category(models.Model):
  name = models.CharField(verbose_name="セメスター", max_length=255, blank=False, null=False)
  
  def __str__(self):
    return self.name
  

class Post(models.Model):
  project = models.CharField(verbose_name="プロジェクト名", max_length=255, blank=False, null=False, unique=True)
  description = models.TextField(verbose_name="概要",blank=True, null=False)
  team = models.CharField(verbose_name="チーム名",max_length=255, blank=False, null=False)
  url = models.URLField(verbose_name="URL",max_length=200)
  pm = models.CharField(verbose_name="PM",max_length=255, blank=False, null=False)
  second_menber = models.CharField(verbose_name="メンバー１",max_length=255, blank=False, null=False)
  third_menber = models.CharField(verbose_name="メンバー２",max_length=255, blank=False, null=False)
  created_at = models.DateTimeField(verbose_name="作成日",auto_now_add=True, editable=False, blank=False, null=False)
  updated_at = models.DateTimeField(verbose_name="更新日",auto_now=True, editable=False, blank=False, null=False)
  category = models.ForeignKey(Category, verbose_name="セメスター", null=False, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.project


  