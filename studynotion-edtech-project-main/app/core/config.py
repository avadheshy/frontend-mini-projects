from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Studynotion EdTech API"
    api_v1_str: str = "/api/v1"
    mongodb_url: str = "mongodb://localhost:27017"
    mongodb_db: str = "studynotion"
    jwt_secret: str = "change-me"
    jwt_expire_hours: int = 24

    mail_host:str= 'smtp.gmail.com'
    mail_user: str='avadheshy2015@gmail.com'
    mail_pass: str ='dawkooiuahyxruqf'
    

    cloud_name: str | None = None
    cloud_api_key: str | None = None
    cloud_api_secret: str | None = None
    cloud_folder: str | None = None

    razorpay_key: str | None = None
    razorpay_secret: str | None = None

    frontend_reset_url: str = "https://studynotion-edtech-project.vercel.app/update-password"

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
