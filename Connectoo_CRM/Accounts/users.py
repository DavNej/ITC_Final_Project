# import csv
# import os
# import django
# import sys
# sys.path.append('..')
# # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "authtest.settings") NOT WORKING ON SERVER
# os.environ["DJANGO_SETTINGS_MODULE"] = "Connectoo_CRM.settings"

# django.setup()

# from CRM.models import Users
# #
# #Add countries
# with open('../static/csv/countries.csv', 'rb') as csvfile:
#     countryreader = csv.reader(csvfile, delimiter=str(u',').encode('utf-8'))
#     for row in countryreader:
#         Country.objects.create(country_name=row[1], country_iso=row[0])


# #Remove duplicate countries
# for user in Users.objects.all():
#     if Users.objects.filter(user_id=user.user_id, user_name=user.user_name).count()>1:
#         print (user)
#         user.delete()