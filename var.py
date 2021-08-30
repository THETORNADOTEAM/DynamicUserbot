import os

ENV = bool(os.environ.get("ENV", False))
if ENV:
    from heroku_DYNAMIC import Var as Config
else:
    from heroku_DYNAMIC import Development as Config


Var = Config
