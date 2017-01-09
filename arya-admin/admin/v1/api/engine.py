# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas


class Engine(Resource):

    def get(self):

        return {}, 200, None

    def put(self):
        print(g.json)

        return {}, 200, None