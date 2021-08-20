from flask import Flask


def load_blueprints(instance: Flask):
    from app.routes.healthCheckServerRoute import health_check_server_blueprint
    from app.routes.logsRoute import logs_blueprint

    prefix = instance.config["APPLICATION_ROOT"]

    instance.register_blueprint(logs_blueprint, url_prefix=prefix)
    instance.register_blueprint(health_check_server_blueprint, url_prefix=prefix)
