# Author : Kenedy Nopriansyah
# Email : kenedinovriansyah@gmail.com
# description : Don't forgot to happy :D
import os
import datetime
import json
from pathlib import Path
from django.conf import settings

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-j&(n%3x3*wo6ziu*@e&rfm42u1%luy8f-snt!1z&0f-e8(oo_+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

with open('setup/config.json', 'r') as r:
    for i in json.loads(r.read()):
        INSTALLED_APPS.append(i)

with open('setup/apps.json', 'r') as r:
    for i in json.loads(r.read()):
        INSTALLED_APPS.append(i)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "corsheaders.middleware.CorsMiddleware",
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:4200"
]

ROOT_URLCONF = 'L7.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'L7.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = (
    os.path.join(BASE_DIR, "static")
)

MEDIA_URL = "/media/"
MEDIA_ROOT = (
    os.path.join(BASE_DIR, "media")
)

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


JWT_AUTH = {
    'JWT_ENCODE_HANDLER':
    'rest_framework_jwt.utils.jwt_encode_handler',

    'JWT_DECODE_HANDLER':
    'rest_framework_jwt.utils.jwt_decode_handler',

    'JWT_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_payload_handler',

    'JWT_PAYLOAD_GET_USER_ID_HANDLER':
    'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',

    'JWT_RESPONSE_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_response_payload_handler',

    'JWT_SECRET_KEY': settings.SECRET_KEY,
    'JWT_GET_USER_SECRET_KEY': None,
    'JWT_PUBLIC_KEY': None,
    'JWT_PRIVATE_KEY': None,
    'JWT_ALGORITHM': 'HS256',
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LEEWAY': 0,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=300 * 99999999),
    'JWT_AUDIENCE': None,
    'JWT_ISSUER': None,

    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),

    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    'JWT_AUTH_COOKIE': None,

}


