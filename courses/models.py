from django.db import models

class Nfq(models.Model):
    name = models.CharField(max_length=100)
    level= models.IntegerField(null=True)

    def __str__(self):
        return self.name

class Program_Catalogues(models.Model):
    name = models.CharField(max_length=100)
    #number = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class Learnership(models.Model):
    CERTIFICATE_TYPE = (
        ('National Certificate', 'National Certificate'),
        ('Further Education & Training', 'Further Education & Training')
    )
    MODE_OF_DELIVERY = (
        ('O', 'Online'),
        ('P', 'Physical'),
        ('H', 'Hybrid'),
    )
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=200)
    certificate_type = models.CharField(max_length=50, choices=CERTIFICATE_TYPE, default='National Certificate')
    description = models.TextField(blank=False)
    image = models.ImageField(upload_to='uploads/learnership_images/', null=True)
    mode_of_delivery = models.CharField(max_length=1, choices=MODE_OF_DELIVERY)
    nfq_level = models.ForeignKey(Nfq, on_delete=models.CASCADE, related_name="nfqlevel")
    #nfq_level = models.IntegerField(null=False)
    credits = models.IntegerField(null=False)
    #outcomes = models.TextField(null=False, default="")
    expectations = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    # duration = models.DurationField(null=False)
    duration = models.CharField( max_length=50, null=True)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False, default=None)
    end_date = models.DateTimeField(auto_now=False, auto_now_add=False, default=None)
    modules = models.TextField(null=False, default="")
    brochure = models.FileField(upload_to='uploads/learnership_brochures')

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.title


class Accredited_Program(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    MODE_OF_DELIVERY = (
        ('Online', 'Online'),
        ('Physical', 'Physical'),
        ('Hybrid', 'Hybrid'),
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=False, null=True)
    image = models.ImageField(upload_to='uploads/learnership_images/', null=True)
    mode_of_delivery = models.CharField(max_length=30, choices=MODE_OF_DELIVERY, default='O')
    expectations = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    #duration = models.DurationField(null=True)
    duration = models.CharField( max_length=50, null=True)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False, default=None)
    end_date = models.DateTimeField(auto_now=False, auto_now_add=False, default=None)
    overview = models.TextField(null=False, default="")
    accredited_brochure = models.FileField(upload_to='uploads/learnership_brochures', null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.title

    def __str__(self):
        return self.title


class Skills_Program(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    MODE_OF_DELIVERY = (
        ('O', 'Online'),
        ('P', 'Physical'),
        ('H', 'Hybrid'),
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=False , null=True)
    image = models.ImageField(upload_to='uploads/learnership_images/', null=True)
    mode_of_delivery = models.CharField(max_length=1, choices=MODE_OF_DELIVERY, default='O')
    expectations = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    # duration = models.DurationField(null=True)
    duration = models.CharField( max_length=50, null=True)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False, default=None)
    end_date = models.DateTimeField(auto_now=False, auto_now_add=False, default=None)
    overview = models.TextField(null=False, default="")
    skills_brochure = models.FileField(upload_to='uploads/learnership_brochures', null=True)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.title


class Online(models.Model):
    title = models.CharField(max_length=200)


class Specialized_Course(models.Model):
    MODE_OF_DELIVERY = (
        ('O', 'Online'),
        ('P', 'Physical'),
        ('H', 'Hybrid'),
    )
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=False, null=True)
    image = models.ImageField(upload_to='uploads/learnership_images/', null=True)
    mode_of_delivery = models.CharField(max_length=1, choices=MODE_OF_DELIVERY, default='O')
    expectations = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    # duration = models.DurationField( null=True)
    duration = models.CharField( max_length=50, null=True)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False, default=None)
    end_date = models.DateTimeField(auto_now=False, auto_now_add=False, default=None)
    overview = models.TextField(null=False, default="")
    specialized_brochure = models.FileField(upload_to='uploads/learnership_brochures', null=True)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.title