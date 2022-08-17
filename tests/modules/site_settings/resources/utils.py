# -*- coding: utf-8 -*-
"""
Configuration resources utils
-------------
"""
import uuid

from tests import utils as test_utils

EXPECTED_KEYS = {
    'preferred_language',
    'email_service',
    'site.general.description',
    'email_service_username',
    'site.links.facebookLink',
    'site.general.helpDescription',
    'email_default_sender_email',
    'autogenerated_names',
    'site.images',
    'email_adoption_button_text',
    'transloaditService',
    'site.general.tagline',
    'sentryDsn',
    'site.general.customCardLine2',
    'site.species',
    'email_header_image_url',
    'site.general.customCardButtonText',
    'flatfileKey',
    'recaptchaSecretKey',
    'site.custom.regions',
    'site.adminUserInitialized',
    'system_guid',
    'logo',
    'site.general.customCardButtonUrl',
    'site.custom.customFields.Sighting',
    'email_default_sender_name',
    'site.links.instagramLink',
    'email_service_password',
    'email_legal_statement',
    'social_group_roles',
    'transloaditTemplateId',
    'googleMapsApiKey',
    'site.custom.customFields.Encounter',
    'site.general.photoGuidelinesUrl',
    'splashVideo',
    'site.custom.customFieldCategories',
    'customCardImage',
    'email_title_greeting',
    'email_secondary_text',
    'site.general.customCardLine1',
    'site.general.taglineSubtitle',
    'relationship_type_roles',
    'site.general.donationButtonUrl',
    'site.private',
    'site.look.logoIncludesSiteName',
    'site.look.themeColor',
    'site.links.twitterLink',
    'email_secondary_title',
    'recaptchaPublicKey',
    'transloaditKey',
    'site.name',
    'site.needsSetup',
    'splashImage',
    'site.custom.customFields.Individual',
}
EXPECTED_SINGLE_KEY = {'value'}
SETTING_PATH = '/api/v1/site-settings'


def _read_settings(
    flask_app_client,
    user,
    conf_path,
    expected_status_code=None,
    response_200=EXPECTED_KEYS,
):
    res = test_utils.get_dict_via_flask(
        flask_app_client,
        user,
        scopes='site-settings:read',
        path=conf_path,
        expected_status_code=expected_status_code,
        response_200=response_200,
        response_error={'message'},
    )
    return res


def read_main_settings(
    flask_app_client,
    user,
    conf_path=None,
    expected_status_code=200,
):
    if conf_path:
        path = f'{SETTING_PATH}/data/{conf_path}'
        response_200 = EXPECTED_SINGLE_KEY
    else:
        path = f'{SETTING_PATH}/data/'
        response_200 = EXPECTED_KEYS

    return _read_settings(
        flask_app_client, user, path, expected_status_code, response_200
    )


def read_main_settings_definition(
    flask_app_client,
    user,
    conf_path='block',
    expected_status_code=200,
):
    path = f'{SETTING_PATH}/definition/main/{conf_path}'
    return _read_settings(
        flask_app_client, user, path, expected_status_code, response_200={'response'}
    )


def read_file(flask_app_client, user, filename, expected_status_code=302):
    path = f'{SETTING_PATH}/file/{filename}'

    # Files are special in that they have no json response so cannot be validated by the normal utils
    resp = _read_settings(flask_app_client, user, path)
    assert resp.status_code == expected_status_code

    return resp


def _modify_setting(
    flask_app_client,
    user,
    data,
    conf_path,
    expected_status_code=None,
    expected_error=None,
):
    return test_utils.post_via_flask(
        flask_app_client,
        user,
        scopes='site-settings:write',
        path=conf_path,
        data=data,
        expected_status_code=expected_status_code,
        response_200=None,
        expected_error=expected_error,
    )


def modify_main_settings(
    flask_app_client,
    user,
    data,
    conf_key=None,
    expected_status_code=200,
    expected_error=None,
):
    if conf_key:
        data_sent = {'value': data}
        path = f'{SETTING_PATH}/data/{conf_key}'
    else:
        path = f'{SETTING_PATH}/data/'
        data_sent = data
    return _modify_setting(
        flask_app_client, user, data_sent, path, expected_status_code, expected_error
    )


def write_file(flask_app_client, user, data, expected_status_code=200):
    path = f'{SETTING_PATH}/file'
    return _modify_setting(
        flask_app_client, user, data, path, expected_status_code, {'file_upload_guid'}
    )


def _get_default_custom_field_categories(flask_app_client, user, cls):
    cat_name = 'site.custom.customFieldCategories'
    categories = read_main_settings(flask_app_client, user, cat_name).json['value']
    type = None
    label = None
    if cls == 'Sighting' or cls == 'Occurrence':
        type = 'sighting'
        label = 'distance'
    elif cls == 'Encounter':
        type = 'encounter'
        label = 'distance'
    elif cls == 'Individual' or cls == 'MarkedIndividual':
        type = 'individual'
        label = 'grumpiness'

    for cat in categories:
        if cat['type'] == type and cat['label'] == label:
            break
    else:
        categories.append({'id': str(uuid.uuid4()), 'label': label, 'type': type})
        modify_main_settings(flask_app_client, user, categories, cat_name)
        categories = read_main_settings(flask_app_client, user, cat_name).json['value']

    class_cats = [cat for cat in categories if cat['type'] == type]
    return class_cats


