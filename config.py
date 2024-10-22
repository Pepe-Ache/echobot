#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

# gunicorn --bind 0.0.0.0 --worker-class aiohttp.worker.GunicornWebWorker --timeout 600 app:app

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "c9d36d28-741a-4db3-b69a-e0dd328441a5")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "J_68Q~xZgxbK1H1C-QPA0.NdFh4zd26-I_TM2ccI")