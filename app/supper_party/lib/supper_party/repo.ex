defmodule SupperParty.Repo do
  use Ecto.Repo,
    otp_app: :supper_party,
    adapter: Ecto.Adapters.Postgres
end
