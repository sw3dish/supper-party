# This happens to be the version of Erlang + Elixir that I have on my machine
FROM hexpm/elixir:1.11.0-erlang-22.3.4.11-debian-buster-20200607

WORKDIR /usr/srv/app

COPY . .

RUN mix local.hex --force

CMD [ "sleep", "infinity" ]

# RUN mix do compile
