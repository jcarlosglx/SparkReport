from os import system as system_command

from app.commands.baseCommand import BaseCommand
from app.entryApp import get_config_server
from app.services.testServer import TestServer


class RunTests(BaseCommand):

    NAME: str = "run_tests"

    def run(self):
        config = get_config_server()
        with TestServer(config.TIME_WAKE_SEC) as test_server:

            test_files_path = test_server.test_files_path
            system_command(f"coverage run -m pytest {test_files_path}")
            system_command("coverage html")
            system_command("coverage report")
