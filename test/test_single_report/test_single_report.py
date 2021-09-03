from test.base_test.baseTest import BaseGetGeneralTest
from app.config.configEndpoint import EndpointConfig
from app.messages.statusMessages import STATUS_200
from app.schemas.singleReporteSchema import SingleReportSchema


class TestSingleReport(BaseGetGeneralTest):
    endpoint_get = EndpointConfig.endpoint_single
    expect_status_get = STATUS_200
    schema_general_get = SingleReportSchema
