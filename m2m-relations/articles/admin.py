from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main_cnt = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                is_main_cnt += 1
        if is_main_cnt != 1:
            raise ValidationError('Ошибка')
        return super().clean()

class ScopeInline(admin.TabularInline):
    model = Scope
    verbose_name = 'Тег'
    verbose_name_plural = 'Теги'
    formset = ScopeInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass