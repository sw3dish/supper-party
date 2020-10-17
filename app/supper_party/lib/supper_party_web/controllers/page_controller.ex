defmodule SupperPartyWeb.PageController do
  use SupperPartyWeb, :controller

  def index(conn, _params) do
    render(conn, "index.html")
  end
end
