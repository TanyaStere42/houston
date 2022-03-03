# -*- coding: utf-8 -*-
"""empty message

Revision ID: 19dd4e2c1e63
Revises: e9df5182903a
Create Date: 2022-02-15 00:05:23.174018

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19dd4e2c1e63'
down_revision = 'ea69d76faa6b'


def upgrade():
    """
    Upgrade Semantic Description:
        ENTER DESCRIPTION HERE
    """
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('annotation', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'indexed',
                sa.DateTime(),
                nullable=False,
                server_default=sa.func.current_timestamp(),
            )
        )
        batch_op.create_index(
            batch_op.f('ix_annotation_indexed'), ['indexed'], unique=False
        )

    with op.batch_alter_table('annotation_keywords', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'indexed',
                sa.DateTime(),
                nullable=False,
                server_default=sa.func.current_timestamp(),
            )
        )
        batch_op.create_index(
            batch_op.f('ix_annotation_keywords_indexed'), ['indexed'], unique=False
        )

    with op.batch_alter_table('asset', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'indexed',
                sa.DateTime(),
                nullable=False,
                server_default=sa.func.current_timestamp(),
            )
        )
        batch_op.create_index(batch_op.f('ix_asset_indexed'), ['indexed'], unique=False)

    with op.batch_alter_table('asset_group_sighting', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'indexed',
                sa.DateTime(),
                nullable=False,
                server_default=sa.func.current_timestamp(),
            )
        )
        batch_op.create_index(
            batch_op.f('ix_asset_group_sighting_indexed'), ['indexed'], unique=False
        )

    with op.batch_alter_table('asset_tags', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'indexed',
                sa.DateTime(),
                nullable=False,
                server_default=sa.func.current_timestamp(),
            )
        )
        batch_op.create_index(
            batch_op.f('ix_asset_tags_indexed'), ['indexed'], unique=False
        )

    with op.batch_alter_table('audit_log', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'indexed',
                sa.DateTime(),
                nullable=False,
                server_default=sa.func.current_timestamp(),
            )
        )
        batch_op.create_index(
            batch_op.f('ix_audit_log_indexed'), ['indexed'], unique=False
        )

    with op.batch_alter_table('code', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'indexed',
                sa.DateTime(),
                nullable=False,
                server_default=sa.func.current_timestamp(),
            )
        )
        batch_op.create_index(batch_op.f('ix_code_indexed'), ['indexed'], unique=False)

    with op.batch_alter_table('collaboration', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'indexed',
                sa.DateTime(),
                nullable=False,
                server_default=sa.func.current_timestamp(),
            )
        )
        batch_op.create_index(
            batch_op.f('ix_collaboration_indexed'), ['indexed'], unique=False
        )

    with op.batch_alter_table('collaboration_user_associations', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'indexed',
                sa.DateTime(),
                nullable=False,
                server_default=sa.func.current_timestamp(),
            )
        )
        batch_op.create_index(
            batch_op.f('ix_collaboration_user_associations_indexed'),
            ['indexed'],
            unique=False,
        )

    with op.batch_alter_table('email_record', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'indexed',
                sa.DateTime(),
                nullable=False,
                server_default=sa.func.current_timestamp(),
            )
        )
        batch_op.create_index(
            batch_op.f('ix_email_record_indexed'), ['indexed'], unique=False
        )

    with op.batch_alter_table('encounter', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'indexed',
                sa.DateTime(),
                nullable=False,
                server_default=sa.func.current_timestamp(),
            )
        )
        batch_op.create_index(
            batch_op.f('ix_encounter_indexed'), ['indexed'], unique=False
        )

    with op.batch_alter_table('file_upload', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'indexed',
                sa.DateTime(),
                nullable=False,
                server_default=sa.func.current_timestamp(),
            )
        )
        batch_op.create_index(
            batch_op.f('ix_file_upload_indexed'), ['indexed'], unique=False
        )

    with op.batch_alter_table('git_store', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'indexed',
                sa.DateTime(),
                nullable=False,
                server_default=sa.func.current_timestamp(),
            )
        )
        batch_op.create_index(
            batch_op.f('ix_git_store_indexed'), ['indexed'], unique=False
        )

    with op.batch_alter_table('houston_config', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'indexed',
                sa.DateTime(),
                nullable=False,
                server_default=sa.func.current_timestamp(),
            )
        )
        batch_op.create_index(
            batch_op.f('ix_houston_config_indexed'), ['indexed'], unique=False
        )

    with op.batch_alter_table('individual', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'indexed',
                sa.DateTime(),
                nullable=False,
                server_default=sa.func.current_timestamp(),
            )
        )
        batch_op.create_index(
            batch_op.f('ix_individual_indexed'), ['indexed'], unique=False
        )

    with op.batch_alter_table('keyword', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'indexed',
                sa.DateTime(),
                nullable=False,
                server_default=sa.func.current_timestamp(),
            )
        )
        batch_op.create_index(batch_op.f('ix_keyword_indexed'), ['indexed'], unique=False)

    with op.batch_alter_table('mission', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'indexed',
                sa.DateTime(),
                nullable=False,
                server_default=sa.func.current_timestamp(),
            )
        )
        batch_op.create_index(batch_op.f('ix_mission_indexed'), ['indexed'], unique=False)

    with op.batch_alter_table('mission_task', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'indexed',
                sa.DateTime(),
                nullable=False,
                server_default=sa.func.current_timestamp(),
            )
        )
        batch_op.create_index(
            batch_op.f('ix_mission_task_indexed'), ['indexed'], unique=False
        )

    with op.batch_alter_table(
        'mission_task_annotation_participation', schema=None
    ) as batch_op:
        batch_op.add_column(
            sa.Column(
                'indexed',
                sa.DateTime(),
                nullable=False,
                server_default=sa.func.current_timestamp(),
            )
        )
        batch_op.create_index(
            batch_op.f('ix_mission_task_annotation_participation_indexed'),
            ['indexed'],
            unique=False,
        )

    with op.batch_alter_table(
        'mission_task_asset_participation', schema=None
    ) as batch_op:
        batch_op.add_column(
            sa.Column(
                'indexed',
                sa.DateTime(),
                nullable=False,
                server_default=sa.func.current_timestamp(),
            )
        )
        batch_op.create_index(
            batch_op.f('ix_mission_task_asset_participation_indexed'),
            ['indexed'],
            unique=False,
        )

    with op.batch_alter_table('mission_task_user_assignment', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'indexed',
                sa.DateTime(),
                nullable=False,
                server_default=sa.func.current_timestamp(),
            )
        )
        batch_op.create_index(
            batch_op.f('ix_mission_task_user_assignment_indexed'),
            ['indexed'],
            unique=False,
        )

    with op.batch_alter_table('mission_user_assignment', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'indexed',
                sa.DateTime(),
                nullable=False,
                server_default=sa.func.current_timestamp(),
            )
        )
        batch_op.create_index(
            batch_op.f('ix_mission_user_assignment_indexed'), ['indexed'], unique=False
        )

    with op.batch_alter_table('name', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'indexed',
                sa.DateTime(),
                nullable=False,
                server_default=sa.func.current_timestamp(),
            )
        )
        batch_op.create_index(batch_op.f('ix_name_indexed'), ['indexed'], unique=False)

    with op.batch_alter_table('name_preferring_users_join', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'indexed',
                sa.DateTime(),
                nullable=False,
                server_default=sa.func.current_timestamp(),
            )
        )
        batch_op.create_index(
            batch_op.f('ix_name_preferring_users_join_indexed'), ['indexed'], unique=False
        )

    with op.batch_alter_table('notification', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'indexed',
                sa.DateTime(),
                nullable=False,
                server_default=sa.func.current_timestamp(),
            )
        )
        batch_op.create_index(
            batch_op.f('ix_notification_indexed'), ['indexed'], unique=False
        )

    with op.batch_alter_table('organization', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'indexed',
                sa.DateTime(),
                nullable=False,
                server_default=sa.func.current_timestamp(),
            )
        )
        batch_op.create_index(
            batch_op.f('ix_organization_indexed'), ['indexed'], unique=False
        )

    with op.batch_alter_table(
        'organization_user_membership_enrollment', schema=None
    ) as batch_op:
        batch_op.add_column(
            sa.Column(
                'indexed',
                sa.DateTime(),
                nullable=False,
                server_default=sa.func.current_timestamp(),
            )
        )
        batch_op.create_index(
            batch_op.f('ix_organization_user_membership_enrollment_indexed'),
            ['indexed'],
            unique=False,
        )

    with op.batch_alter_table(
        'organization_user_moderator_enrollment', schema=None
    ) as batch_op:
        batch_op.add_column(
            sa.Column(
                'indexed',
                sa.DateTime(),
                nullable=False,
                server_default=sa.func.current_timestamp(),
            )
        )
        batch_op.create_index(
            batch_op.f('ix_organization_user_moderator_enrollment_indexed'),
            ['indexed'],
            unique=False,
        )

    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'indexed',
                sa.DateTime(),
                nullable=False,
                server_default=sa.func.current_timestamp(),
            )
        )
        batch_op.create_index(batch_op.f('ix_project_indexed'), ['indexed'], unique=False)

    with op.batch_alter_table('project_encounter', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'indexed',
                sa.DateTime(),
                nullable=False,
                server_default=sa.func.current_timestamp(),
            )
        )
        batch_op.create_index(
            batch_op.f('ix_project_encounter_indexed'), ['indexed'], unique=False
        )

    with op.batch_alter_table(
        'project_user_membership_enrollment', schema=None
    ) as batch_op:
        batch_op.add_column(
            sa.Column(
                'indexed',
                sa.DateTime(),
                nullable=False,
                server_default=sa.func.current_timestamp(),
            )
        )
        batch_op.create_index(
            batch_op.f('ix_project_user_membership_enrollment_indexed'),
            ['indexed'],
            unique=False,
        )

    with op.batch_alter_table('relationship', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'indexed',
                sa.DateTime(),
                nullable=False,
                server_default=sa.func.current_timestamp(),
            )
        )
        batch_op.create_index(
            batch_op.f('ix_relationship_indexed'), ['indexed'], unique=False
        )

    with op.batch_alter_table('relationship_individual_member', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'indexed',
                sa.DateTime(),
                nullable=False,
                server_default=sa.func.current_timestamp(),
            )
        )
        batch_op.create_index(
            batch_op.f('ix_relationship_individual_member_indexed'),
            ['indexed'],
            unique=False,
        )

    with op.batch_alter_table('sighting', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'indexed',
                sa.DateTime(),
                nullable=False,
                server_default=sa.func.current_timestamp(),
            )
        )
        batch_op.create_index(
            batch_op.f('ix_sighting_indexed'), ['indexed'], unique=False
        )

    with op.batch_alter_table('sighting_assets', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'indexed',
                sa.DateTime(),
                nullable=False,
                server_default=sa.func.current_timestamp(),
            )
        )
        batch_op.create_index(
            batch_op.f('ix_sighting_assets_indexed'), ['indexed'], unique=False
        )

    with op.batch_alter_table('site_setting', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'indexed',
                sa.DateTime(),
                nullable=False,
                server_default=sa.func.current_timestamp(),
            )
        )
        batch_op.create_index(
            batch_op.f('ix_site_setting_indexed'), ['indexed'], unique=False
        )

    with op.batch_alter_table('social_group', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'indexed',
                sa.DateTime(),
                nullable=False,
                server_default=sa.func.current_timestamp(),
            )
        )
        batch_op.create_index(
            batch_op.f('ix_social_group_indexed'), ['indexed'], unique=False
        )

    with op.batch_alter_table(
        'social_group_individual_membership', schema=None
    ) as batch_op:
        batch_op.add_column(
            sa.Column(
                'indexed',
                sa.DateTime(),
                nullable=False,
                server_default=sa.func.current_timestamp(),
            )
        )
        batch_op.create_index(
            batch_op.f('ix_social_group_individual_membership_indexed'),
            ['indexed'],
            unique=False,
        )

    with op.batch_alter_table('system_notification_preferences', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'indexed',
                sa.DateTime(),
                nullable=False,
                server_default=sa.func.current_timestamp(),
            )
        )
        batch_op.create_index(
            batch_op.f('ix_system_notification_preferences_indexed'),
            ['indexed'],
            unique=False,
        )

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'indexed',
                sa.DateTime(),
                nullable=False,
                server_default=sa.func.current_timestamp(),
            )
        )
        batch_op.create_index(batch_op.f('ix_user_indexed'), ['indexed'], unique=False)

    with op.batch_alter_table('user_notification_preferences', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'indexed',
                sa.DateTime(),
                nullable=False,
                server_default=sa.func.current_timestamp(),
            )
        )
        batch_op.create_index(
            batch_op.f('ix_user_notification_preferences_indexed'),
            ['indexed'],
            unique=False,
        )

    # ### end Alembic commands ###


def downgrade():
    """
    Downgrade Semantic Description:
        ENTER DESCRIPTION HERE
    """
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_notification_preferences', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_notification_preferences_indexed'))
        batch_op.drop_column('indexed')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_indexed'))
        batch_op.drop_column('indexed')

    with op.batch_alter_table('system_notification_preferences', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_system_notification_preferences_indexed'))
        batch_op.drop_column('indexed')

    with op.batch_alter_table(
        'social_group_individual_membership', schema=None
    ) as batch_op:
        batch_op.drop_index(batch_op.f('ix_social_group_individual_membership_indexed'))
        batch_op.drop_column('indexed')

    with op.batch_alter_table('social_group', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_social_group_indexed'))
        batch_op.drop_column('indexed')

    with op.batch_alter_table('site_setting', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_site_setting_indexed'))
        batch_op.drop_column('indexed')

    with op.batch_alter_table('sighting_assets', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_sighting_assets_indexed'))
        batch_op.drop_column('indexed')

    with op.batch_alter_table('sighting', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_sighting_indexed'))
        batch_op.drop_column('indexed')

    with op.batch_alter_table('relationship_individual_member', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_relationship_individual_member_indexed'))
        batch_op.drop_column('indexed')

    with op.batch_alter_table('relationship', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_relationship_indexed'))
        batch_op.drop_column('indexed')

    with op.batch_alter_table(
        'project_user_membership_enrollment', schema=None
    ) as batch_op:
        batch_op.drop_index(batch_op.f('ix_project_user_membership_enrollment_indexed'))
        batch_op.drop_column('indexed')

    with op.batch_alter_table('project_encounter', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_project_encounter_indexed'))
        batch_op.drop_column('indexed')

    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_project_indexed'))
        batch_op.drop_column('indexed')

    with op.batch_alter_table(
        'organization_user_moderator_enrollment', schema=None
    ) as batch_op:
        batch_op.drop_index(
            batch_op.f('ix_organization_user_moderator_enrollment_indexed')
        )
        batch_op.drop_column('indexed')

    with op.batch_alter_table(
        'organization_user_membership_enrollment', schema=None
    ) as batch_op:
        batch_op.drop_index(
            batch_op.f('ix_organization_user_membership_enrollment_indexed')
        )
        batch_op.drop_column('indexed')

    with op.batch_alter_table('organization', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_organization_indexed'))
        batch_op.drop_column('indexed')

    with op.batch_alter_table('notification', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_notification_indexed'))
        batch_op.drop_column('indexed')

    with op.batch_alter_table('name_preferring_users_join', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_name_preferring_users_join_indexed'))
        batch_op.drop_column('indexed')

    with op.batch_alter_table('name', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_name_indexed'))
        batch_op.drop_column('indexed')

    with op.batch_alter_table('mission_user_assignment', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_mission_user_assignment_indexed'))
        batch_op.drop_column('indexed')

    with op.batch_alter_table('mission_task_user_assignment', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_mission_task_user_assignment_indexed'))
        batch_op.drop_column('indexed')

    with op.batch_alter_table(
        'mission_task_asset_participation', schema=None
    ) as batch_op:
        batch_op.drop_index(batch_op.f('ix_mission_task_asset_participation_indexed'))
        batch_op.drop_column('indexed')

    with op.batch_alter_table(
        'mission_task_annotation_participation', schema=None
    ) as batch_op:
        batch_op.drop_index(
            batch_op.f('ix_mission_task_annotation_participation_indexed')
        )
        batch_op.drop_column('indexed')

    with op.batch_alter_table('mission_task', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_mission_task_indexed'))
        batch_op.drop_column('indexed')

    with op.batch_alter_table('mission', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_mission_indexed'))
        batch_op.drop_column('indexed')

    with op.batch_alter_table('keyword', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_keyword_indexed'))
        batch_op.drop_column('indexed')

    with op.batch_alter_table('individual', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_individual_indexed'))
        batch_op.drop_column('indexed')

    with op.batch_alter_table('houston_config', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_houston_config_indexed'))
        batch_op.drop_column('indexed')

    with op.batch_alter_table('git_store', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_git_store_indexed'))
        batch_op.drop_column('indexed')

    with op.batch_alter_table('file_upload', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_file_upload_indexed'))
        batch_op.drop_column('indexed')

    with op.batch_alter_table('encounter', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_encounter_indexed'))
        batch_op.drop_column('indexed')

    with op.batch_alter_table('email_record', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_email_record_indexed'))
        batch_op.drop_column('indexed')

    with op.batch_alter_table('collaboration_user_associations', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_collaboration_user_associations_indexed'))
        batch_op.drop_column('indexed')

    with op.batch_alter_table('collaboration', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_collaboration_indexed'))
        batch_op.drop_column('indexed')

    with op.batch_alter_table('code', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_code_indexed'))
        batch_op.drop_column('indexed')

    with op.batch_alter_table('audit_log', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_audit_log_indexed'))
        batch_op.drop_column('indexed')

    with op.batch_alter_table('asset_tags', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_asset_tags_indexed'))
        batch_op.drop_column('indexed')

    with op.batch_alter_table('asset_group_sighting', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_asset_group_sighting_indexed'))
        batch_op.drop_column('indexed')

    with op.batch_alter_table('asset', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_asset_indexed'))
        batch_op.drop_column('indexed')

    with op.batch_alter_table('annotation_keywords', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_annotation_keywords_indexed'))
        batch_op.drop_column('indexed')

    with op.batch_alter_table('annotation', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_annotation_indexed'))
        batch_op.drop_column('indexed')

    # ### end Alembic commands ###
