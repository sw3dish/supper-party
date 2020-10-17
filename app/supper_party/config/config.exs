# This file is responsible for configuring your application
# and its dependencies with the aid of the Mix.Config module.
#
# This configuration file is loaded before any dependency and
# is restricted to this project.

# General application configuration
use Mix.Config

config :supper_party,
  ecto_repos: [SupperParty.Repo]

# Configures the endpoint
config :supper_party, SupperPartyWeb.Endpoint,
  url: [host: "localhost"],
  secret_key_base: "3Lp/N/X3YqJNrfOXQFMnLsQgCR7n4s39M8Qu0A8IuxoOKG8pc5LTOsFFjmdrYx/c",
  render_errors: [view: SupperPartyWeb.ErrorView, accepts: ~w(html json), layout: false],
  pubsub_server: SupperParty.PubSub,
  live_view: [signing_salt: "UiTh2Yx/"]

# Configures Elixir's Logger
config :logger, :console,
  format: "$time $metadata[$level] $message\n",
  metadata: [:request_id]

# Use Jason for JSON parsing in Phoenix
config :phoenix, :json_library, Jason

# Import environment specific config. This must remain at the bottom
# of this file so it overrides the configuration defined above.
import_config "#{Mix.env()}.exs"
