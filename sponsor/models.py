from django.db import models
from django.contrib.auth import get_user_model
from sorl.thumbnail import ImageField as SorlImageField
User = get_user_model()


class SponsorLevelManager(models.Manager):
    def get_queryset(self):
        return super(SponsorLevelManager, self).get_queryset().all().order_by('order')


class SponsorLevel(models.Model):
    name = models.CharField(max_length=255, blank=True,
                            default='', help_text='후원 등급명')
    slug = models.SlugField(max_length=100, unique=True,
                            help_text='level별 후원사 정보를 보여주는 페이지의 path명')
    desc = models.TextField(
        null=True, blank=True, help_text='후원 혜택을 입력하면 될 거 같아요 :) 후원사가 등급을 정할 때 볼 문구입니다.')
    visible = models.BooleanField(default=True)
    price = models.IntegerField(default=0)
    limit = models.IntegerField(default=0,
                                help_text='후원사 등급 별 구좌수')
    order = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = SponsorLevelManager()

    @property
    def current_remaining_number(self):
        return self.limit - self.accepted_count

    @property
    def paid_count(self):
        return Sponsor.objects.filter(
            level=self, submitted=True, accepted=True, paid_at__isnull=False).count()

    @property
    def accepted_count(self):
        return Sponsor.objects.filter(level=self, submitted=True, accepted=True).count()

    def __str__(self):
        return self.name


def registration_file_upload_to(instance, filename):
    return f'sponsor/business_registration/{instance.id}/{filename}'


def logo_image_upload_to(instance, filename):
    return f'sponsor/logo/{instance.id}/{filename}'


class Sponsor(models.Model):
    class Meta:
        ordering = ['paid_at', 'id']
    slug = models.SlugField(max_length=100, unique=True,
                            help_text='후원사 상세 페이지의 path로 사용됩니다')
    creator = models.ForeignKey(User, on_delete=models.CASCADE,
                                help_text='후원사를 등록한 유저')
    name = models.CharField(max_length=255, null=True, blank=True,
                            help_text='후원사 이름입니다. 서비스나 회사 이름이 될 수 있습니다.')
    level = models.ForeignKey(SponsorLevel, null=True,
                              on_delete=models.SET_NULL, blank=True,
                              help_text='후원사 등급입니다.')
    desc = models.TextField(null=True, blank=True,
                            help_text='후원사 설명입니다. 이 설명은 홈페이지에 게시됩니다.')
    manager_name = models.CharField(max_length=100, blank=True, default='',
                                    help_text='후원사 담당자의 이름입니다.')
    manager_email = models.CharField(max_length=100, blank=True, default='',
                                     help_text='후원사 담당자의 이메일 주소입니다.')
    business_registration_number = models.CharField(max_length=100, blank=True, default='',
                                                    help_text='후원사 사업자 등록번호입니다.')
    business_registration_file = models.FileField(
        upload_to=registration_file_upload_to, blank=True, default='',
        help_text='후원사 사업자 등록증 스캔본입니다.')
    url = models.CharField(max_length=255, null=True, blank=True,
                           help_text='후원사 홈페이지 주소입니다. 파이콘 홈페이지에 공개됩니다.')
    logo_image = SorlImageField(upload_to=logo_image_upload_to, null=True, blank=True,
                                help_text='홈페이지에 공개되는 후원사 이미지입니다.')
    paid_at = models.DateTimeField(null=True, blank=True,
                                   help_text='후원금이 입금된 일시입니다. 아직 입금되지 않았을 경우 None이 들어갑니다.')
    submitted = models.BooleanField(default=False,
                                    help_text='사용자가 제출했는지 여부를 저장합니다..')
    accepted = models.BooleanField(default=False,
                                   help_text='파이콘 준비위원회의 검토 후 후원사의 후원을 받을지 여부를 결정합니다.')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}/{self.level}'

    def get_absolute_url(self):
        return reverse('sponsor', args=[self.slug])