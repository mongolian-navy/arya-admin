# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.apps_app_id_routes_route_id import AppsAppIdRoutesRouteId
from .api.apps_app_id import AppsAppId
from .api.apps import Apps
from .api.engine import Engine
from .api.apps_app_id_routes import AppsAppIdRoutes


routes = [
    dict(resource=AppsAppIdRoutesRouteId, urls=['/apps/<int:app_id>/routes/<int:route_id>'], endpoint='apps_app_id_routes_route_id'),
    dict(resource=AppsAppId, urls=['/apps/<int:app_id>'], endpoint='apps_app_id'),
    dict(resource=Apps, urls=['/apps'], endpoint='apps'),
    dict(resource=Engine, urls=['/engine'], endpoint='engine'),
    dict(resource=AppsAppIdRoutes, urls=['/apps/<int:app_id>/routes'], endpoint='apps_app_id_routes'),
]