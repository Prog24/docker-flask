.PHONY: default start stop restart log logs kill clean bash db

default:
	@cat ./Makefile

status:
	@docker-compose ps

start:
	@docker-compose up -d

stop:
	@docker-compose stop

restart:
	@docker-compose restart

log:
	@docker-compose logs api

logs:
	@docker-compose logs -f api

kill:
	@docker-compose rm -sf

bash:
	@docker-compose exec api ash
