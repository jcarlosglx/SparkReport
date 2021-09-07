from test.base_test.basePlot import BaseGetPlotTest, BaseGetMultiPlotTest
from test.base_test.baseBoxPlot import BaseGetBoxPlotTest, BaseGetMultiBoxPlotTest
from test.base_test.baseHistogram import BaseGetHistogramTest
from test.base_test.baseStatistics import BaseGetStatisticsTest
from test.base_test.baseScatter import BaseGetScatterTest

from app.config.configEndpoint import EndpointConfig
from app.messages.statusMessages import STATUS_200
from app.schemas.singleReporteSchema import SingleReportSchema


class TestSingleReportHistogram(BaseGetHistogramTest):
    endpoint_get = EndpointConfig.endpoint_single
    expect_status_get = STATUS_200
    schema_general_get = SingleReportSchema


class TestSingleReportPlot(BaseGetPlotTest):
    endpoint_get = EndpointConfig.endpoint_single
    expect_status_get = STATUS_200
    schema_general_get = SingleReportSchema


class TestSingleReportMultiPlot(BaseGetMultiPlotTest):
    endpoint_get = EndpointConfig.endpoint_single
    expect_status_get = STATUS_200
    schema_general_get = SingleReportSchema


class TestSingleReportBoxPlot(BaseGetBoxPlotTest):
    endpoint_get = EndpointConfig.endpoint_single
    expect_status_get = STATUS_200
    schema_general_get = SingleReportSchema


class TestSingleReportMultiBoxPlot(BaseGetMultiBoxPlotTest):
    endpoint_get = EndpointConfig.endpoint_single
    expect_status_get = STATUS_200
    schema_general_get = SingleReportSchema


class TestSingleReportScatter(BaseGetScatterTest):
    endpoint_get = EndpointConfig.endpoint_single
    expect_status_get = STATUS_200
    schema_general_get = SingleReportSchema


class TestSingleReportStatistics(BaseGetStatisticsTest):
    endpoint_get = EndpointConfig.endpoint_single
    expect_status_get = STATUS_200
    schema_general_get = SingleReportSchema
