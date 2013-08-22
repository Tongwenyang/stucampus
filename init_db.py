#-*- coding: utf-8
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType

from stucampus.account.models import Student
from stucampus.organization.models import Organization


DEFAULT_ADMIN_EMAIL = 'stucampus@live.cn'
DEFAULT_ADMIN_PASSWORD = '123456'
DEFAULT_ADMIN_NAME = 'stucampus'


create_perm = Permission.objects.create
create_group = Group.objects.create
get_content_type = ContentType.objects.get


def create_groups():
    global admin_group
    admin_group = create_group(name='StuCampus')
    organization_manager_group = create_group(name='organization_manager')
    organization_member_group = create_group(name='organization_member')


def create_permissions():
    # Content_type for permissions
    student_model_content_type = get_content_type(app_label='account')
    organization_content_type = get_content_type(app_label='organization')

    # Permissions for student
    student_list = create_perm(codename='student_list',
                               name='List all students',
                               content_type=student_model_content_type)
    student_view = create_perm(codename='student_view', 
                               name='View the information of student.',
                               content_type=student_model_content_type)
    student_create = create_perm(codename='student_create',
                                 name='Create new student.',
                                 content_type=student_model_content_type)
    student_edit = create_perm(codename='student_edit',
                               name='Edit the information of students.',
                               content_type=student_model_content_type)
    student_del = create_perm(codename='student_del',
                              name='Delete student.',
                              content_type=student_model_content_type)

    # Permissions for organization
    organization_list = create_perm(codename='organization_list',
                                    name='List all organizations.',
                                    content_type=organization_content_type)
    organization_view = create_perm(codename='organization_view',
                                    name='View information of organization.',
                                    content_type=organization_content_type)
    organization_create = create_perm(codename='organization_create',
                                      name='Create organization.',
                                      content_type=organization_content_type)
    organization_edit = create_perm(codename='organization_edit',
                                    name='Edit information of organization.',
                                    content_type=organization_content_type)
    organization_del = create_perm(codename='organization_del',
                                   name='Delete the organization.',
                                   content_type=organization_content_type)

    # Permissions for adding organization manager.
    manager_list = create_perm(codename='org_manager_list',
                               name='List all managers of a organization.',
                               content_type=student_model_content_type)
    managers_create = create_perm(codename='org_manager_create',
                                  name='Create new manager.',
                                  content_type=student_model_content_type)
    managers_del = create_perm(codename='org_manager_del',
                               name='Delete manager of a organization',
                               content_type=student_model_content_type)

    # Permissions for organization members
    member_list = create_perm(codename='member_list',
                              name='List the members in a organization.',
                              content_type=student_model_content_type)
    member_view = create_perm(codename='member_view',
                              name='View the information of member.',
                              content_type=student_model_content_type)
    member_create = create_perm(codename='member_create',
                                name='Create member in a organization.',
                                content_type=student_model_content_type)
    member_del = create_perm(codename='member_del',
                             name='Delete member from a organization',
                             content_type=student_model_content_type)


def create_stucampus_organization():
    global org
    org = Organization.objects.create(name='深圳大学学子天地')
    org.url = 'http://stu.szu.edu.cn'
    org.logo = '/static/images/layout/logo3.png'
    org.save()


def create_user():
    global admin_user
    admin_email = (raw_input('Please input the email of admin, '
                             'or leave blank for %s.\n' % DEFAULT_ADMIN_EMAIL)
                   or DEFAULT_ADMIN_EMAIL)
    admin_password = (raw_input('Please input the password of admin, '
                                'or leave blank for %s\n'
                                % DEFAULT_ADMIN_PASSWORD)
                      or DEFAULT_ADMIN_PASSWORD)
    admin_name = (raw_input('Please input the name of admin, '
                            'or leave blank for %s\n'
                            % DEFAULT_ADMIN_NAME)
                  or DEFAULT_ADMIN_NAME)
    admin_user = User.objects.create_user(username=admin_email,
                                          email=admin_email,
                                          password=admin_password)
    student = Student.objects.create(user=admin_user, screen_name=admin_name)


def bind():
    admin_user.groups.add(admin_group)
    org.managers.add(admin_user.student)
    perms = Permission.objects.all()
    for perm in perms:
        admin_group.permissions.add(perm)


def run():
    create_groups()
    create_permissions()
    create_stucampus_organization()
    create_user()
    bind()