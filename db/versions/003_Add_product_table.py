from sqlalchemy import Table, Column, Integer, String, MetaData

meta = MetaData()

product = Table(
        'product', meta,
        Column('id', Integer, primary_key=True),
        Column('nama', String(40)),
        Column('kategori', Integer),
        Column('stok', Integer),
        )

def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind = migrate_engine
    product.create()
    # pass


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    # pass
    meta.bind = migrate_engine()
    product.drop()
