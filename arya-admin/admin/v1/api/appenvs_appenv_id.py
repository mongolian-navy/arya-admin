# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas


class AppenvsAppenvId(Resource):

    def get(self, appenv_id):
        print(g.args)

        return {}, 200, None