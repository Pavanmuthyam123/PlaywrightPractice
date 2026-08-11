"""Simple configuration for tests and environments."""

BASE_URL = "https://the-internet.herokuapp.com"

# List of supported browser names for parametrization or config
BROWSERS = ["chromium", "firefox", "webkit"]

# Default headless mode — can be toggled in CI or locally
HEADLESS = True

# Environment key (placeholder for future multi-env support)
ENV = "qa"
