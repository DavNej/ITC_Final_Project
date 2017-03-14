# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Agendas(models.Model):
    is_awake = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    agendable_id = models.IntegerField(blank=True, null=True)
    agendable_type = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    report = models.CharField(max_length=255, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    poop_id = models.IntegerField(blank=True, null=True)
    lack_id = models.IntegerField(blank=True, null=True)
    food_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    will_be_absent_until = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'agendas'
    
    def __str__(self):
        return self.comment


class Attachments(models.Model):
    file_file_name = models.CharField(max_length=255, blank=True, null=True)
    file_content_type = models.CharField(max_length=255, blank=True, null=True)
    file_file_size = models.IntegerField(blank=True, null=True)
    file_updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'attachments'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BulletinGhosts(models.Model):
    bulletin = models.ForeignKey('Bulletins', models.DO_NOTHING, blank=True, null=True)
    group_ids = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bulletin_ghosts'


class BulletinGroups(models.Model):
    bulletin = models.ForeignKey('Bulletins', models.DO_NOTHING, blank=True, null=True)
    group = models.ForeignKey('Groups', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bulletin_groups'


class BulletinLinks(models.Model):
    url = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image_file_name = models.CharField(max_length=255, blank=True, null=True)
    image_content_type = models.CharField(max_length=255, blank=True, null=True)
    image_file_size = models.IntegerField(blank=True, null=True)
    image_updated_at = models.DateTimeField(blank=True, null=True)
    bulletin = models.ForeignKey('Bulletins', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bulletin_links'


class BulletinPhotos(models.Model):
    bulletin = models.ForeignKey('Bulletins', models.DO_NOTHING, blank=True, null=True)
    image_file_name = models.CharField(max_length=255, blank=True, null=True)
    image_content_type = models.CharField(max_length=255, blank=True, null=True)
    image_file_size = models.IntegerField(blank=True, null=True)
    image_updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bulletin_photos'


class Bulletins(models.Model):
    text = models.TextField(blank=True, null=True)
    k_garden = models.ForeignKey('KGardens', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    link = models.CharField(max_length=255, blank=True, null=True)
    creator_id = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    updater_id = models.IntegerField(blank=True, null=True)
    deleter_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bulletins'


class Contacts(models.Model):
    firstname = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    contact_profile_id = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    cell_phone = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    contact_pic_file_name = models.CharField(max_length=255, blank=True, null=True)
    contact_pic_content_type = models.CharField(max_length=255, blank=True, null=True)
    contact_pic_file_size = models.IntegerField(blank=True, null=True)
    contact_pic_updated_at = models.DateTimeField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    contact_title = models.CharField(max_length=255, blank=True, null=True)
    relative_id = models.IntegerField(blank=True, null=True)
    kid = models.ForeignKey('Kids', models.DO_NOTHING, blank=True, null=True)
    registered_user = models.IntegerField(blank=True, null=True)
    creator_id = models.IntegerField(blank=True, null=True)
    visible = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'contacts'


class Conversions(models.Model):
    from_id = models.IntegerField(blank=True, null=True)
    to_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    isnew = models.IntegerField(db_column='isNew', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'conversions'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EventReminders(models.Model):
    event_id = models.CharField(max_length=255, blank=True, null=True)
    k_garden_id = models.IntegerField(blank=True, null=True)
    event_type = models.CharField(max_length=255, blank=True, null=True)
    start_at = models.DateTimeField(blank=True, null=True)
    end_at = models.DateTimeField(blank=True, null=True)
    repeat = models.IntegerField(blank=True, null=True)
    date_interval = models.CharField(max_length=255, blank=True, null=True)
    repeat_interval = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    kid_id = models.IntegerField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_reminders'


class EventTypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_types'


class Events(models.Model):
    k_garden_id = models.IntegerField(blank=True, null=True)
    event_date_from = models.DateField(blank=True, null=True)
    event_date_to = models.DateField(blank=True, null=True)
    event_time_from = models.TimeField(blank=True, null=True)
    event_time_to = models.TimeField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    notification_min_befor = models.IntegerField(blank=True, null=True)
    event_type_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    rule_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events'


class EventsInGroups(models.Model):
    event_id = models.IntegerField(blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events_in_groups'


class Faces(models.Model):
    kid_id = models.IntegerField(blank=True, null=True)
    service_face_id = models.CharField(unique=True, max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    faceable_id = models.IntegerField(blank=True, null=True)
    faceable_type = models.CharField(max_length=255, blank=True, null=True)
    detected_faces = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'faces'


class FoodActs(models.Model):
    kid_id = models.IntegerField(blank=True, null=True)
    k_garden_id = models.IntegerField(blank=True, null=True)
    food_id = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    rule_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'food_acts'


class FoodAtGardens(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    k_garden_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    icon_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'food_at_gardens'


class FoodTemplates(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    icon_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'food_templates'


class Foods(models.Model):
    food_name = models.CharField(max_length=255, blank=True, null=True)
    parent_food = models.IntegerField(blank=True, null=True)
    k_garden_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'foods'


class GroupTypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'group_types'


class Groups(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    k_garden = models.ForeignKey('KGardens', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    group_type = models.ForeignKey(GroupTypes, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'groups'


class KGardens(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    house = models.IntegerField(blank=True, null=True)
    entry = models.IntegerField(blank=True, null=True)
    floor = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    postal = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    cellphone = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    pay_factor = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    registration_code_parent = models.CharField(unique=True, max_length=255, blank=True, null=True)
    valid_until = models.DateTimeField(blank=True, null=True)
    credit_api_key = models.CharField(max_length=255, blank=True, null=True)
    picture_file_name = models.CharField(max_length=255, blank=True, null=True)
    picture_content_type = models.CharField(max_length=255, blank=True, null=True)
    picture_file_size = models.IntegerField(blank=True, null=True)
    picture_updated_at = models.DateTimeField(blank=True, null=True)
    google_calendar_id = models.CharField(max_length=255, blank=True, null=True)
    face_group_id = models.IntegerField(unique=True, blank=True, null=True)
    lat = models.CharField(max_length=255, blank=True, null=True)
    lng = models.CharField(max_length=255, blank=True, null=True)
    registration_code_staff = models.CharField(unique=True, max_length=255, blank=True, null=True)
    staff_notifications = models.IntegerField(blank=True, null=True)
    staff_notifications_time = models.CharField(max_length=255, blank=True, null=True)
    parents_notifications = models.IntegerField(blank=True, null=True)
    parents_notifications_time = models.CharField(max_length=255, blank=True, null=True)
    location_base_reminder = models.IntegerField(blank=True, null=True)
    start_location_base_reminder_time = models.CharField(max_length=255, blank=True, null=True)
    geofence_id = models.CharField(max_length=255, blank=True, null=True)
    end_location_base_reminder_time = models.CharField(max_length=255, blank=True, null=True)
    geotrigger_campaign_id = models.CharField(max_length=255, blank=True, null=True)
    registration_code = models.CharField(max_length=255, blank=True, null=True)
    country_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'k_gardens'


class KidLacks(models.Model):
    lack_id = models.IntegerField(blank=True, null=True)
    kid_id = models.IntegerField(blank=True, null=True)
    k_garden_id = models.IntegerField(blank=True, null=True)
    is_done = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kid_lacks'


class KidPhotos(models.Model):
    kid = models.ForeignKey('Kids', models.DO_NOTHING, blank=True, null=True)
    image_file_name = models.CharField(max_length=255, blank=True, null=True)
    image_content_type = models.CharField(max_length=255, blank=True, null=True)
    image_file_size = models.IntegerField(blank=True, null=True)
    image_updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'kid_photos'


class KidPoops(models.Model):
    kid_id = models.IntegerField(blank=True, null=True)
    k_garden_id = models.IntegerField(blank=True, null=True)
    poop_id = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kid_poops'


class KidPresences(models.Model):
    k_garden_id = models.IntegerField(blank=True, null=True)
    kid_id = models.IntegerField(blank=True, null=True)
    action_type = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    reported_date = models.DateTimeField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kid_presences'


class Kids(models.Model):
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    picture_id = models.IntegerField(blank=True, null=True)
    id_num = models.CharField(max_length=255, blank=True, null=True)
    bdate = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    profile_pic_file_name = models.CharField(max_length=255, blank=True, null=True)
    profile_pic_content_type = models.CharField(max_length=255, blank=True, null=True)
    profile_pic_file_size = models.IntegerField(blank=True, null=True)
    profile_pic_updated_at = models.DateTimeField(blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    partner_code = models.CharField(max_length=255, blank=True, null=True)
    valid_until = models.DateTimeField(blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    event_id = models.CharField(max_length=255, blank=True, null=True)
    face_person_id = models.CharField(unique=True, max_length=255, blank=True, null=True)
    default_face_id = models.CharField(max_length=255, blank=True, null=True)
    group = models.ForeignKey(Groups, models.DO_NOTHING, blank=True, null=True)
    will_be_absent_until = models.DateField(blank=True, null=True)
    status_changed_at = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kids'

    def __str__(self):
        return self.first_name

class KindPoops(models.Model):
    kid_id = models.IntegerField(blank=True, null=True)
    k_garden_id = models.IntegerField(blank=True, null=True)
    poop_id = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kind_poops'


class LackAtGardens(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    k_garden_id = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    icon_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lack_at_gardens'


class LackTemplates(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    icon_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lack_templates'


class Lacks(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    k_garden_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lacks'


class Likes(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    picture_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'likes'


class MessageTemplates(models.Model):
    content = models.TextField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message_templates'


class Messages(models.Model):
    content = models.TextField(blank=True, null=True)
    conversion_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    from_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'messages'


class NumberOfPics(models.Model):
    kid = models.ForeignKey(Kids, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'number_of_pics'


class NumberOfPicsTags(models.Model):
    number_of_pic_id = models.IntegerField(blank=True, null=True)
    tag_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'number_of_pics_tags'


class Pictures(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    upload_file_name = models.CharField(max_length=255, blank=True, null=True)
    upload_content_type = models.CharField(max_length=255, blank=True, null=True)
    upload_file_size = models.IntegerField(blank=True, null=True)
    upload_updated_at = models.DateTimeField(blank=True, null=True)
    k_garden_id = models.IntegerField(blank=True, null=True)
    batch_id = models.IntegerField(blank=True, null=True)
    batch_size = models.IntegerField(blank=True, null=True)
    face_processing_done = models.IntegerField()
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    detected_faces = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pictures'


class Poops(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'poops'


class Profiles(models.Model):
    profile_name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profiles'


class Relatives(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    limit = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'relatives'


class SchemaMigrations(models.Model):
    version = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'schema_migrations'


class Sleeps(models.Model):
    kid_id = models.IntegerField(blank=True, null=True)
    k_garden_id = models.IntegerField(blank=True, null=True)
    is_awake = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sleeps'


class Tags(models.Model):
    picture_id = models.IntegerField(blank=True, null=True)
    kid_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    left = models.IntegerField(blank=True, null=True)
    top = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tags'


class Timelines(models.Model):
    timelineable_id = models.IntegerField(blank=True, null=True)
    timelineable_type = models.CharField(max_length=255, blank=True, null=True)
    kid_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'timelines'


class Users(models.Model):
    email = models.CharField(max_length=255, blank=True, null=True)
    encrypted_password = models.CharField(max_length=255)
    reset_password_token = models.CharField(unique=True, max_length=255, blank=True, null=True)
    reset_password_sent_at = models.DateTimeField(blank=True, null=True)
    remember_created_at = models.DateTimeField(blank=True, null=True)
    sign_in_count = models.IntegerField()
    current_sign_in_at = models.DateTimeField(blank=True, null=True)
    last_sign_in_at = models.DateTimeField(blank=True, null=True)
    current_sign_in_ip = models.CharField(max_length=255, blank=True, null=True)
    last_sign_in_ip = models.CharField(max_length=255, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    id_num = models.CharField(max_length=255, blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    is_approved = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    authentication_token = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    k_garden_id = models.IntegerField(blank=True, null=True)
    profile = models.ForeignKey(Profiles, models.DO_NOTHING, blank=True, null=True)
    device_id = models.CharField(max_length=255, blank=True, null=True)
    is_android = models.IntegerField()
    confirmation_token = models.CharField(unique=True, max_length=255, blank=True, null=True)
    confirmed_at = models.DateTimeField(blank=True, null=True)
    confirmation_sent_at = models.DateTimeField(blank=True, null=True)
    is_agree_privacy = models.IntegerField(blank=True, null=True)
    sms_send_date = models.DateTimeField(blank=True, null=True)
    sms_count = models.IntegerField(blank=True, null=True)
    locale = models.CharField(max_length=255, blank=True, null=True)
    picture_file_name = models.CharField(max_length=255, blank=True, null=True)
    picture_content_type = models.CharField(max_length=255, blank=True, null=True)
    picture_file_size = models.IntegerField(blank=True, null=True)
    picture_updated_at = models.DateTimeField(blank=True, null=True)
    relative_id = models.IntegerField(blank=True, null=True)
    attendance_notifications = models.IntegerField(blank=True, null=True)
    attendance_notifications_time = models.CharField(max_length=255, blank=True, null=True)
    location_base_reminder = models.IntegerField(blank=True, null=True)
    start_location_base_reminder_time = models.CharField(max_length=255, blank=True, null=True)
    end_location_base_reminder_time = models.CharField(max_length=255, blank=True, null=True)
    failed_attempts = models.IntegerField()
    unlock_token = models.CharField(unique=True, max_length=255, blank=True, null=True)
    locked_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class UsersKids(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    kid_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    access = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_kids'


class Versions(models.Model):
    number = models.CharField(max_length=255, blank=True, null=True)
    platform = models.CharField(max_length=255, blank=True, null=True)
    force = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'versions'
