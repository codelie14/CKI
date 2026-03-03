from django.contrib import admin
from .models import (
    Vendor, Product, Vulnerability, Exploit, ThreatGroup, 
    AttackPattern, IndicatorOfCompromise, Article, AIAnalysis, Alert, Report
)

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['vendor', 'name', 'version', 'created_at']
    list_filter = ['vendor']
    search_fields = ['name', 'version']

@admin.register(Vulnerability)
class VulnerabilityAdmin(admin.ModelAdmin):
    list_display = ['cve_id', 'cvss_score', 'severity', 'is_zero_day', 'published_date']
    list_filter = ['severity', 'is_zero_day']
    search_fields = ['cve_id', 'description']
    filter_horizontal = ['products']

@admin.register(Exploit)
class ExploitAdmin(admin.ModelAdmin):
    list_display = ['title', 'vulnerability', 'exploit_type', 'created_at']
    list_filter = ['exploit_type']
    search_fields = ['title', 'description']

@admin.register(ThreatGroup)
class ThreatGroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'origin_country', 'created_at']
    search_fields = ['name', 'aliases']

@admin.register(AttackPattern)
class AttackPatternAdmin(admin.ModelAdmin):
    list_display = ['mitre_id', 'name', 'created_at']
    search_fields = ['mitre_id', 'name']

@admin.register(IndicatorOfCompromise)
class IOCAdmin(admin.ModelAdmin):
    list_display = ['type', 'value', 'vulnerability', 'threat_group', 'created_at']
    list_filter = ['type']
    search_fields = ['value', 'description']

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published_date', 'scraped_at']
    search_fields = ['title', 'content']
    filter_horizontal = ['vulnerabilities']

@admin.register(AIAnalysis)
class AIAnalysisAdmin(admin.ModelAdmin):
    list_display = ['threat_level', 'analyzed_at']
    filter_horizontal = ['mitre_mapping']

@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ['vulnerability', 'is_read', 'created_at']
    list_filter = ['is_read']

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']
