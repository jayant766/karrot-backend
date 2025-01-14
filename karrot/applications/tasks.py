import sentry_sdk
from anymail.exceptions import AnymailAPIError
from django.contrib.auth import get_user_model
from huey.contrib.djhuey import db_task

from karrot.applications.emails import prepare_new_application_notification_email, \
    prepare_application_accepted_email, prepare_application_declined_email
from karrot.groups.models import GroupMembership
from karrot.groups.models import GroupNotificationType


@db_task()
def notify_members_about_new_application(application):
    users = application.group.members.filter(
        groupmembership__in=GroupMembership.objects.active().with_notification_type(
            GroupNotificationType.NEW_APPLICATION
        ),
    ).exclude(
        id__in=get_user_model().objects.unverified(),
    )

    for user in users:
        try:
            prepare_new_application_notification_email(user, application).send()
        except AnymailAPIError:
            sentry_sdk.capture_exception()


@db_task()
def notify_about_accepted_application(application):
    prepare_application_accepted_email(application).send()


@db_task()
def notify_about_declined_application(application):
    prepare_application_declined_email(application).send()
