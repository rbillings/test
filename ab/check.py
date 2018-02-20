 # -*- coding: utf-8 -*-

from urllib.parse import urlparse
import argparse
import sys
from collections import defaultdict

import requests


reqs = requests.Session()
