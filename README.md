## Installation
- Copy the directory `token_authenticaiton` app to your Django project
- Insert `token_authentication` to the INSTALLED_APPS in your main project setttings (settings.py)
- Create the migration: `python manage.py makemigrations token_authentication`
- Apply the migration: `python manage.py migrate`
- Create a role with the create_role API or manually create in your database (table: user_role)
- (Optional) make the url: `path('token_authentication/', include('token_authentication.urls', namespace='token_authentication_ns'))`
- (Optional) disable CSRF from middleware
