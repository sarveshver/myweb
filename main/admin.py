from django.contrib import admin
from .models import Project
from .models import Testimonial
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'github_url')  # Columns shown in admin list view
    search_fields = ('title', 'description')  # Search bar in admin
    # Optional: fields to display on the edit form in order
    fields = (
    'title',
    'description',
    'pdf_file',
    'github_url',
    'card_title_1',
    'card_desc_1',
    'card_image_1',
    'card_title_2',
    'card_desc_2',
    'card_image_2',
    'tech_title_1', 'tech_desc_1', 'tech_icon_1',
    'tech_title_2', 'tech_desc_2', 'tech_icon_2',
    'tech_title_3', 'tech_desc_3', 'tech_icon_3',
    'tech_title_4', 'tech_desc_4', 'tech_icon_4',
    'grid_image_1', 'grid_image_2', 'grid_image_3', 'grid_image_4',
)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'created_at')
    search_fields = ('name', 'role', 'comment')
    ordering = ('-created_at',)