from test.base_test.baseBoxPlot import (BaseGetBoxPlotTest,
                                        BaseGetMultiBoxPlotTest)
from test.base_test.baseHistogram import BaseGetHistogramTest
from test.base_test.basePlot import BaseGetMultiPlotTest, BaseGetPlotTest
from test.base_test.baseScatter import BaseGetScatterTest
from test.base_test.baseStatistics import BaseGetStatisticsTest

from app.config.configEndpoint import EndpointConfig
from app.messages.statusMessages import STATUS_200


class TestSquareReportHistogram(BaseGetHistogramTest):
    endpoint_get = EndpointConfig.endpoint_square
    expect_status_get = STATUS_200


class TestSquareReportPlot(BaseGetPlotTest):
    endpoint_get = EndpointConfig.endpoint_square
    expect_status_get = STATUS_200


class TestSquareReportMultiPlot(BaseGetMultiPlotTest):
    endpoint_get = EndpointConfig.endpoint_square
    expect_status_get = STATUS_200


class TestSquareReportBoxPlot(BaseGetBoxPlotTest):
    endpoint_get = EndpointConfig.endpoint_square
    expect_status_get = STATUS_200


class TestSquareReportMultiBoxPlot(BaseGetMultiBoxPlotTest):
    endpoint_get = EndpointConfig.endpoint_square
    expect_status_get = STATUS_200


class TestSquareReportScatter(BaseGetScatterTest):
    endpoint_get = EndpointConfig.endpoint_square
    expect_status_get = STATUS_200


class TestSquareReportStatistics(BaseGetStatisticsTest):
    endpoint_get = EndpointConfig.endpoint_square
    expect_status_get = STATUS_200
