import sys

from alembic.config import CommandLine, Config

from src.infrastructure.database.settings import AlembicSettings, DBSettings


def make_config() -> Config:
    db_settings = DBSettings()
    alembic_settings = AlembicSettings()
    config = Config()
    print(db_settings.DB_URL)
    config.set_main_option("script_location", alembic_settings.ALEMBIC_SCRIPT_LOCATION)
    config.set_main_option("version_locations", alembic_settings.ALEMBIC_VERSION_LOCATIONS)
    config.set_main_option("sqlalchemy.url", db_settings.DB_URL)
    config.set_main_option(
        "file_template", alembic_settings.ALEMBIC_MIGRATION_FILENAME_TEMPLATE
    )
    config.set_main_option("timezone", "UTC")
    return config


def run_cmd(*args: str) -> None:
    cli = CommandLine()
    cli.run_cmd(make_config(), cli.parser.parse_args(args))


if __name__ == "__main__":
    run_cmd(*sys.argv[1:])
