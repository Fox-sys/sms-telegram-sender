import asyncio
import signal
import sys
from uvicorn import Config, Server

from src.presentation.api.app import app


async def run_server(config: Config):
    server = Server(config)
    server_task = asyncio.create_task(server.serve())

    def signal_handler(sig, frame):
        server.should_exit = True

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    await server_task


if __name__ == "__main__":
    cli_args = sys.argv[1:]

    kwargs = {}
    for arg in cli_args:
        if "=" in arg:
            key, value = arg.split("=", 1)
            if value.isdigit():
                value = int(value)
            elif value.lower() in ("true", "false"):
                value = value.lower() == "true"
            kwargs[key] = value

    kwargs.setdefault("host", "127.0.0.1")
    kwargs.setdefault("port", 8000)
    kwargs.setdefault("timeout_graceful_shutdown", 5)

    config = Config(app=app, **kwargs)
    asyncio.run(run_server(config))
