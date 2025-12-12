from alembic import op
import sqlalchemy as sa


revision = '779e0323cf46'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('review_text', sa.Text(), nullable=False),
    sa.Column('sentiment', sa.Text(), nullable=True),
    sa.Column('key_points', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_reviews'))
    )

def downgrade():
    op.drop_table('reviews')
