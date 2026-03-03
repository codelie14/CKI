from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    version = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('vendor', 'name', 'version')

    def __str__(self):
        return f"{self.vendor.name} - {self.name} ({self.version})"

class Vulnerability(models.Model):
    cve_id = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    cvss_score = models.FloatField(null=True, blank=True)
    severity = models.CharField(max_length=20, blank=True, null=True) # Low, Medium, High, Critical
    published_date = models.DateTimeField(null=True, blank=True)
    last_modified_date = models.DateTimeField(null=True, blank=True)
    products = models.ManyToManyField(Product, related_name='vulnerabilities')
    source_url = models.URLField(blank=True, null=True)
    is_zero_day = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cve_id

class Exploit(models.Model):
    vulnerability = models.ForeignKey(Vulnerability, on_delete=models.CASCADE, related_name='exploits')
    title = models.CharField(max_length=255)
    description = models.TextField()
    source_url = models.URLField()
    exploit_type = models.CharField(max_length=100, blank=True, null=True) # e.g., Remote, Local, DoS
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Exploit for {self.vulnerability.cve_id}: {self.title}"

class ThreatGroup(models.Model):
    name = models.CharField(max_length=255, unique=True)
    aliases = models.TextField(blank=True, null=True) # JSON or comma separated
    description = models.TextField()
    origin_country = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class AttackPattern(models.Model):
    mitre_id = models.CharField(max_length=20, unique=True) # T1234
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.mitre_id} - {self.name}"

class IndicatorOfCompromise(models.Model):
    IOC_TYPES = (
        ('IP', 'IP Address'),
        ('DOMAIN', 'Domain'),
        ('HASH', 'File Hash'),
        ('URL', 'URL'),
    )
    type = models.CharField(max_length=10, choices=IOC_TYPES)
    value = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    vulnerability = models.ForeignKey(Vulnerability, on_delete=models.SET_NULL, null=True, blank=True, related_name='iocs')
    threat_group = models.ForeignKey(ThreatGroup, on_delete=models.SET_NULL, null=True, blank=True, related_name='iocs')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type}: {self.value}"

class Article(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    source_url = models.URLField(unique=True)
    published_date = models.DateTimeField(null=True, blank=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    scraped_at = models.DateTimeField(auto_now_add=True)
    vulnerabilities = models.ManyToManyField(Vulnerability, related_name='articles', blank=True)

    def __str__(self):
        return self.title

class AIAnalysis(models.Model):
    article = models.OneToOneField(Article, on_delete=models.CASCADE, null=True, blank=True, related_name='ai_analysis')
    vulnerability = models.OneToOneField(Vulnerability, on_delete=models.CASCADE, null=True, blank=True, related_name='ai_analysis')
    summary = models.TextField()
    extracted_entities = models.JSONField(default=dict)
    threat_level = models.CharField(max_length=50)
    mitre_mapping = models.ManyToManyField(AttackPattern, blank=True)
    analyzed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.article:
            return f"AI Analysis for Article: {self.article.title}"
        return f"AI Analysis for CVE: {self.vulnerability.cve_id}"

class Alert(models.Model):
    vulnerability = models.ForeignKey(Vulnerability, on_delete=models.CASCADE, related_name='alerts')
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Alert for {self.vulnerability.cve_id}"

class Report(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    file_path = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
