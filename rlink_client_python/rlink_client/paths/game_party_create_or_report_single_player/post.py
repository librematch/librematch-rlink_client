# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from urllib3._collections import HTTPHeaderDict

from rlink_client import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from rlink_client import schemas  # noqa: F401

from . import path

# Query params
AppbincrcSchema = schemas.IntSchema
CallNumSchema = schemas.IntSchema
CountersZipSchema = schemas.StrSchema
CreateMatchKeySchema = schemas.IntSchema
DatacrcSchema = schemas.IntSchema
IsCompleteSchema = schemas.IntSchema
ItemUpdatesSchema = schemas.IntSchema
LastCallTimeSchema = schemas.StrSchema
MapnameSchema = schemas.StrSchema
MatchKeySchema = schemas.StrSchema
MatchTypeIDSchema = schemas.IntSchema
ModDLLChecksumSchema = schemas.IntSchema
ModDLLFileSchema = schemas.StrSchema
ModNameSchema = schemas.StrSchema
ModVersionSchema = schemas.StrSchema
OptionsSchema = schemas.StrSchema
RaceIdsSchema = schemas.IntSchema
ResultsSchema = schemas.IntSchema
SlotInfoSchema = schemas.StrSchema
TeamIDsSchema = schemas.IntSchema
VersionFlagsSchema = schemas.IntSchema
XpGainedSchema = schemas.IntSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    "RequestRequiredQueryParams",
    {
        "appbincrc": typing.Union[
            AppbincrcSchema,
            decimal.Decimal,
            int,
        ],
        "callNum": typing.Union[
            CallNumSchema,
            decimal.Decimal,
            int,
        ],
        "countersZip": typing.Union[
            CountersZipSchema,
            str,
        ],
        "createMatchKey": typing.Union[
            CreateMatchKeySchema,
            decimal.Decimal,
            int,
        ],
        "datacrc": typing.Union[
            DatacrcSchema,
            decimal.Decimal,
            int,
        ],
        "isComplete": typing.Union[
            IsCompleteSchema,
            decimal.Decimal,
            int,
        ],
        "itemUpdates": typing.Union[
            ItemUpdatesSchema,
            decimal.Decimal,
            int,
        ],
        "lastCallTime": typing.Union[
            LastCallTimeSchema,
            str,
        ],
        "mapname": typing.Union[
            MapnameSchema,
            str,
        ],
        "matchKey": typing.Union[
            MatchKeySchema,
            str,
        ],
        "matchTypeID": typing.Union[
            MatchTypeIDSchema,
            decimal.Decimal,
            int,
        ],
        "modDLLChecksum": typing.Union[
            ModDLLChecksumSchema,
            decimal.Decimal,
            int,
        ],
        "modDLLFile": typing.Union[
            ModDLLFileSchema,
            str,
        ],
        "modName": typing.Union[
            ModNameSchema,
            str,
        ],
        "modVersion": typing.Union[
            ModVersionSchema,
            str,
        ],
        "options": typing.Union[
            OptionsSchema,
            str,
        ],
        "race_ids": typing.Union[
            RaceIdsSchema,
            decimal.Decimal,
            int,
        ],
        "results": typing.Union[
            ResultsSchema,
            decimal.Decimal,
            int,
        ],
        "slotInfo": typing.Union[
            SlotInfoSchema,
            str,
        ],
        "teamIDs": typing.Union[
            TeamIDsSchema,
            decimal.Decimal,
            int,
        ],
        "versionFlags": typing.Union[
            VersionFlagsSchema,
            decimal.Decimal,
            int,
        ],
        "xpGained": typing.Union[
            XpGainedSchema,
            decimal.Decimal,
            int,
        ],
    },
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    "RequestOptionalQueryParams", {}, total=False
)


class RequestQueryParams(
    RequestRequiredQueryParams, RequestOptionalQueryParams
):
    pass


