from core.configs import settings
from core.database import engine


async def create_table() -> None:
    import models.__all_models

    print('Criando as tabelas no banco...')

    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
    print('Todas as tabelas criadas com sucesso.')


if __name__ == '__main__':
    import asyncio

    asyncio.run(create_table())