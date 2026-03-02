import os

c = get_config()  # noqa: F821

# ---------------------------------------------------------------------------
# JupyterHub general settings
# ---------------------------------------------------------------------------
c.JupyterHub.ip = "0.0.0.0"
c.JupyterHub.port = int(os.environ.get("JUPYTERHUB_PORT", 8000))

# Proxy auth token (set via env for security)
c.ConfigurableHTTPProxy.auth_token = os.environ.get(
    "CONFIGURABLE_PROXY_AUTH_TOKEN",
    os.environ.get("JUPYTERHUB_SECRET_TOKEN", ""),
)

# ---------------------------------------------------------------------------
# Spawner – use SimpleLocalProcessSpawner (single-container setup)
# ---------------------------------------------------------------------------
c.JupyterHub.spawner_class = "simple"

# Default to JupyterLab interface
c.Spawner.default_url = "/lab"
c.Spawner.http_timeout = 120
c.Spawner.start_timeout = 120
c.Spawner.args = ["--allow-root"]

# ---------------------------------------------------------------------------
# Authenticator – local system users created automatically
# ---------------------------------------------------------------------------
c.JupyterHub.authenticator_class = "dummy"

# Admin user name from environment variable
admin_user = os.environ.get("JUPYTERHUB_ADMIN_USER", "admin")
admin_password = os.environ.get("JUPYTERHUB_ADMIN_PASSWORD", "admin")

c.DummyAuthenticator.password = admin_password
c.Authenticator.admin_users = {admin_user}

# Allow admin to access the admin panel
c.JupyterHub.admin_access = True

# ---------------------------------------------------------------------------
# Database – SQLite stored inside the mounted volume
# ---------------------------------------------------------------------------
c.JupyterHub.db_url = "sqlite:///jupyterhub.sqlite"
