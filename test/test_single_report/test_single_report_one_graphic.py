from test.base_test.baseBoxPlot import (BaseGetBoxPlotTest,
                                        BaseGetMultiBoxPlotTest)
from test.base_test.baseGetTest import BaseGetGeneralTest
from test.base_test.baseHistogram import BaseGetHistogramTest
from test.base_test.basePlot import BaseGetMultiPlotTest, BaseGetPlotTest
from test.base_test.baseScatter import BaseGetScatterTest
from test.base_test.baseStatistics import BaseGetStatisticsTest
from typing import List

from app.config.configEndpoint import EndpointConfig
from app.messages.statusMessages import STATUS_200


class TestSingleReportHistogram(BaseGetHistogramTest):
    endpoint_get = EndpointConfig.endpoint_single
    expect_status_get = STATUS_200


class TestSingleReportPlot(BaseGetPlotTest):
    endpoint_get = EndpointConfig.endpoint_single
    expect_status_get = STATUS_200


class TestSingleReportMultiPlot(BaseGetMultiPlotTest):
    endpoint_get = EndpointConfig.endpoint_single
    expect_status_get = STATUS_200


class TestSingleReportBoxPlot(BaseGetBoxPlotTest):
    endpoint_get = EndpointConfig.endpoint_single
    expect_status_get = STATUS_200


class TestSingleReportMultiBoxPlotTwoGraphic(BaseGetMultiBoxPlotTest):
    X_Axis: List[str] = [
        BaseGetGeneralTest.header_cvs[1],
        BaseGetGeneralTest.header_cvs[2],
    ]
    endpoint_get = EndpointConfig.endpoint_quarter
    expect_status_get = STATUS_200


class TestSingleReportMultiBoxPlot(BaseGetMultiBoxPlotTest):
    endpoint_get = EndpointConfig.endpoint_single
    expect_status_get = STATUS_200


class TestSingleReportScatter(BaseGetScatterTest):
    endpoint_get = EndpointConfig.endpoint_single
    expect_status_get = STATUS_200


class TestSingleReportStatistics(BaseGetStatisticsTest):
    endpoint_get = EndpointConfig.endpoint_single
    expect_status_get = STATUS_200
