ENVIRONMENT = "development"
# ENVIRONMENT = "production"

SETTINGS_MODULE = "config.settings.development"

if ENVIRONMENT == "development":
    SETTINGS_MODULE = "config.settings.development"
if ENVIRONMENT == "production":
    SETTINGS_MODULE = "config.settings.production"
