from environs import Env
from dataclasses import dataclass


@dataclass
class Bots:
    bot_token: str
    creator: str
    admin_ids: list

@dataclass
class Settings:
    bot: Bots


def get_settings(path: str):
    env = Env()
    env.read_env(path)
    return Settings(
        Bots(
            bot_token=env.str("BOT_TOKEN"),
            creator=env.str("CREATOR"),
            admin_ids=env.str("ADMIN_IDS").split(":")
        )
    )

setting = get_settings("input")