# {
#   "has_multiple_schedules": false,
#   "id_event": "io3",
#   "event_name": "Movievaganza: The Sound of Music",
#   "custom_url": "https://www.loket.com/event/movievaganza-the-sound-of-music_io3",
#   "start_date": "2021-07-03 19:00:00",
#   "end_date": "2021-07-03 21:20:00",
#   "start_end_date": "03 Jul 2021",
#   "start_end_time": "19:00 - 21:20",
#   "location_name": "Jakarta",
#   "address": "DKI Jakarta",
#   "country": "Indonesia",
#   "province": "DKI Jakarta",
#   "district": "Online",
#   "region": "Online",
#   "is_past_event": true,
#   "organization_name": "Pranadjaja's Theatrical Group",
#   "event_banner": "https://s3-ap-southeast-1.amazonaws.com/loket-production-sg/images/banner/20210615143026_60c8571292422.jpg",
#   "event_banners": [],
#   "cheapest_ticket_price": 100000,
#   "cheapest_initial_ticket_price": null,
#   "is_streak_price": false,
#   "categories": [
#     {
#       "id_event_category": 3,
#       "name_event_category": "Concert",
#       "urlencode": "concert",
#       "status_event_category": 1,
#       "status_event_category_name": "ACTIVE"
#     }
#   ],
#   "schedules": [
#     {
#       "id_schedule": 49544,
#       "id_schedule_external": "",
#       "start_date": "2021-07-03 19:00:00",
#       "end_date": "2021-07-03 21:20:00",
#       "use_seating_chart": false,
#       "tax": 0,
#       "form_option": [
#         "firstname",
#         "lastname",
#         "email",
#         "telephone",
#         "identity_id"
#       ],
#       "display_option": [
#         "firstname",
#         "lastname",
#         "email",
#         "telephone",
#         "identity_id"
#       ],
#       "checkin_option": [
#         "name",
#         "email",
#         "phone",
#         "payment",
#         "ticket",
#         "invoice_code"
#       ],
#       "evoucher_type": 1,
#       "status_schedule": 1,
#       "status_schedule_name": "ACTIVE",
#       "evoucher_type_name": "Evoucher",
#       "refund_status": 0,
#       "location": {
#         "id_location": 49541,
#         "location_name": "Jakarta",
#         "id_country": 1,
#         "country_name": "Indonesia",
#         "id_province": 6,
#         "province_name": "DKI Jakarta",
#         "id_district": 3143,
#         "district_name": "Online",
#         "id_region": 5687,
#         "region_name": "Online",
#         "address": "DKI Jakarta",
#         "postal_code": "",
#         "latitude": -6.17539,
#         "longitude": 106.827,
#         "status_location": 1,
#         "status_location_name": "ACTIVE"
#       },
#       "groups": [
#         {
#           "id_group": 55682,
#           "id_schedule": 49544,
#           "group_name": "Self Service Group",
#           "is_unique_email": false,
#           "max_transaction": 5,
#           "id_country": 1,
#           "ticket_multiply": 1,
#           "ticket_minimum": 1,
#           "is_same_ticket": false,
#           "show_in_widget": 0,
#           "expired_widget": "",
#           "show_in_api": 1,
#           "expired_api": "2038-01-19 10:14:07",
#           "show_in_ticketbox": false,
#           "ticketbox_input_type": 2,
#           "ticketbox_input_type_name": "Dropdown",
#           "ticketbox_checkin": false,
#           "widget_code": "j59iv9dniutl36j3",
#           "widget_url": "https://widget.loket.com/widget/j59iv9dniutl36j3",
#           "is_enable_invitation": false,
#           "is_enable_coupon": false,
#           "banner_name": "",
#           "banner_mobile_name": "",
#           "group_banner": 0,
#           "background_name": "",
#           "group_background": 0,
#           "currency_code": "IDR",
#           "currency_prefix": "Rp. ",
#           "seating_type": 2,
#           "seating_type_name": "BEST",
#           "enable_whatsapp_notif": true,
#           "participant_evoucher": false,
#           "is_associate_gate_barcode": false,
#           "show_promotor_logo": false,
#           "show_widget_title": true,
#           "default_language": "ind",
#           "status_group": 1,
#           "bulk_attendee": 2,
#           "bulk_attendee_name": "INACTIVE",
#           "status_group_name": "ACTIVE",
#           "tickets": [
#             {
#               "id_ticket": 121687,
#               "id_ticket_external": "",
#               "id_ticket_type": 110703,
#               "ticket_type": "Early Bird",
#               "description": "",
#               "start_sale": "2021-03-06 00:00:00",
#               "end_sale": "2021-04-01 23:00:00",
#               "price": 100000,
#               "basic_price": 100000,
#               "initial_price": 0,
#               "quantity": 250,
#               "available": true,
#               "available_qty": 226,
#               "is_specific_setting": false,
#               "is_enable_waitlist": false,
#               "ticket_order": 0,
#               "ticket_minimum": 1,
#               "max_transaction": 5,
#               "ticket_multiply": 1,
#               "show_in_widget": false,
#               "show_in_ticketbox": false,
#               "ticket_seating_chart": false,
#               "ticket_color": null,
#               "hold_end_date": null,
#               "hold_message": null,
#               "status_ticket": 6,
#               "is_enable_hide_not_started": false,
#               "stock_mode": 1,
#               "expired_time_checkin": 0,
#               "status_ticket_name": "SALE ENDED",
#               "stock_mode_name": "NORMAL_STOCK",
#               "tags": [],
#               "max_buy_qty": 5
#             },
#             {
#               "id_ticket": 121688,
#               "id_ticket_external": "",
#               "id_ticket_type": 110704,
#               "ticket_type": "Presale",
#               "description": "",
#               "start_sale": "2021-05-01 00:00:00",
#               "end_sale": "2021-05-31 00:00:00",
#               "price": 150000,
#               "basic_price": 150000,
#               "initial_price": 0,
#               "quantity": 150,
#               "available": true,
#               "available_qty": 141,
#               "is_specific_setting": false,
#               "is_enable_waitlist": false,
#               "ticket_order": 0,
#               "ticket_minimum": 1,
#               "max_transaction": 5,
#               "ticket_multiply": 1,
#               "show_in_widget": false,
#               "show_in_ticketbox": false,
#               "ticket_seating_chart": false,
#               "ticket_color": null,
#               "hold_end_date": null,
#               "hold_message": null,
#               "status_ticket": 2,
#               "is_enable_hide_not_started": false,
#               "stock_mode": 1,
#               "expired_time_checkin": 0,
#               "status_ticket_name": "INACTIVE",
#               "stock_mode_name": "NORMAL_STOCK",
#               "tags": [],
#               "max_buy_qty": 5
#             },
#             {
#               "id_ticket": 121689,
#               "id_ticket_external": "",
#               "id_ticket_type": 110705,
#               "ticket_type": "Presale",
#               "description": "",
#               "start_sale": "2021-06-01 00:00:00",
#               "end_sale": "2021-06-30 23:00:00",
#               "price": 150000,
#               "basic_price": 150000,
#               "initial_price": 0,
#               "quantity": 1000,
#               "available": true,
#               "available_qty": 899,
#               "is_specific_setting": false,
#               "is_enable_waitlist": false,
#               "ticket_order": 0,
#               "ticket_minimum": 1,
#               "max_transaction": 5,
#               "ticket_multiply": 1,
#               "show_in_widget": false,
#               "show_in_ticketbox": false,
#               "ticket_seating_chart": false,
#               "ticket_color": null,
#               "hold_end_date": null,
#               "hold_message": null,
#               "status_ticket": 6,
#               "is_enable_hide_not_started": false,
#               "stock_mode": 1,
#               "expired_time_checkin": 0,
#               "status_ticket_name": "SALE ENDED",
#               "stock_mode_name": "NORMAL_STOCK",
#               "tags": [],
#               "max_buy_qty": 5
#             },
#             {
#               "id_ticket": 136351,
#               "id_ticket_external": "",
#               "id_ticket_type": 124193,
#               "ticket_type": "CASTS",
#               "description": "",
#               "start_sale": "2021-06-29 02:00:00",
#               "end_sale": "2021-06-29 03:00:00",
#               "price": 10000,
#               "basic_price": 10000,
#               "initial_price": 0,
#               "quantity": 40,
#               "available": false,
#               "available_qty": 0,
#               "is_specific_setting": false,
#               "is_enable_waitlist": false,
#               "ticket_order": 0,
#               "ticket_minimum": 1,
#               "max_transaction": 5,
#               "ticket_multiply": 1,
#               "show_in_widget": false,
#               "show_in_ticketbox": false,
#               "ticket_seating_chart": false,
#               "ticket_color": null,
#               "hold_end_date": null,
#               "hold_message": null,
#               "status_ticket": 2,
#               "is_enable_hide_not_started": false,
#               "stock_mode": 1,
#               "expired_time_checkin": 0,
#               "status_ticket_name": "INACTIVE",
#               "stock_mode_name": "NORMAL_STOCK",
#               "tags": [],
#               "max_buy_qty": 0
#             },
#             {
#               "id_ticket": 136573,
#               "id_ticket_external": "",
#               "id_ticket_type": 124392,
#               "ticket_type": "REGULER",
#               "description": "",
#               "start_sale": "2021-07-01 00:00:00",
#               "end_sale": "2021-07-03 19:00:00",
#               "price": 200000,
#               "basic_price": 200000,
#               "initial_price": 0,
#               "quantity": 1000,
#               "available": true,
#               "available_qty": 934,
#               "is_specific_setting": false,
#               "is_enable_waitlist": false,
#               "ticket_order": 0,
#               "ticket_minimum": 1,
#               "max_transaction": 5,
#               "ticket_multiply": 1,
#               "show_in_widget": false,
#               "show_in_ticketbox": false,
#               "ticket_seating_chart": false,
#               "ticket_color": null,
#               "hold_end_date": null,
#               "hold_message": null,
#               "status_ticket": 6,
#               "is_enable_hide_not_started": false,
#               "stock_mode": 1,
#               "expired_time_checkin": 0,
#               "status_ticket_name": "SALE ENDED",
#               "stock_mode_name": "NORMAL_STOCK",
#               "tags": [],
#               "max_buy_qty": 5
#             }
#           ],
#           "fees": [
#             {
#               "id_invoice_cost": 514,
#               "cost_name": "Streaming fee",
#               "is_included_ticket_price": 2,
#               "nominal": 3000,
#               "cost_percent": 0,
#               "is_vendor_fee": 1,
#               "charge": 1,
#               "status": 1,
#               "charge_name": "PER TICKET",
#               "is_vendor_fee_name": "Vendor",
#               "is_included_ticket_price_name": "No",
#               "status_name": "ACTIVE"
#             }
#           ],
#           "payments": [
#             {
#               "id_list_payment": 1,
#               "id_parent_payment": 0,
#               "payment_name": "Credit Card",
#               "payment_type": 2,
#               "payment_type_name": "ONLINE",
#               "installment_term": null,
#               "payment_vendor": null,
#               "payment_vendor_name": null,
#               "expired_time_invoice": 0,
#               "expired_reminder": null,
#               "payment_custom_percent": 0,
#               "payment_custom_nominal": 0,
#               "payment_info": null,
#               "payment_info_ind": null,
#               "payment_logo": null,
#               "status_payment": 1,
#               "status_payment_name": "ACTIVE",
#               "id_group": null,
#               "payment_custom": null,
#               "childs": [
#                 {
#                   "id_list_payment": 6,
#                   "id_parent_payment": 1,
#                   "payment_name": "Credit / Debit Card",
#                   "payment_type": 2,
#                   "payment_type_name": "ONLINE",
#                   "installment_term": null,
#                   "payment_vendor": 1,
#                   "payment_vendor_name": "Midtrans",
#                   "expired_time_invoice": 900,
#                   "expired_reminder": 0,
#                   "payment_custom_percent": 3,
#                   "payment_custom_nominal": 5000,
#                   "payment_info": "We accept credit cards or debit online with Visa and MasterCard",
#                   "payment_info_ind": "Kami menerima kartu kredit atau debit online berlogo Visa dan MasterCard.\n",
#                   "payment_logo": "https://s3-ap-southeast-1.amazonaws.com/loket-production-sg/images/payment_logo/20200310123748.png",
#                   "status_payment": 1,
#                   "status_payment_name": "ACTIVE",
#                   "id_group": 55682,
#                   "payment_custom": {
#                     "config_bank": "bca",
#                     "config_is_secure": true,
#                     "expired_time_invoice": 900,
#                     "id_payment_custom": 330121,
#                     "payment_custom_nominal": 5000,
#                     "payment_custom_percent": 3
#                   },
#                   "childs": []
#                 }
#               ]
#             },
#             {
#               "id_list_payment": 3,
#               "id_parent_payment": 0,
#               "payment_name": "Virtual Account",
#               "payment_type": 2,
#               "payment_type_name": "ONLINE",
#               "installment_term": null,
#               "payment_vendor": null,
#               "payment_vendor_name": null,
#               "expired_time_invoice": 0,
#               "expired_reminder": null,
#               "payment_custom_percent": 0,
#               "payment_custom_nominal": 0,
#               "payment_info": null,
#               "payment_info_ind": null,
#               "payment_logo": null,
#               "status_payment": 1,
#               "status_payment_name": "ACTIVE",
#               "id_group": null,
#               "payment_custom": null,
#               "childs": [
#                 {
#                   "id_list_payment": 18,
#                   "id_parent_payment": 3,
#                   "payment_name": "ATM Transfer",
#                   "payment_type": 2,
#                   "payment_type_name": "ONLINE",
#                   "installment_term": null,
#                   "payment_vendor": 1,
#                   "payment_vendor_name": "Midtrans",
#                   "expired_time_invoice": 10800,
#                   "expired_reminder": 3600,
#                   "payment_custom_percent": 0,
#                   "payment_custom_nominal": 5000,
#                   "payment_info": "Payment using ATM Transfer",
#                   "payment_info_ind": "Pembayaran menggunakan metode Transfer ATM",
#                   "payment_logo": "https://s3-ap-southeast-1.amazonaws.com/loket-production-sg/images/payment_logo/20170529023111.jpg",
#                   "status_payment": 1,
#                   "status_payment_name": "ACTIVE",
#                   "id_group": 55682,
#                   "payment_custom": {
#                     "config_bank": "0",
#                     "config_is_secure": false,
#                     "expired_time_invoice": 10800,
#                     "id_payment_custom": 330114,
#                     "payment_custom_nominal": 4000,
#                     "payment_custom_percent": 0
#                   },
#                   "childs": []
#                 },
#                 {
#                   "id_list_payment": 34,
#                   "id_parent_payment": 3,
#                   "payment_name": "Virtual Account BCA",
#                   "payment_type": 2,
#                   "payment_type_name": "ONLINE",
#                   "installment_term": null,
#                   "payment_vendor": 1,
#                   "payment_vendor_name": "Midtrans",
#                   "expired_time_invoice": 10800,
#                   "expired_reminder": 3600,
#                   "payment_custom_percent": 0,
#                   "payment_custom_nominal": 5000,
#                   "payment_info": "Virtual Account BCA. <br>\nPayment can be done using KlikBCA Individu, ATM BCA or mBCA",
#                   "payment_info_ind": "Virtual Account BCA. <br>\nPembayaran dapat dilakukan melalui KlikBCA Individu, ATM BCA atau mBCA",
#                   "payment_logo": "https://s3-ap-southeast-1.amazonaws.com/loket-production-sg/images/payment_logo/20170125045852.png",
#                   "status_payment": 1,
#                   "status_payment_name": "ACTIVE",
#                   "id_group": 55682,
#                   "payment_custom": {
#                     "config_bank": "0",
#                     "config_is_secure": false,
#                     "expired_time_invoice": 10800,
#                     "id_payment_custom": 330115,
#                     "payment_custom_nominal": 4000,
#                     "payment_custom_percent": 0
#                   },
#                   "childs": []
#                 },
#                 {
#                   "id_list_payment": 54,
#                   "id_parent_payment": 3,
#                   "payment_name": "Alfamart",
#                   "payment_type": 2,
#                   "payment_type_name": "ONLINE",
#                   "installment_term": null,
#                   "payment_vendor": 3,
#                   "payment_vendor_name": "FasPay",
#                   "expired_time_invoice": 10800,
#                   "expired_reminder": 0,
#                   "payment_custom_percent": 0,
#                   "payment_custom_nominal": 5000,
#                   "payment_info": "Payment Point Alfamart",
#                   "payment_info_ind": "Bayar di Payment Point Alfamart",
#                   "payment_logo": "https://s3-ap-southeast-1.amazonaws.com/loket-production-sg/images/payment_logo/20170703104003.png",
#                   "status_payment": 2,
#                   "status_payment_name": "INACTIVE",
#                   "id_group": 55682,
#                   "payment_custom": {
#                     "config_bank": "0",
#                     "config_is_secure": false,
#                     "expired_time_invoice": 10800,
#                     "id_payment_custom": 330116,
#                     "payment_custom_nominal": 6000,
#                     "payment_custom_percent": 0
#                   },
#                   "childs": []
#                 },
#                 {
#                   "id_list_payment": 84,
#                   "id_parent_payment": 3,
#                   "payment_name": "Alfamart - Alfagroup",
#                   "payment_type": 2,
#                   "payment_type_name": "ONLINE",
#                   "installment_term": null,
#                   "payment_vendor": 1,
#                   "payment_vendor_name": "Midtrans",
#                   "expired_time_invoice": 10800,
#                   "expired_reminder": 0,
#                   "payment_custom_percent": 0,
#                   "payment_custom_nominal": 5000,
#                   "payment_info": "Complete your payment on Alfa Group Payment Point (Alfamart, Alfamidi, DAN+DAN)",
#                   "payment_info_ind": "Lakukan pembayaran di Alfa Group Payment Point (Alfamart, Alfamidi, DAN+DAN)",
#                   "payment_logo": "https://s3-ap-southeast-1.amazonaws.com/loket-production-sg/images/payment_logo/20191210015359.png",
#                   "status_payment": 2,
#                   "status_payment_name": "INACTIVE",
#                   "id_group": 55682,
#                   "payment_custom": {
#                     "config_bank": "0",
#                     "config_is_secure": false,
#                     "expired_time_invoice": 10800,
#                     "id_payment_custom": 330117,
#                     "payment_custom_nominal": 6000,
#                     "payment_custom_percent": 0
#                   },
#                   "childs": []
#                 },
#                 {
#                   "id_list_payment": 85,
#                   "id_parent_payment": 3,
#                   "payment_name": "Indomaret",
#                   "payment_type": 2,
#                   "payment_type_name": "ONLINE",
#                   "installment_term": null,
#                   "payment_vendor": 1,
#                   "payment_vendor_name": "Midtrans",
#                   "expired_time_invoice": 10800,
#                   "expired_reminder": 0,
#                   "payment_custom_percent": 0,
#                   "payment_custom_nominal": 5000,
#                   "payment_info": "Pembayaran menggunakan Indomaret",
#                   "payment_info_ind": "Pembayaran menggunakan Indomaret",
#                   "payment_logo": "https://s3-ap-southeast-1.amazonaws.com/loket-production-sg/images/payment_logo/20180417035629.png",
#                   "status_payment": 1,
#                   "status_payment_name": "ACTIVE",
#                   "id_group": 55682,
#                   "payment_custom": {
#                     "config_bank": "0",
#                     "config_is_secure": false,
#                     "expired_time_invoice": 10800,
#                     "id_payment_custom": 330118,
#                     "payment_custom_nominal": 6000,
#                     "payment_custom_percent": 0
#                   },
#                   "childs": []
#                 }
#               ]
#             },
#             {
#               "id_list_payment": 28,
#               "id_parent_payment": 0,
#               "payment_name": "Free Payment",
#               "payment_type": 2,
#               "payment_type_name": "ONLINE",
#               "installment_term": null,
#               "payment_vendor": 6,
#               "payment_vendor_name": "Free Payment",
#               "expired_time_invoice": 3600,
#               "expired_reminder": null,
#               "payment_custom_percent": 0,
#               "payment_custom_nominal": 0,
#               "payment_info": "Free Payment",
#               "payment_info_ind": null,
#               "payment_logo": null,
#               "status_payment": 1,
#               "status_payment_name": "ACTIVE",
#               "id_group": null,
#               "payment_custom": null,
#               "childs": [
#                 {
#                   "id_list_payment": 29,
#                   "id_parent_payment": 28,
#                   "payment_name": "Free Payment",
#                   "payment_type": 2,
#                   "payment_type_name": "ONLINE",
#                   "installment_term": null,
#                   "payment_vendor": 6,
#                   "payment_vendor_name": "Free Payment",
#                   "expired_time_invoice": 0,
#                   "expired_reminder": null,
#                   "payment_custom_percent": 0,
#                   "payment_custom_nominal": 0,
#                   "payment_info": "Free",
#                   "payment_info_ind": null,
#                   "payment_logo": null,
#                   "status_payment": 1,
#                   "status_payment_name": "ACTIVE",
#                   "id_group": 55682,
#                   "payment_custom": null,
#                   "childs": []
#                 }
#               ]
#             },
#             {
#               "id_list_payment": 43,
#               "id_parent_payment": 0,
#               "payment_name": "Wallet",
#               "payment_type": 2,
#               "payment_type_name": "ONLINE",
#               "installment_term": null,
#               "payment_vendor": null,
#               "payment_vendor_name": null,
#               "expired_time_invoice": 0,
#               "expired_reminder": null,
#               "payment_custom_percent": 0,
#               "payment_custom_nominal": 0,
#               "payment_info": null,
#               "payment_info_ind": null,
#               "payment_logo": null,
#               "status_payment": 1,
#               "status_payment_name": "ACTIVE",
#               "id_group": null,
#               "payment_custom": null,
#               "childs": [
#                 {
#                   "id_list_payment": 67,
#                   "id_parent_payment": 43,
#                   "payment_name": "GO-PAY",
#                   "payment_type": 2,
#                   "payment_type_name": "ONLINE",
#                   "installment_term": null,
#                   "payment_vendor": 1,
#                   "payment_vendor_name": "Midtrans",
#                   "expired_time_invoice": 900,
#                   "expired_reminder": 0,
#                   "payment_custom_percent": 1.5,
#                   "payment_custom_nominal": 0,
#                   "payment_info": "GO-PAY is an e-Wallet payment method by GO-JEK.  You will pay using the GO-JEK app.",
#                   "payment_info_ind": "GoPay adalah layanan pembayaran online yang disediakan oleh Gojek. Kamu akan membayarnya melalui aplikasi GO-JEK.",
#                   "payment_logo": "https://s3-ap-southeast-1.amazonaws.com/loket-production-sg/images/payment_logo/20201006041922.png",
#                   "status_payment": 1,
#                   "status_payment_name": "ACTIVE",
#                   "id_group": 55682,
#                   "payment_custom": {
#                     "config_bank": null,
#                     "config_is_secure": false,
#                     "expired_time_invoice": 900,
#                     "id_payment_custom": 330119,
#                     "payment_custom_nominal": 0,
#                     "payment_custom_percent": 1.5
#                   },
#                   "childs": []
#                 },
#                 {
#                   "id_list_payment": 82,
#                   "id_parent_payment": 43,
#                   "payment_name": "LinkAja",
#                   "payment_type": 2,
#                   "payment_type_name": "ONLINE",
#                   "installment_term": null,
#                   "payment_vendor": 3,
#                   "payment_vendor_name": "FasPay",
#                   "expired_time_invoice": 1800,
#                   "expired_reminder": 0,
#                   "payment_custom_percent": 0,
#                   "payment_custom_nominal": 3000,
#                   "payment_info": "Pay using LinkAja",
#                   "payment_info_ind": "Pembayaran menggunakan LinkAja",
#                   "payment_logo": "https://s3-ap-southeast-1.amazonaws.com/loket-production-sg/images/payment_logo/20191010065408.png",
#                   "status_payment": 1,
#                   "status_payment_name": "ACTIVE",
#                   "id_group": 55682,
#                   "payment_custom": {
#                     "config_bank": null,
#                     "config_is_secure": false,
#                     "expired_time_invoice": 1800,
#                     "id_payment_custom": 330120,
#                     "payment_custom_nominal": 3000,
#                     "payment_custom_percent": 0
#                   },
#                   "childs": []
#                 },
#                 {
#                   "id_list_payment": 87,
#                   "id_parent_payment": 43,
#                   "payment_name": "Shopee Pay",
#                   "payment_type": 2,
#                   "payment_type_name": "ONLINE",
#                   "installment_term": null,
#                   "payment_vendor": 1,
#                   "payment_vendor_name": "Midtrans",
#                   "expired_time_invoice": 900,
#                   "expired_reminder": 0,
#                   "payment_custom_percent": 1.5,
#                   "payment_custom_nominal": 0,
#                   "payment_info": "Payment using Shopee Pay",
#                   "payment_info_ind": "Pembayaran menggunakan Shopee Pay",
#                   "payment_logo": "https://s3-ap-southeast-1.amazonaws.com/loket-production-sg/images/payment_logo/20210414091539.png",
#                   "status_payment": 1,
#                   "status_payment_name": "ACTIVE",
#                   "id_group": 55682,
#                   "payment_custom": null,
#                   "childs": []
#                 },
#                 {
#                   "id_list_payment": 88,
#                   "id_parent_payment": 43,
#                   "payment_name": "Shopeepay QRIS",
#                   "payment_type": 2,
#                   "payment_type_name": "ONLINE",
#                   "installment_term": null,
#                   "payment_vendor": 1,
#                   "payment_vendor_name": "Midtrans",
#                   "expired_time_invoice": 900,
#                   "expired_reminder": 0,
#                   "payment_custom_percent": 1.5,
#                   "payment_custom_nominal": 0,
#                   "payment_info": "Shopeepay QRIS EN",
#                   "payment_info_ind": "Shopeepay QRIS ID",
#                   "payment_logo": "https://s3-ap-southeast-1.amazonaws.com/loket-production-sg/images/payment_logo/20210416032254.png",
#                   "status_payment": 1,
#                   "status_payment_name": "ACTIVE",
#                   "id_group": 55682,
#                   "payment_custom": null,
#                   "childs": []
#                 }
#               ]
#             }
#           ],
#           "installments": [],
#           "custom_policy": [],
#           "blocked_dates": [],
#           "ids_organization": [
#             194,
#             48
#           ]
#         }
#       ],
#       "custom_data": null
#     }
#   ],
#   "is_online_event": true,
#   "organization_avatar": "https://s3-ap-southeast-1.amazonaws.com/loket-production-sg/images/organization/20200703180134_5eff100e5b16e.png"
# }