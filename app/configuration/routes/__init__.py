from app.configuration.routes.routes import Routes
from app.core.routes import base

__routes__ = Routes(routers=(base.router,))
