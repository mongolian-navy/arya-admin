# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.appenvs import Appenvs
from .api.appenvs_appenv_id import AppenvsAppenvId
from .api.appenvs_appenv_id_routes_route_id import AppenvsAppenvIdRoutesRouteId
from .api.appenvs_appenv_id_routes import AppenvsAppenvIdRoutes
from .api.engine import Engine


routes = [
    dict(resource=Appenvs, urls=['/appenvs'], endpoint='appenvs'),
    dict(resource=AppenvsAppenvId, urls=['/appenvs/<int:appenv_id>'], endpoint='appenvs_appenv_id'),
    dict(resource=AppenvsAppenvIdRoutesRouteId, urls=['/appenvs/<int:appenv_id>/routes/<int:route_id>'], endpoint='appenvs_appenv_id_routes_route_id'),
    dict(resource=AppenvsAppenvIdRoutes, urls=['/appenvs/<int:appenv_id>/routes'], endpoint='appenvs_appenv_id_routes'),
    dict(resource=Engine, urls=['/engine'], endpoint='engine'),
]