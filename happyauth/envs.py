from dataclasses import dataclass
from environs import Env

from .dirs import BASE_DIR


@dataclass
class DjangoConfig:
    secret_key: str
    su_name: str
    su_password: str
    su_email: str


@dataclass
class Config:
    django: DjangoConfig


def load_config() -> Config:
    env: Env = Env()
    env.read_env(BASE_DIR / ".env")

    return Config(
        django=DjangoConfig(
            secret_key=env.str("DJANGO_SECRETKEY"),
            su_name=env.str("DJANGO_SUPERUSER_NAME"),
            su_password=env.str("DJANGO_SUPERUSER_PASSWORD"),
            su_email=env.str("DJANGO_SUPERUSER_EMAIL"),
        ),
    )
