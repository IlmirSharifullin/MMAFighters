from src.settings import Settings
from dotenv import load_dotenv

load_dotenv()


def main():
    settings: Settings = Settings()
    print(settings.build_postgres_dsn())


if __name__ == '__main__':
    main()