from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, email,
                    first_name, last_name, gender, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, email, first_name, last_name, gender,  **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            password=password,
            **extra_fields
        )
    
    def is_unique(self, username, email):
        isUnique = True
        usernameUsed = self.model.objects.filter(username=username).count()
        emailUsed = self.model.objects.filter(email=email).count()
        message = ''
        if usernameUsed:
            message += f'The username {username} is already taken. Choose another one.\n'
            isUnique = False
        if emailUsed:
            message += f'The email {email} is already taken. Choose another one.\n'
            isUnique = False
        return {
            'is_unique':isUnique,
            'message':message,
        }
