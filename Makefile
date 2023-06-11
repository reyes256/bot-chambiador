start:
	cd ../minecraft-server && docker compose up -d

stop:
	cd ../minecraft-server && docker compose down

show-players:
	cd ../minecraft-server && docker exec mc-server rcon-cli list