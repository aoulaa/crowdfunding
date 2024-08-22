from django.contrib import admin

from project.models import Project, Investment, Transaction, RewardsEarned, Category, Tag, ProjectVideo, ProjectImage


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    fields = (
    'id', 'title', 'details', 'target', 'start_date', 'end_date', 'creation_date', 'creator', 'category', 'tags', 'is_deleted')
    readonly_fields = ['id', ]


@admin.register(Investment)
class InvestmentAdmin(admin.ModelAdmin):
    fields = ('id', 'amount', 'investor', 'project', 'status')
    readonly_fields = ['id', ]


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    fields = ('id', 'amount', 'transaction_date', 'project', 'investor')
    readonly_fields = ['id', ]


@admin.register(RewardsEarned)
class RewardsEarnedAdmin(admin.ModelAdmin):
    fields = ('id', 'investor', 'investment', 'amount', 'title', 'description')
    readonly_fields = ['id', ]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('id', 'title')
    readonly_fields = ['id', ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    fields = ('id', 'title')
    readonly_fields = ['id', ]

@admin.register(ProjectVideo)
class ProjectVideoAdmin(admin.ModelAdmin):
    fields = ('id', 'path', 'project')
    readonly_fields = ['id', ]
    list_display = ('id',)

@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    fields = ('id', 'path', 'project')
    readonly_fields = ['id', ]
    list_display = ('id',)
