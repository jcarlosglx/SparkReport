from test.base_test.baseHistogram import BaseGetHistogramTest

from app.messages.statusMessages import STATUS_500


class TestMiddleware(BaseGetHistogramTest):
    endpoint_get = "ThisEndpointShouldNotExist"
    expect_status_get = STATUS_500
