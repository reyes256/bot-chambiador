start:
	cd ../minecraft-server && docker compose up -d && cd ../bot-chambiador

stop:
	cd ../minecraft-server && docker compose down && cd ../bot-chambiador

show-players:
	cd ../minecraft-server && docker exec mc-server rcon-cli list && cd ../bot-chambiador