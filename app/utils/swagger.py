from drf_yasg import openapi


USER_CREATION_BODY = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=["email", "password", "name"],
    properties={
        "name": openapi.Schema(
            type=openapi.TYPE_STRING,
        ),
        "email": openapi.Schema(type=openapi.TYPE_STRING),
        "password": openapi.Schema(type=openapi.TYPE_STRING),
    },
    additional_properties=False,
)

MOVEMENTS_GET_QUERY_PARAMS = [
    openapi.Parameter(
        name="type",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_STRING,
        required=False,
    ),
    openapi.Parameter(
        name="category",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_STRING,
        required=False,
    ),
    openapi.Parameter(
        name="is_recurrent",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_BOOLEAN,
        required=False,
    ),
]

MOVEMENTS_POST_BODY = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=["value", "name", "type", "category"],
    properties={
        "value": openapi.Schema(
            type=openapi.TYPE_NUMBER,
        ),
        "name": openapi.Schema(
            type=openapi.TYPE_STRING,
        ),
        "type": openapi.Schema(
            type=openapi.TYPE_STRING,
            enum=["INCOME", "EXPENSE"],
        ),
        "category": openapi.Schema(
            type=openapi.TYPE_STRING,
        ),
        "is_recurrent": openapi.Schema(
            type=openapi.TYPE_BOOLEAN,
        ),
    },
    additional_properties=False,
)
