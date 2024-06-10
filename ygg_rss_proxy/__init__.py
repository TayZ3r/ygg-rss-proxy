from ygg_rss_proxy.settings import settings
from ygg_rss_proxy.app import app
from ygg_rss_proxy.logging_config import logger
from ygg_rss_proxy.run_gunicorn import GunicornApp


options = {
    "bind": f"{settings.gunicorn_binder}:{settings.gunicorn_port}",
    "workers": settings.gunicorn_workers,
    "preload_app": True,
}

logger.info("----------------------------------------------------------")
logger.info(
    f"Starting ygg_rss_proxy on {settings.rss_shema}://{settings.rss_host}:{settings.rss_port}"
)
logger.info("----------------------------------------------------------")

GunicornApp(app, options).run()
