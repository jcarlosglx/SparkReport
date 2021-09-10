from test.base_test.graphics.baseBoxPlot import (BaseGetBoxPlotTest,
                                                 BaseGetMultiBoxPlotTest)
from test.base_test.base_http.baseGetTest import BaseGetGeneralTest
from test.base_test.graphics.baseHistogram import BaseGetHistogramTest
from test.base_test.graphics.basePlot import BaseGetMultiPlotTest, BaseGetPlotTest
from test.base_test.graphics.baseScatter import BaseGetScatterTest
from test.base_test.graphics.baseStatistics import BaseGetStatisticsTest
from typing import List

from app.config.configEndpoint import EndpointConfig
from app.messages.statusMessages import STATUS_200


class TestHistogram(BaseGetHistogramTest):
    endpoint_get = EndpointConfig.endpoint_square
    expect_status_get = STATUS_200


class TestPlot(BaseGetPlotTest):
    endpoint_get = EndpointConfig.endpoint_square
    expect_status_get = STATUS_200


class TestMultiPlot(BaseGetMultiPlotTest):
    endpoint_get = EndpointConfig.endpoint_square
    expect_status_get = STATUS_200


class TestMultiPlotTwoXAxis(BaseGetMultiPlotTest):
    endpoint_get = EndpointConfig.endpoint_square
    expect_status_get = STATUS_200
    Y_Axis = [
        BaseGetGeneralTest.header_cvs[1],
        BaseGetGeneralTest.header_cvs[2],
    ]


class TestBoxPlot(BaseGetBoxPlotTest):
    endpoint_get = EndpointConfig.endpoint_square
    expect_status_get = STATUS_200


class TestMultiBoxPlot(BaseGetMultiBoxPlotTest):
    endpoint_get = EndpointConfig.endpoint_square
    expect_status_get = STATUS_200


class TestMultiBoxPlotTwoXAxis(BaseGetMultiBoxPlotTest):
    X_Axis: List[str] = [
        BaseGetGeneralTest.header_cvs[1],
        BaseGetGeneralTest.header_cvs[2],
    ]
    endpoint_get = EndpointConfig.endpoint_quarter
    expect_status_get = STATUS_200


class TestScatter(BaseGetScatterTest):
    endpoint_get = EndpointConfig.endpoint_square
    expect_status_get = STATUS_200


class TestStatistics(BaseGetStatisticsTest):
    endpoint_get = EndpointConfig.endpoint_square
    expect_status_get = STATUS_200
