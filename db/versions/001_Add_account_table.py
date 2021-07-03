from sqlalchemy import Table, Column, Integer, String, MetaData

meta = MetaData()

account = Table(
        'account', meta,
        Column('id', Integer, primary_key=True),
        Column('login', String(40)),
        Column('passwd', String(40)),
        Column('nama', String(40)),
        )

def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind = migrate_engine
    account.create()
    # pass


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    account.drop()
    # pass
