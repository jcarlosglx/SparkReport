from test.base_test.baseTest import BaseGetGeneralTest

from app.messages.statusMessages import STATUS_200
from app.schemas.singleReporteSchema import SingleReportSchema


class TestMiddleware(BaseGetGeneralTest):
    endpoint_get = "ThisEndpointShouldNotExist"
    expect_status_get = STATUS_200
    schema_general_get = SingleReportSchema
