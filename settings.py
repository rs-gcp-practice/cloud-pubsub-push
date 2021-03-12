import io
import os

# from google.oauth2 import service_account
import environ


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# start[load env file]
env = environ.Env()

# env_file path
env_file = os.path.join(BASE_DIR, ".env")
# check if `.env` file exists, then load it
if os.path.isfile(env_file):
    env.read_env(env_file)
# end[load env]

# start[project settings and auth]

# secret key
SECRET_KEY = env("SECRET_KEY")
# project settings and sub token for verification
PROJECT = env("GOOGLE_CLOUD_PROJECT")
PUBSUB_TOPIC = env("PUBSUB_TOPIC")
PUBSUB_VERIFICATION_TOKEN = env("PUBSUB_VERIFICATION_TOKEN")
