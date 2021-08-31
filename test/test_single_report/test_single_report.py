from test.base_test.baseTest import BaseGetGeneralTest
from test.config.configTest import ConfigTest

from app.messages.statusMessages import STATUS_200


class TestMiddleware(BaseGetGeneralTest):
    endpoint_get = "ThisEndpointShouldNotExist"
    expect_status_get = STATUS_200
    schema_general_get = None