request_query_appbincrc = api_client.QueryParameter(
    name="appbincrc",
    style=api_client.ParameterStyle.FORM,
    schema=AppbincrcSchema,
    required=True,
    explode=True,
)
request_query_call_num = api_client.QueryParameter(
    name="callNum",
    style=api_client.ParameterStyle.FORM,
    schema=CallNumSchema,
    required=True,
    explode=True,
)
request_query_counters_zip = api_client.QueryParameter(
    name="countersZip",
    style=api_client.ParameterStyle.FORM,
    schema=CountersZipSchema,
    required=True,
    explode=True,
)
request_query_create_match_key = api_client.QueryParameter(
    name="createMatchKey",
    style=api_client.ParameterStyle.FORM,
    schema=CreateMatchKeySchema,
    required=True,
    explode=True,
)
request_query_datacrc = api_client.QueryParameter(
    name="datacrc",
    style=api_client.ParameterStyle.FORM,
    schema=DatacrcSchema,
    required=True,
    explode=True,
)
request_query_is_complete = api_client.QueryParameter(
    name="isComplete",
    style=api_client.ParameterStyle.FORM,
    schema=IsCompleteSchema,
    required=True,
    explode=True,
)
request_query_item_updates = api_client.QueryParameter(
    name="itemUpdates",
    style=api_client.ParameterStyle.FORM,
    schema=ItemUpdatesSchema,
    required=True,
    explode=True,
)
request_query_last_call_time = api_client.QueryParameter(
    name="lastCallTime",
    style=api_client.ParameterStyle.FORM,
    schema=LastCallTimeSchema,
    required=True,
    explode=True,
)
request_query_mapname = api_client.QueryParameter(
    name="mapname",
    style=api_client.ParameterStyle.FORM,
    schema=MapnameSchema,
    required=True,
    explode=True,
)
request_query_match_key = api_client.QueryParameter(
    name="matchKey",
    style=api_client.ParameterStyle.FORM,
    schema=MatchKeySchema,
    required=True,
    explode=True,
)
request_query_match_type_id = api_client.QueryParameter(
    name="matchTypeID",
    style=api_client.ParameterStyle.FORM,
    schema=MatchTypeIDSchema,
    required=True,
    explode=True,
)
request_query_mod_dll_checksum = api_client.QueryParameter(
    name="modDLLChecksum",
    style=api_client.ParameterStyle.FORM,
    schema=ModDLLChecksumSchema,
    required=True,
    explode=True,
)
request_query_mod_dll_file = api_client.QueryParameter(
    name="modDLLFile",
    style=api_client.ParameterStyle.FORM,
    schema=ModDLLFileSchema,
    required=True,
    explode=True,
)
request_query_mod_name = api_client.QueryParameter(
    name="modName",
    style=api_client.ParameterStyle.FORM,
    schema=ModNameSchema,
    required=True,
    explode=True,
)
request_query_mod_version = api_client.QueryParameter(
    name="modVersion",
    style=api_client.ParameterStyle.FORM,
    schema=ModVersionSchema,
    required=True,
    explode=True,
)
request_query_options = api_client.QueryParameter(
    name="options",
    style=api_client.ParameterStyle.FORM,
    schema=OptionsSchema,
    required=True,
    explode=True,
)
request_query_race_ids = api_client.QueryParameter(
    name="race_ids",
    style=api_client.ParameterStyle.FORM,
    schema=RaceIdsSchema,
    required=True,
    explode=True,
)
request_query_results = api_client.QueryParameter(
    name="results",
    style=api_client.ParameterStyle.FORM,
    schema=ResultsSchema,
    required=True,
    explode=True,
)
request_query_slot_info = api_client.QueryParameter(
    name="slotInfo",
    style=api_client.ParameterStyle.FORM,
    schema=SlotInfoSchema,
    required=True,
    explode=True,
)
request_query_team_ids = api_client.QueryParameter(
    name="teamIDs",
    style=api_client.ParameterStyle.FORM,
    schema=TeamIDsSchema,
    required=True,
    explode=True,
)
request_query_version_flags = api_client.QueryParameter(
    name="versionFlags",
    style=api_client.ParameterStyle.FORM,
    schema=VersionFlagsSchema,
    required=True,
    explode=True,
)
request_query_xp_gained = api_client.QueryParameter(
    name="xpGained",
    style=api_client.ParameterStyle.FORM,
    schema=XpGainedSchema,
    required=True,
    explode=True,
)
_auth = [
    "sessionID",
    "connectID",
]
SchemaFor200ResponseBodyApplicationJson = schemas.AnyTypeSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[SchemaFor200ResponseBodyApplicationJson,]
    headers: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        "application/json": api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson
        ),
    },
)
_status_code_to_response = {
    "200": _response_for_200,
}
_all_accept_content_types = ("application/json",)


class BaseApi(api_client.Api):
    @typing.overload
    def _game_party_create_or_report_single_player_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[ApiResponseFor200,]:
        ...

    @typing.overload
    def _game_party_create_or_report_single_player_oapg(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization:
        ...

    @typing.overload
    def _game_party_create_or_report_single_player_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        ...

    def _game_party_create_or_report_single_player_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value

        prefix_separator_iterator = None
        for parameter in (
            request_query_appbincrc,
            request_query_call_num,
            request_query_counters_zip,
            request_query_create_match_key,
            request_query_datacrc,
            request_query_is_complete,
            request_query_item_updates,
            request_query_last_call_time,
            request_query_mapname,
            request_query_match_key,
            request_query_match_type_id,
            request_query_mod_dll_checksum,
            request_query_mod_dll_file,
            request_query_mod_name,
            request_query_mod_version,
            request_query_options,
            request_query_race_ids,
            request_query_results,
            request_query_slot_info,
            request_query_team_ids,
            request_query_version_flags,
            request_query_xp_gained,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = (
                    parameter.get_prefix_separator_iterator()
                )
            serialized_data = parameter.serialize(
                parameter_data, prefix_separator_iterator
            )
            for serialized_value in serialized_data.values():
                used_path += serialized_value

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add("Accept", accept_content_type)

        response = self.api_client.call_api(
            resource_path=used_path,
            method="post".upper(),
            headers=_headers,
            auth_settings=_auth,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(
                response=response
            )
        else:
            response_for_status = _status_code_to_response.get(
                str(response.status)
            )
            if response_for_status:
                api_response = response_for_status.deserialize(
                    response, self.api_client.configuration
                )
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(
                    response=response
                )

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(
                status=response.status,
                reason=response.reason,
                api_response=api_response,
            )

        return api_response


class GamePartyCreateOrReportSinglePlayer(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def game_party_create_or_report_single_player(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[ApiResponseFor200,]:
        ...

    @typing.overload
    def game_party_create_or_report_single_player(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization:
        ...

    @typing.overload
    def game_party_create_or_report_single_player(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        ...

    def game_party_create_or_report_single_player(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._game_party_create_or_report_single_player_oapg(
            query_params=query_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization,
        )


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def post(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[ApiResponseFor200,]:
        ...

    @typing.overload
    def post(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization:
        ...

    @typing.overload
    def post(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        ...

    def post(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._game_party_create_or_report_single_player_oapg(
            query_params=query_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization,
        )
