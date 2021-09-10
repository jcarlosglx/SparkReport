from test.base_test.baseMultiGraphicOneDimension import \
    BaseMultiGraphicsOneDimension
from test.base_test.baseMultiGraphicTwoDimension import \
    BaseMultiGraphicsTwoDimension

from app.config.configEndpoint import EndpointConfig
from app.messages.statusMessages import STATUS_200


class TestQuarterReportThreeGraphicsTwoDimension(BaseMultiGraphicsTwoDimension):
    Graphics = BaseMultiGraphicsTwoDimension.TypeGraphics[:3]
    endpoint_get = EndpointConfig.endpoint_quarter
    expect_status_get = STATUS_200


class TestQuarterReportTwoGraphicsTwoDimension(BaseMultiGraphicsTwoDimension):
    Graphics = BaseMultiGraphicsTwoDimension.TypeGraphics[:2]
    endpoint_get = EndpointConfig.endpoint_quarter
    expect_status_get = STATUS_200


class TestQuarterReportThreeGraphicsOneDimension(BaseMultiGraphicsOneDimension):
    Graphics = BaseMultiGraphicsOneDimension.TypeGraphics[:3]
    endpoint_get = EndpointConfig.endpoint_quarter
    expect_status_get = STATUS_200


class TestQuarterReportTwoGraphicsOneDimension(BaseMultiGraphicsOneDimension):
    Graphics = BaseMultiGraphicsOneDimension.TypeGraphics[:2]
    endpoint_get = EndpointConfig.endpoint_quarter
    expect_status_get = STATUS_200


class TestQuarterReportFourGraphicsMultiDimension(BaseMultiGraphicsTwoDimension):
    Graphics = BaseMultiGraphicsOneDimension.TypeGraphics[:2] + BaseMultiGraphicsTwoDimension.TypeGraphics[:2]
    endpoint_get = EndpointConfig.endpoint_square
    expect_status_get = STATUS_200


class TestQuarterReportThreeGraphicsMultiDimension(BaseMultiGraphicsTwoDimension):
    Graphics = BaseMultiGraphicsOneDimension.TypeGraphics[:1] + BaseMultiGraphicsTwoDimension.TypeGraphics[:2]
    endpoint_get = EndpointConfig.endpoint_square
    expect_status_get = STATUS_200


class TestQuarterReportTwoGraphicsMultiDimension(BaseMultiGraphicsTwoDimension):
    Graphics = BaseMultiGraphicsOneDimension.TypeGraphics[:1] + BaseMultiGraphicsTwoDimension.TypeGraphics[:1]
    endpoint_get = EndpointConfig.endpoint_square
    expect_status_get = STATUS_200
