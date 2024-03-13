from django.contrib import admin
from import_export import resources,fields
from import_export.admin import ImportExportModelAdmin,ImportMixin
from .models import Student
from django.contrib.auth.models import User

# class StudentAdmin(admin.ModelAdmin):
    

# admin.site.register(Student, StudentAdmin)

# class StudentResource(resources.ModelResource):
#     class Meta:
#         model = Student
#         import_id_fields = ('rollNoId', )


# class StudentAdmin(ImportExportModelAdmin):
#     resource_class = StudentResource
#     list_display = ['firstname', 'lastname', 'rollNoId', 'email', 'semester', 'program', 'isGuideSelected', 'created_at', 'updated_at', 'project_name']
#     search_fields = ['firstname', 'lastname', 'rollNoId', 'email']  # Enable searching by these fields
#     list_filter = ['semester', 'program', 'isGuideSelected']  # Add filters for these fields

# admin.site.register(Student, StudentAdmin)

class StudentResource(resources.ModelResource):
    class Meta:
        model = Student
        fields = ('firstname', 'lastname', 'rollNoId', 'email', 'semester', 'program', 'isGuideSelected', 'created_at', 'updated_at', 'project_name')
        #exclude = ('id',)
        import_id_fields = ('rollNoId', )
    #user_username = fields.Field(column_name='username', attribute='user__username')
    #user_email = fields.Field(column_name='email', attribute='user__email')

#     # def before_import_row(self, row, **kwargs):
#     #     # Extract user data from the row
#     #     print("hellooo")
#     #     username = row.get('username')
#     #     email = row.get('email')
#     #     print("where")


#     #     # Create or update User object
#     #     if username and email:
#     #         print("here")
#     #         user, created = User.objects.get_or_create(username=username,email=email)
#     #         print("1")
#     #         row['user__username'] = user.username
#     #         print("2")
#     #         row['user__email'] = user.email
#     #         print("3")
#     #     else:
#     #         # Handle the case where either username or email is missing
#     #         print("missing")
#     #         row['user__username'] = None
#     #         row['user__email'] = None
#     def before_import_row(self, row, **kwargs):
#     # Extract user data from the row
#         username = row.get('username')
#         email = row.get('email')

#         # Create or update User object
#         if username and email:
#             try:
#                 user, created = User.objects.get_or_create(username=username, email=email)
#                 if created:
#                     row['user__username'] = user.username
#                     row['user__email'] = user.email
#             except Exception as e:
#                 # Handle any errors that occur during user creation
#                 print(f"Error creating user: {e}")
#                 row['user__username'] = None
#                 row['user__email'] = None
#         else:
#             # Handle the case where either username or email is missing
#             row['user__username'] = None
#             row['user__email'] = None

# # def skip_row(self, instance, original):
# #     # Skip importing User row if it's already created
# #     return instance and instance.user_id

#     def skip_row(self, instance, original):
#         # Skip importing User row if it's already created
#         return instance and instance.user_id


class StudentAdmin(ImportMixin, admin.ModelAdmin):
    resource_class = StudentResource
    list_display = ['firstname', 'lastname', 'rollNoId', 'email', 'semester', 'program', 'isGuideSelected', 'created_at', 'updated_at', 'project_name']
    search_fields = ['firstname', 'lastname', 'rollNoId', 'email']  # Enable searching by these fields
    list_filter = ['semester', 'program', 'isGuideSelected']  # Add filters for these fields
    actions = ['delete_selected_students']

    def delete_selected_students(self, request, queryset):
        queryset.delete()

    delete_selected_students.short_description = "Delete selected students"


    # def import_row(self, row, instance_loader, **kwargs):
    #     print("import row functionality")
    #     # Extract student data from the row
    #     username = row['email']
    #     email = row['email']
    #     firstname = row['firstname']
    #     lastname = row['lastname']

    #     # Create a new User instance
    #     user, created = User.objects.get_or_create(username=username, email=email)
    #     print("helloooooo")
    #     print(created)
    #     # Set a default password if necessary
    #     if created:
    #         user.set_password('default_password')
    #         user.save()

    #     # Associate the User with the Student instance
    #     instance = super().import_row(row, instance_loader, **kwargs)
    #     instance.user = user
    #     return instance

admin.site.register(Student, StudentAdmin)
