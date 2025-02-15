from pydantic_settings import BaseSettings, SettingsConfigDict
import aiosqlite

class Settings(BaseSettings):
    sqlite_db: str = 'database.db'

    email_address: str
    email_password: str
    email_server: str

    jwt_secret: str


    api_link: str
    files_dir: str = 'assets/images'
    upload_dir: str = 'static'
    date_format: str = '%Y-%m-%d'
    date_time_format: str = '%Y-%m-%d %H:%M'

    model_config = SettingsConfigDict(env_file='.env')

    def get_async_uri(self):
        return f'sqlite+aiosqlite:///{self.sqlite_db}'

    def get_uri(self):
        return f'sqlite+sqlite:///{self.sqlite_db}'



settings = Settings()
