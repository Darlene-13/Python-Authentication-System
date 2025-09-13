from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import timedelta


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('User', 'User'),
        ('Manager', 'Manager'),
    ]
    username = models.CharField(max_length=150, help_text="Required. Enter a username.")
    email = models.EmailField(unique=True, help_text="Required. Enter a valid email address.")
    first_name = models.CharField(max_length=30, help_text="Required. Enter your first name.")
    last_name = models.CharField(max_length=30, help_text="Required. Enter your last name.")
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, blank=True, null=True, help_text="Optional. Define the user's role within the system.")
    is_active = models.BooleanField(default=True, help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.")
    date_joined = models.DateTimeField(auto_now_add=True, help_text = "Records the date and time when the user account was created. ")
    is_staff = models.BooleanField(default=False, help_text="Designates whether the user can log into this admin site.")
    is_superuser = models.BooleanField(default=False, help_text="Designates that this user has all permissions without explicitly assigning them.")
    phone_number = models.CharField(max_length=15, blank=True, null=True, help_text="Optional. Enter your phone number.")
    is_email_verified = models.BooleanField(default=False, help_text="Designates whether the user's email has been verified.")
    is_2fa_enabled = models.BooleanField(default=False, help_text="Designates whether two-factor authentication is enabled for the user.")
    failed_login_attempts = models.IntegerField(default=0, help_text="Counts the number of consecutive failed login attempts.")
    locked_until = models.DateTimeField(blank=True, null=True, help_text="If the account is locked due to too many failed login attempts, this field records the time until which the account remains locked.")
    last_login_ip = models.GenericIPAddressField(blank=True, null=True, help_text="Records the IP address from which the user last logged in.")
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True, help_text="Optional. Upload a profile picture.")
    bio = models.TextField(blank=True, null=True, help_text="Optional. Write a short bio about yourself.")


    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'custom_user'
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'
        ordering = ['username']
        indexes = [
            models.Index(fields=['email'], name='email_idx'),
            models.Index(fields=['is_active'], name='active_idx'),
        ]
        permissions = [
            ("can_view_profile", "Can view user profile"),
            ("can_edit_profile", "Can edit user profile"),
        ]
        

    
    def get_full_name(self):
        """
        Return the first name plus the last name with a space in between.
        """
        return f"{self.first_name} {self.last_name}".strip()
    
    def get_short_name(self):
        """
        Returns the short name of the user
        """
        return self.first_name or self.username
    
    def can_login(self):
        """
        Returns true if the user is active and not locked out
        """
        return self.is_active and (self.locked_until is None or self.locked_until < timezone.now()) 
    
    def increment_failed_logins(self):
        """
        Returns the number of failed login attempts
        """
        self.failed_login_attempts += 1
        self.save(update_fields=['failed_login_attempts'])
        return self.failed_login_attempts
    
    def reset_failed_logins(self):
        """
        Resets the failed login attempts to zero
        """
        self.failed_login_attempts = 0
        self.locked_until = None
        self.save(update_fields=['failed_login_attempts', 'locked_until'])

    def lock_account(self, duration_minutes=5):
        """
        Locks the user account for the specified duration in minutes for instance here 5 minutes
        """
        self.locked_until = timezone.now() + timedelta(minutes=duration_minutes)
        self.save(update_fields=['locked_until'])

    def is_account_locked(self):
        """
        Returns true if the account is currently locked, false otherwise
        """
        return self.locked_until is not None and self.locked_until > timezone.now()
    
    def has_role(self, role_name):
        """
        Checks if the user has a specific role
        """
        return self.groups.filter(name=role_name).exists()
    
    def is_admin(self):
        """
        Returns true if the user is an admin
        """
        return self.is_superuser or self.has_role('Admin')
    
    def get_permissions(self):
        """
        Returns a list of all permissions the user has
        """
        return self.get_all_permissions()