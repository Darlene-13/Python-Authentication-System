# Django Authentication System

A comprehensive authentication system built with Django REST Framework, featuring JWT authentication, OAuth2 integration, two-factor authentication, and Redis-based rate limiting.

## Project Overview

This Django-based authentication system serves as a production-ready backend service that handles user authentication, authorization, and security features. Built to demonstrate advanced Django/DRF concepts and serve as a foundation for scalable web applications.

## Features

### Core Authentication
- [x] User registration and email verification
- [x] JWT-based authentication (access & refresh tokens)
- [x] Secure password hashing with Django's built-in system
- [x] Password strength validation
- [x] Password reset via email
- [x] User profile management

### Authorization & Permissions
- [x] Role-based access control (RBAC)
- [x] Custom permission classes
- [x] Group-based permissions
- [x] Resource-level permissions
- [x] API endpoint protection

### Security Features
- [x] Redis-based rate limiting (no django-axes)
- [x] Account lockout after failed attempts
- [x] IP-based rate limiting
- [x] CORS configuration
- [x] Security headers middleware
- [x] Audit logging for authentication events

### OAuth2 & Social Authentication
- [x] Google OAuth2 integration
- [x] GitHub OAuth2 integration
- [x] Social account linking
- [x] Profile data synchronization

### Two-Factor Authentication
- [x] TOTP (Time-based One-Time Password)
- [x] Email-based OTP
- [x] QR code generation for authenticator apps
- [x] Backup codes generation
- [x] 2FA enforcement policies

### API Features
- [x] RESTful API design
- [x] OpenAPI/Swagger documentation
- [x] API versioning
- [x] Proper HTTP status codes
- [x] Error handling and validation
- [x] Pagination for list endpoints

## Tech Stack

### Core Framework
- **Django**: Web framework
- **Django REST Framework**: API development
- **PostgreSQL**: Primary database
- **Redis**: Caching and rate limiting

### Authentication & Security
- **djangorestframework-simplejwt**: JWT implementation
- **django-allauth**: OAuth2 and social authentication
- **django-cors-headers**: CORS handling
- **django-redis**: Redis integration

### Development & Testing
- **pytest**: Testing framework
- **pytest-django**: Django-specific testing tools
- **factory-boy**: Test data generation
- **coverage**: Code coverage analysis

### Documentation & API
- **drf-yasg**: Swagger/OpenAPI documentation
- **django-extensions**: Development utilities

### Deployment
- **gunicorn**: WSGI server
- **Docker**: Containerization
- **whitenoise**: Static file serving

## Project Structure

```
auth-django/
├── README.md
├── requirements.txt
├── requirements-dev.txt
├── manage.py
├── pytest.ini
├── .env.example
├── Dockerfile
├── docker-compose.yml
├── auth_project/
│   ├── settings/
│   │   ├── base.py
│   │   ├── development.py
│   │   ├── production.py
│   │   └── testing.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   ├── authentication/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── permissions.py
│   │   └── tests/
│   ├── users/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── tests/
│   ├── oauth/
│   │   ├── views.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── tests/
│   └── core/
│       ├── middleware.py
│       ├── permissions.py
│       ├── throttles.py
│       ├── utils.py
│       └── exceptions.py
├── static/
├── media/
├── logs/
└── tests/
    ├── fixtures/
    ├── integration/
    └── unit/
```

## API Endpoints

### Authentication Endpoints
- `POST /api/v1/auth/register/` - User registration
- `POST /api/v1/auth/login/` - User login
- `POST /api/v1/auth/logout/` - User logout
- `POST /api/v1/auth/refresh/` - Refresh JWT token
- `POST /api/v1/auth/verify-email/` - Verify email address
- `POST /api/v1/auth/forgot-password/` - Request password reset
- `POST /api/v1/auth/reset-password/` - Reset password

### User Management Endpoints
- `GET /api/v1/users/profile/` - Get user profile
- `PUT /api/v1/users/profile/` - Update user profile
- `DELETE /api/v1/users/profile/` - Delete user account
- `GET /api/v1/users/` - List users (Admin only)
- `GET /api/v1/users/{id}/` - Get user details (Admin only)
- `DELETE /api/v1/users/{id}/` - Delete user (Admin only)

### OAuth2 Endpoints
- `GET /api/v1/oauth/google/` - Google OAuth2 redirect
- `GET /api/v1/oauth/github/` - GitHub OAuth2 redirect
- `POST /api/v1/oauth/callback/` - OAuth2 callback handler
- `POST /api/v1/oauth/link/` - Link social account
- `DELETE /api/v1/oauth/unlink/` - Unlink social account

### Two-Factor Authentication Endpoints
- `POST /api/v1/auth/2fa/setup/` - Setup 2FA
- `POST /api/v1/auth/2fa/verify/` - Verify 2FA code
- `POST /api/v1/auth/2fa/disable/` - Disable 2FA
- `GET /api/v1/auth/2fa/qr/` - Get QR code for setup
- `GET /api/v1/auth/2fa/backup-codes/` - Get backup codes
- `POST /api/v1/auth/2fa/regenerate-backup/` - Regenerate backup codes

## Database Models

### User Model
Extended Django's AbstractUser with additional fields:
- Email verification status
- Phone number
- 2FA settings
- Account lockout information
- Login tracking
- Timestamps

