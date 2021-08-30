import os

ENV = bool(os.environ.get("ENV", False))
if ENV:
    from heroku_DYNAMICConfig import Var as Config
else:
    from heroku_DYNAMICConfig import Development as Config


Var = Config
