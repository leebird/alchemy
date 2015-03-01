from elric.resources.user.user import UserAuthAPI
from elric.resources.user.version import VersionAPI

ENDPOINTS = [
    (UserAuthAPI, '/user/'),
    (VersionAPI, '/version/'),
]