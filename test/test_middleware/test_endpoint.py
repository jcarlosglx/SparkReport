# from test.base_test.baseTest import BaseGetGeneralTest, BasePutTest
# from test.config.configTest import ConfigTest
#
# from app.messages.statusMessages import STATUS_405, STATUS_500
#
#
# class TestMiddleware(BasePutTest, BaseGetGeneralTest):
#     endpoint_put = ConfigTest.endpoint_logs
#     endpoint_get = "ThisEndpointShouldNotExist"
#     expect_status_get = STATUS_500
#     expect_status_put = STATUS_405
