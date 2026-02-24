"""
Configuration file for Blood Group Prediction Flask App.
Supports development and production environments.
"""
import os
from datetime import timedelta


class Config:
    """Base configuration."""
    
    # Secret key for sessions
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    
    # Database
    DATABASE = os.environ.get('DATABASE', 'database.db')
    
    # Upload settings
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp'}
    
    # Static folders
    STATIC_FOLDER = os.environ.get('STATIC_FOLDER', 'static')
    
    # Model paths
    MODEL_PATH = os.environ.get('MODEL_PATH', '.')
    SCALER_PATH = os.environ.get('SCALER_PATH', 'scaler.pkl')
    ENCODER_PATH = os.environ.get('ENCODER_PATH', 'encoder.pkl')
    
    # Session settings
    PERMANENT_SESSION_LIFETIME = timedelta(hours=24)
    SESSION_COOKIE_SECURE = False
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    
    # Logging
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')
    LOG_FILE = os.environ.get('LOG_FILE', 'app.log')
    
    # ML Feature list
    ALL_FEATURES = [
        'fundus_cnn_pca1', 'fundus_AVR', 'fundus_vessel_redness',
        'fundus_tortuosity', 'fundus_vessel_density',
        'sclera_cnn_pca1', 'sclera_AVR', 'sclera_mean_hue',
        'sclera_redness', 'sclera_perivascular_contrast'
    ]


class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    TESTING = False
    
    # Development settings
    SESSION_COOKIE_SECURE = False
    LOG_LEVEL = 'DEBUG'
    
    # Auto-train if models missing
    AUTO_TRAIN = True


class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    TESTING = False
    
    # Production security
    SESSION_COOKIE_SECURE = True
    LOG_LEVEL = 'WARNING'
    
    # No auto-training in production
    AUTO_TRAIN = False
    
    @classmethod
    def init_app(cls, app):
        """Initialize production-specific configuration."""
        # Enforce secure cookie settings
        app.config['SESSION_COOKIE_SECURE'] = True
        app.config['SESSION_COOKIE_HTTPONLY'] = True
        app.config['SESSION_COOKIE_SAMESITE'] = 'Strict'


class TestingConfig(Config):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    DATABASE = 'test_database.db'
    WTF_CSRF_ENABLED = False


# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}


def get_config(env=None):
    """Get configuration based on environment.
    
    Args:
        env: Environment name (development, production, testing)
        
    Returns:
        Configuration class
    """
    if env is None:
        env = os.environ.get('FLASK_ENV', 'development')
    return config.get(env, DevelopmentConfig)
