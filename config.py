#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

# gunicorn --bind 0.0.0.0 --worker-class aiohttp.worker.GunicornWebWorker --timeout 600 app:app

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "a430df57-e02d-451e-9b63-50347ce4f020")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "rAe8Q~zEPKAB0leHwNL63t_i5EVoPFCedzd.baLs")
