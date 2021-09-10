from test.base_test.baseMultiGraphicOneDimension import \
    BaseMultiGraphicsOneDimension
from test.base_test.baseMultiGraphicTwoDimension import \
    BaseMultiGraphicsTwoDimension

from app.config.configEndpoint import EndpointConfig
from app.messages.statusMessages import STATUS_200


class TestSquareReportThreeGraphicsTwoDimension(BaseMultiGraphicsTwoDimension):
    Graphics = BaseMultiGraphicsTwoDimension.TypeGraphics[:3]
    endpoint_get = EndpointConfig.endpoint_square
    expect_status_get = STATUS_200


class TestSquareReportTwoGraphicsTwoDimension(BaseMultiGraphicsTwoDimension):
    Graphics = BaseMultiGraphicsTwoDimension.TypeGraphics[:2]
    endpoint_get = EndpointConfig.endpoint_square
    expect_status_get = STATUS_200


class TestSquareReportThreeGraphicsOneDimension(BaseMultiGraphicsOneDimension):
    Graphics = BaseMultiGraphicsOneDimension.TypeGraphics[:3]
    endpoint_get = EndpointConfig.endpoint_square
    expect_status_get = STATUS_200


class TestSquareReportTwoGraphicsOneDimension(BaseMultiGraphicsOneDimension):
    Graphics = BaseMultiGraphicsOneDimension.TypeGraphics[:2]
    endpoint_get = EndpointConfig.endpoint_square
    expect_status_get = STATUS_200


class TestSquareReportSixGraphicsMultiDimension(BaseMultiGraphicsTwoDimension):
    Graphics = BaseMultiGraphicsOneDimension.TypeGraphics[:3] + BaseMultiGraphicsTwoDimension.TypeGraphics[:3]
    endpoint_get = EndpointConfig.endpoint_square
    expect_status_get = STATUS_200
    save_file = True


class TestSquareReportFiveGraphicsMultiDimension(BaseMultiGraphicsTwoDimension):
    Graphics = BaseMultiGraphicsOneDimension.TypeGraphics[:2] + BaseMultiGraphicsTwoDimension.TypeGraphics[:3]
    endpoint_get = EndpointConfig.endpoint_square
    expect_status_get = STATUS_200


class TestSquareReportFourGraphicsMultiDimension(BaseMultiGraphicsTwoDimension):
    Graphics = BaseMultiGraphicsOneDimension.TypeGraphics[:2] + BaseMultiGraphicsTwoDimension.TypeGraphics[:2]
    endpoint_get = EndpointConfig.endpoint_square
    expect_status_get = STATUS_200
    save_file = True


class TestSquareReportThreeGraphicsMultiDimension(BaseMultiGraphicsTwoDimension):
    Graphics = BaseMultiGraphicsOneDimension.TypeGraphics[:1] + BaseMultiGraphicsTwoDimension.TypeGraphics[:2]
    endpoint_get = EndpointConfig.endpoint_square
    expect_status_get = STATUS_200


class TestSquareReportTwoGraphicsMultiDimension(BaseMultiGraphicsTwoDimension):
    Graphics = BaseMultiGraphicsOneDimension.TypeGraphics[:1] + BaseMultiGraphicsTwoDimension.TypeGraphics[:1]
    endpoint_get = EndpointConfig.endpoint_square
    expect_status_get = STATUS_200
