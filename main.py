from global_settings import settings

print("Entorno:", settings.environment)
print("Base de datos:", settings.database.url)
print("Directorio base:", settings.directories.base_dir)
print("Email de soporte:", settings.emails.support_email)
