from app import create_app
from dotenv import load_dotenv
from utils.logging.logging import setup_logger
import logging
from authlib.integrations.flask_oauth2 import ResourceProtector
from utils.auth import Auth0JWTBearerTokenValidator

app = create_app()

require_auth = ResourceProtector()
validator = Auth0JWTBearerTokenValidator(
    "dev-giv3drwd5zd1cqsb.us.auth0.com", "http://dulany-test"
)
require_auth.register_token_validator(validator)

logger = logging.getLogger("__name__")
setup_logger()

logger.info("Started Up")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