# note: this returns the *id of the CustomFieldDefinition*
def custom_field_create(
    flask_app_client,
    user,
    name,
    cls='Sighting',
    displayType='string',
    multiple=False,
    required=False,
    schema_mods=None,  # will overwrite default (in a good way)
    expected_status_code=200,
    expected_error=None,
):
    fieldname = 'site.custom.customFields.' + cls
    custom_fields = read_main_settings(flask_app_client, user, fieldname).json['value']
    if 'definitions' not in custom_fields:
        custom_fields['definitions'] = []
    for cust in custom_fields['definitions']:
        if cust['name'] == name:
            return cust['id']

    categories = _get_default_custom_field_categories(flask_app_client, user, cls)
    assert len(categories) >= 1
    cat = categories[0]

    # default schema
    schema = {
        'category': cat['id'],
        'description': 'some random text',
        'displayType': displayType,
        'label': 'stuff',
    }
    if isinstance(schema_mods, dict):
        for mod in schema_mods:
            schema[mod] = schema_mods[mod]

    if 'definitions' not in custom_fields:
        custom_fields['definitions'] = []
    cfd_id = str(uuid.uuid4())
    custom_fields['definitions'].append(
        {
            'id': cfd_id,
            'required': required,
            'name': name,
            'multiple': multiple,
            'schema': schema,
        }
    )

    payload = {}
    payload[fieldname] = custom_fields
    resp = modify_main_settings(
        flask_app_client, user, payload, expected_status_code=expected_status_code
    )
    if expected_status_code != 200:
        return resp
    custom_fields = read_main_settings(flask_app_client, user, fieldname).json['value']
    cfd_list = custom_fields.get('definitions', None)

    assert cfd_list
    return cfd_id


def patch_main_setting(
    flask_app_client,
    user,
    data,
    conf_key=None,
    expected_status_code=200,
):
    path = f'{SETTING_PATH}/data/{conf_key}' if conf_key else f'{SETTING_PATH}/data/'
    return test_utils.patch_via_flask(
        flask_app_client,
        user,
        scopes='site-settings:write',
        path=path,
        data=data,
        expected_status_code=expected_status_code,
        response_200=set({}),
    )


def _delete_setting(
    flask_app_client,
    user,
    conf_path,
    expected_status_code=200,
):
    res = test_utils.delete_via_flask(
        flask_app_client,
        user,
        scopes='site-settings:write',
        path=conf_path,
        expected_status_code=expected_status_code,
    )

    return res


def delete_main_setting(
    flask_app_client,
    user,
    conf_key,
    expected_status_code=204,
):
    if conf_key == 'block':
        path = f'{SETTING_PATH}/data'
    else:
        path = f'{SETTING_PATH}/data/{conf_key}'
    return _delete_setting(flask_app_client, user, path, expected_status_code)


def delete_file(
    flask_app_client,
    user,
    conf_key,
    expected_status_code=204,
):
    path = f'{SETTING_PATH}/file/{conf_key}'
    _delete_setting(flask_app_client, user, path, expected_status_code)


def extract_from_main_block(main_block, field):
    if field in main_block and 'value' in main_block[field]:
        return main_block[field]['value']
    return None


# will create one if we dont have any (yet)
def get_some_taxonomy_dict(flask_app_client, admin_user):
    block_data = read_main_settings(flask_app_client, admin_user).json
    species = extract_from_main_block(block_data, 'site.species')

    if species and isinstance(species, list) and len(species) > 0:
        return species[0]

    # need to make one
    vals = [
        {'commonNames': ['Example'], 'scientificName': 'Exempli gratia', 'itisTsn': -1234}
    ]
    modify_main_settings(
        flask_app_client,
        admin_user,
        vals,
        'site.species',
    )
    response = read_main_settings(flask_app_client, admin_user).json
    species = extract_from_main_block(response, 'site.species')
    assert species
    assert isinstance(species, list)
    assert len(species) > 0
    return species[0]


# Helper util to get (and create if necessary) the regions we will use for testing
def get_and_ensure_test_regions(flask_app_client, admin_user):
    block_data = read_main_settings(flask_app_client, admin_user).json
    current_regions = extract_from_main_block(block_data, 'site.custom.regions')

    names = []
    regions = []
    if 'locationID' in current_regions:
        regions = current_regions['locationID']
        names = [region['name'] for region in regions]

    updated = False
    if 'Wiltshire' not in names:
        regions.append({'id': str(uuid.uuid4()), 'name': 'Wiltshire'})
        updated = True
    if 'Mongolia' not in names:
        regions.append({'id': str(uuid.uuid4()), 'name': 'Mongolia'})
        updated = True
    if 'France' not in names:
        regions.append({'id': str(uuid.uuid4()), 'name': 'France'})
        updated = True
    if updated:
        modify_main_settings(
            flask_app_client,
            admin_user,
            {'locationID': regions},
            'site.custom.regions',
        )

    return regions
