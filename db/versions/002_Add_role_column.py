from sqlalchemy import Table, MetaData, String, Column

def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    # pass
    meta = MetaData(bind=migrate_engine)
    account = Table('account', meta, autoload=True)
    rolec = Column('role', String(20))
    rolec.create(account)


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    # pass
    meta = MetaData(bind=migrate_engine)
    account = Table('account', meta, autoload=True)
    account.c.role.drop()