### Role Model
Custom role system for RBAC:
- Role name and description
- Associated permissions
- User assignments

### Social Account Model
OAuth2 account linking:
- Provider information
- Social account details
- User association

### Audit Log Model
Security event tracking:
- Authentication attempts
- Permission changes
- Account modifications
- IP address tracking

## Configuration

### Environment Variables
- `SECRET_KEY` - Django secret key
- `DEBUG` - Debug mode flag
- `DATABASE_URL` - PostgreSQL connection string
- `REDIS_URL` - Redis connection string
- `EMAIL_HOST` - SMTP server configuration
- `GOOGLE_OAUTH2_CLIENT_ID` - Google OAuth2 credentials
- `GITHUB_OAUTH2_CLIENT_ID` - GitHub OAuth2 credentials

### Redis Configuration
- Rate limiting storage
- JWT blacklist storage
- Session caching
- OTP temporary storage

### Email Configuration
- SMTP settings for email verification
- Password reset emails
- 2FA OTP delivery
- Account notification emails

## Security Features

### Rate Limiting Strategy
- IP-based limiting for anonymous users
- User-based limiting for authenticated users
- Different limits for different endpoints
- Configurable time windows
- Redis-based storage for scalability

### Authentication Security
- Strong password requirements
- Password history checking
- Account lockout after failed attempts
- JWT token rotation
- Secure token storage

### API Security
- CORS configuration
- Security headers
- Input validation
- SQL injection prevention
- XSS protection

## Testing Strategy

### Unit Tests
- Model validation tests
- Serializer tests
- View logic tests
- Utility function tests
- Permission tests

### Integration Tests
- API endpoint tests
- Authentication flow tests
- OAuth2 integration tests
- Rate limiting tests
- 2FA workflow tests

### Security Tests
- Authentication bypass attempts
- Permission escalation tests
- Rate limit bypass tests
- Input validation tests
- Session security tests

### Performance Tests
- Load testing for auth endpoints
- Database query optimization
- Redis performance tests
- Response time benchmarks

## Development Workflow

### Phase 1: Foundation (Week 1-2)
- [ ] Project setup and configuration
- [ ] User model and basic authentication
- [ ] JWT implementation
- [ ] Basic API endpoints
- [ ] Initial tests

### Phase 2: Security & Authorization (Week 2-3)
- [ ] RBAC implementation
- [ ] Permission system
- [ ] JWT refresh mechanism
- [ ] Input validation
- [ ] Security middleware

### Phase 3: Rate Limiting (Week 3-4)
- [ ] Redis integration
- [ ] Rate limiting middleware
- [ ] IP-based rate limiting
- [ ] User-based rate limiting
- [ ] Rate limit headers

### Phase 4: OAuth2 Integration (Week 4-5)
- [ ] Google OAuth2 setup
- [ ] GitHub OAuth2 setup
- [ ] Social account linking
- [ ] Profile synchronization
- [ ] OAuth2 tests

### Phase 5: Two-Factor Authentication (Week 5-6)
- [ ] TOTP implementation
- [ ] Email OTP system
- [ ] QR code generation
- [ ] Backup codes
- [ ] 2FA enforcement

### Phase 6: Advanced Features (Week 6-7)
- [ ] Password reset flow
- [ ] Email verification
- [ ] Account lockout policies
- [ ] Audit logging
- [ ] Admin interface

### Phase 7: Documentation & Testing (Week 7-8)
- [ ] API documentation
- [ ] Comprehensive testing
- [ ] Performance optimization
- [ ] Security audit
- [ ] Code review

### Phase 8: Deployment (Week 8)
- [ ] Docker configuration
- [ ] Production settings
- [ ] Environment setup
- [ ] Monitoring integration
- [ ] Deployment automation

## Deployment

### Docker Setup
- Multi-stage Docker build
- Environment-specific configurations
- Health checks
- Volume management
- Network configuration

### Production Considerations
- Database connection pooling
- Redis clustering
- Load balancing
- SSL/TLS configuration
- Monitoring and logging

### Environment Management
- Development environment
- Testing environment
- Staging environment
- Production environment

## Monitoring & Observability

### Logging
- Authentication events
- Error tracking
- Performance metrics
- Security incidents
- User activity

### Metrics
- Response times
- Error rates
- Authentication success/failure rates
- Rate limiting hits
- 2FA usage statistics

### Alerts
- Failed authentication spikes
- Rate limit breaches
- System errors
- Performance degradation
- Security incidents

## Contributing

### Code Standards
- PEP 8 compliance
- Type hints where applicable
- Comprehensive docstrings
- Proper error handling
- Test coverage requirements

### Git Workflow
- Feature branch development
- Pull request reviews
- Automated testing
- Code quality checks
- Documentation updates

## Resources

### Django Documentation
- Django official documentation
- Django REST Framework documentation
- Django security best practices
- Django deployment guide

### Security Resources
- OWASP Authentication Guidelines
- JWT security best practices
- OAuth2 specification
- 2FA implementation guide

### Testing Resources
- pytest documentation
- Django testing guide
- API testing strategies
- Security testing methods

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For questions, issues, or contributions, please refer to the project's issue tracker or contact the development team.