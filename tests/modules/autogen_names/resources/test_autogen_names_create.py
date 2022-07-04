# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring

import pytest

import tests.modules.autogen_names.resources.utils as auto_name_utils
from tests.utils import module_unavailable


@pytest.mark.skipif(
    module_unavailable('autogenerated_names'),
    reason='Autogenerated names module disabled',
)
def test_create_autogenerated_name(
    flask_app_client,
    researcher_1,
    admin_user,
    researcher_2,
    user_manager_user,
    db,
    request,
    test_root,
):

    import uuid

    import tests.modules.individuals.resources.utils as individual_utils

    individual1_uuids = individual_utils.create_individual_and_sighting(
        flask_app_client,
        researcher_1,
        request,
        test_root,
    )
    individual1_id = individual1_uuids['individual']
    individual1_data = individual_utils.read_individual(  # NOQA
        flask_app_client, researcher_1, individual1_id
    ).json
    auto_name_utils.read_all_autogen_names(flask_app_client, admin_user)
    auto_name_utils.read_all_autogen_names(flask_app_client, researcher_1)
    data = {str(uuid.uuid4()): {'prefix': 'woo', 'type': 'auto_species'}}
    auto_name_utils.create_autogen_name(flask_app_client, admin_user, data)

    # create another one the same, should fail
    new_data = {str(uuid.uuid4()): {'prefix': 'woo', 'type': 'auto_species'}}
    error = (
        'Cannot create an additional autogenerated name for type:auto_species, prefix:woo'
    )
    auto_name_utils.create_autogen_name(
        flask_app_client, admin_user, new_data, 400, error
    )

    names = auto_name_utils.read_all_autogen_names(flask_app_client, admin_user)
    spec_woos = [
        names[name_guid]
        for name_guid in names
        if names[name_guid]['type'] == 'auto_species'
        and names[name_guid]['prefix'] == 'woo'
    ]
    assert len(spec_woos) == 1
    name = spec_woos[0]
    assert name['type'] == 'auto_species'
    assert name['prefix'] == 'woo'

    individual2_uuids = individual_utils.create_individual_and_sighting(
        flask_app_client,
        researcher_1,
        request,
        test_root,
    )
    individual2_id = individual2_uuids['individual']  # NOQA
    individual2_data = individual_utils.read_individual(  # NOQA
        flask_app_client, researcher_1, individual1_id
    ).json
