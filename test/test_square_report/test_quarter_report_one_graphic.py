from test.base_test.baseBoxPlot import (BaseGetBoxPlotTest,
                                        BaseGetMultiBoxPlotTest)
from test.base_test.baseHistogram import BaseGetHistogramTest
from test.base_test.basePlot import BaseGetMultiPlotTest, BaseGetPlotTest
from test.base_test.baseScatter import BaseGetScatterTest
from test.base_test.baseStatistics import BaseGetStatisticsTest

from app.config.configEndpoint import EndpointConfig
from app.messages.statusMessages import STATUS_200


class TestQuarterReportHistogram(BaseGetHistogramTest):
    endpoint_get = EndpointConfig.endpoint_quarter
    expect_status_get = STATUS_200


class TestQuarterReportPlot(BaseGetPlotTest):
    endpoint_get = EndpointConfig.endpoint_quarter
    expect_status_get = STATUS_200


class TestQuarterReportMultiPlot(BaseGetMultiPlotTest):
    endpoint_get = EndpointConfig.endpoint_quarter
    expect_status_get = STATUS_200


class TestQuarterReportBoxPlot(BaseGetBoxPlotTest):
    endpoint_get = EndpointConfig.endpoint_quarter
    expect_status_get = STATUS_200


class TestQuarterReportMultiBoxPlot(BaseGetMultiBoxPlotTest):
    endpoint_get = EndpointConfig.endpoint_quarter
    expect_status_get = STATUS_200


class TestQuarterReportScatter(BaseGetScatterTest):
    endpoint_get = EndpointConfig.endpoint_quarter
    expect_status_get = STATUS_200


class TestQuarterReportStatistics(BaseGetStatisticsTest):
    endpoint_get = EndpointConfig.endpoint_quarter
    expect_status_get = STATUS_200
