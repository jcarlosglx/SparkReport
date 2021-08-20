from dataclasses import dataclass


@dataclass
class EndpointConfig:
    endpoint_health_check_server: str = "/health_server"
    endpoint_father: str = "/father"
