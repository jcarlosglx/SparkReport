from dataclasses import dataclass


@dataclass
class EndpointConfig:
    endpoint_health_check_server: str = "/health_server"
    endpoint_logs: str = "/logs"
    endpoint_single: str = "/single"
    endpoint_square: str = "/square"
    endpoint_quarter: str = "/quarter"
