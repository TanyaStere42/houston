# -*- coding: utf-8 -*-
"""
Serialization schemas for Encounters resources RESTful API
----------------------------------------------------
"""

# from flask_marshmallow import base_fields
from flask_restx_patched import ModelSchema

from .models import Encounter


class BaseEncounterSchema(ModelSchema):
    """
    Base Encounter schema exposes only the most general fields.
    """

    class Meta:
        # pylint: disable=missing-docstring
        model = Encounter
        fields = (Encounter.guid.key,)
        dump_only = (Encounter.guid.key,)


class DetailedEncounterSchema(BaseEncounterSchema):
    """
    Detailed Encounter schema exposes all useful fields.
    """

    class Meta(BaseEncounterSchema.Meta):
        fields = BaseEncounterSchema.Meta.fields + (
            Encounter.created.key,
            Encounter.updated.key,
        )
        dump_only = BaseEncounterSchema.Meta.dump_only + (
            Encounter.created.key,
            Encounter.updated.key,
        )
