#!/usr/bin/env python

import os

for env_var in  os.environ:
    print env_var
    #print os.environ[env_var]

# if 'AIRFLOW_HOME' not in os.environ:
#     AIRFLOW_HOME = os.path.expanduser('~/airflow')
# else:
#     AIRFLOW_HOME = os.environ['AIRFLOW_HOME']