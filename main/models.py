from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pdf_file = models.FileField(upload_to='pdfs/', blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)

    card_title_1 = models.CharField(max_length=100, blank=True)
    card_desc_1 = models.TextField(blank=True)
    card_image_1 = models.ImageField(upload_to='cards/', blank=True)

    card_title_2 = models.CharField(max_length=100, blank=True)
    card_desc_2 = models.TextField(blank=True)
    card_image_2 = models.ImageField(upload_to='cards/', blank=True)

    tech_title_1 = models.CharField(max_length=100, blank=True)
    tech_desc_1 = models.TextField(blank=True)
    tech_icon_1 = models.URLField(blank=True)

    tech_title_2 = models.CharField(max_length=100, blank=True)
    tech_desc_2 = models.TextField(blank=True)
    tech_icon_2 = models.URLField(blank=True)
    
    tech_title_3 = models.CharField(max_length=100, blank=True)
    tech_desc_3 = models.TextField(blank=True)
    tech_icon_3 = models.URLField(blank=True)

    tech_title_4 = models.CharField(max_length=100, blank=True)
    tech_desc_4 = models.TextField(blank=True)
    tech_icon_4 = models.URLField(blank=True)
    
    grid_image_1 = models.ImageField(upload_to='grid/', blank=True)
    grid_image_2 = models.ImageField(upload_to='grid/', blank=True)
    grid_image_3 = models.ImageField(upload_to='grid/', blank=True)
    grid_image_4 = models.ImageField(upload_to='grid/', blank=True)


    def __str__(self):
        return self.title
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.role}"