# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os

def test_filesize_whitelist:
    f = os.path.getsize(".cache/profiles/XXX/safebrowsing/*trackwhite")
    assert f < 400000
    # returns size in bytes, mozstd-trackwhite-digest256, mozstdstaging-trackwhite-digest256 [NEW]
    # moztestpub-trackwhite-digest256
