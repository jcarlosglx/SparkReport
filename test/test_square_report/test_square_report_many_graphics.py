from test.base_test.baseMultiGraphicMixDimension import \
    BaseMultiGraphicsMixDimension
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


class TestSquareReportSixGraphicsMixDimension(BaseMultiGraphicsMixDimension):
    Graphics = (
        BaseMultiGraphicsOneDimension.TypeGraphics[:3]
        + BaseMultiGraphicsTwoDimension.TypeGraphics[:3]
    )
    endpoint_get = EndpointConfig.endpoint_square
    expect_status_get = STATUS_200


class TestSquareReportFiveGraphicsMixDimension(BaseMultiGraphicsMixDimension):
    Graphics = (
        BaseMultiGraphicsOneDimension.TypeGraphics[:2]
        + BaseMultiGraphicsTwoDimension.TypeGraphics[:3]
    )
    endpoint_get = EndpointConfig.endpoint_square
    expect_status_get = STATUS_200


class TestSquareReportFourGraphicsMixDimension(BaseMultiGraphicsMixDimension):
    Graphics = (
        BaseMultiGraphicsOneDimension.TypeGraphics[:2]
        + BaseMultiGraphicsTwoDimension.TypeGraphics[:2]
    )
    endpoint_get = EndpointConfig.endpoint_square
    expect_status_get = STATUS_200


class TestSquareReportThreeGraphicsMixDimension(BaseMultiGraphicsMixDimension):
    Graphics = (
        BaseMultiGraphicsOneDimension.TypeGraphics[:1]
        + BaseMultiGraphicsTwoDimension.TypeGraphics[:2]
    )
    endpoint_get = EndpointConfig.endpoint_square
    expect_status_get = STATUS_200


class TestSquareReportTwoGraphicsMixDimension(BaseMultiGraphicsMixDimension):
    Graphics = (
        BaseMultiGraphicsOneDimension.TypeGraphics[:1]
        + BaseMultiGraphicsTwoDimension.TypeGraphics[:1]
    )
    endpoint_get = EndpointConfig.endpoint_square
    expect_status_get = STATUS_200
