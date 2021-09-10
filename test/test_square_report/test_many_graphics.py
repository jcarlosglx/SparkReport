from test.base_test.base_dimension.baseMultiGraphicMixDimension import \
    BaseMultiGraphicsMixDimension
from test.base_test.base_dimension.baseMultiGraphicOneDimension import \
    BaseMultiGraphicsOneDimension
from test.base_test.base_dimension.baseMultiGraphicTwoDimension import \
    BaseMultiGraphicsTwoDimension

from app.config.configEndpoint import EndpointConfig
from app.messages.statusMessages import STATUS_200


class TestThreeGraphicsTwoDimension(BaseMultiGraphicsTwoDimension):
    Graphics = BaseMultiGraphicsTwoDimension.TypeGraphics[:3]
    endpoint_get = EndpointConfig.endpoint_square
    expect_status_get = STATUS_200


class TestTwoGraphicsTwoDimension(BaseMultiGraphicsTwoDimension):
    Graphics = BaseMultiGraphicsTwoDimension.TypeGraphics[:2]
    endpoint_get = EndpointConfig.endpoint_square
    expect_status_get = STATUS_200


class TestThreeGraphicsOneDimension(BaseMultiGraphicsOneDimension):
    Graphics = BaseMultiGraphicsOneDimension.TypeGraphics[:3]
    endpoint_get = EndpointConfig.endpoint_square
    expect_status_get = STATUS_200


class TestTwoGraphicsOneDimension(BaseMultiGraphicsOneDimension):
    Graphics = BaseMultiGraphicsOneDimension.TypeGraphics[:2]
    endpoint_get = EndpointConfig.endpoint_square
    expect_status_get = STATUS_200


class TestSixGraphicsMixDimension(BaseMultiGraphicsMixDimension):
    Graphics = (
        BaseMultiGraphicsOneDimension.TypeGraphics[:3]
        + BaseMultiGraphicsTwoDimension.TypeGraphics[:3]
    )
    endpoint_get = EndpointConfig.endpoint_square
    expect_status_get = STATUS_200


class TestFiveGraphicsMixDimension(BaseMultiGraphicsMixDimension):
    Graphics = (
        BaseMultiGraphicsOneDimension.TypeGraphics[:2]
        + BaseMultiGraphicsTwoDimension.TypeGraphics[:3]
    )
    endpoint_get = EndpointConfig.endpoint_square
    expect_status_get = STATUS_200


class TestFourGraphicsMixDimension(BaseMultiGraphicsMixDimension):
    Graphics = (
        BaseMultiGraphicsOneDimension.TypeGraphics[:2]
        + BaseMultiGraphicsTwoDimension.TypeGraphics[:2]
    )
    endpoint_get = EndpointConfig.endpoint_square
    expect_status_get = STATUS_200


class TestThreeGraphicsMixDimension(BaseMultiGraphicsMixDimension):
    Graphics = (
        BaseMultiGraphicsOneDimension.TypeGraphics[:1]
        + BaseMultiGraphicsTwoDimension.TypeGraphics[:2]
    )
    endpoint_get = EndpointConfig.endpoint_square
    expect_status_get = STATUS_200


class TestTwoGraphicsMixDimension(BaseMultiGraphicsMixDimension):
    Graphics = (
        BaseMultiGraphicsOneDimension.TypeGraphics[:1]
        + BaseMultiGraphicsTwoDimension.TypeGraphics[:1]
    )
    endpoint_get = EndpointConfig.endpoint_square
    expect_status_get = STATUS_200
