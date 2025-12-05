.PHONY: help build up down restart logs shell clean

help:
	@echo "🐳 Commandes disponibles:"
	@echo "  make build    - Construire l'image Docker"
	@echo "  make up       - Démarrer l'application"
	@echo "  make down     - Arrêter l'application"
	@echo "  make restart  - Redémarrer"
	@echo "  make logs     - Voir les logs"
	@echo "  make shell    - Ouvrir un shell"
	@echo "  make clean    - Tout nettoyer"

build:
	@echo "🔨 Construction..."
	docker-compose build

up:
	@echo "🚀 Démarrage..."
	docker-compose up -d
	@echo "✅ App: http://localhost:8080"
	@echo "📊 Portainer: http://localhost:9000"

down:
	@echo "🛑 Arrêt..."
	docker-compose down

restart:
	docker-compose restart

logs:
	docker-compose logs -f web

shell:
	docker-compose exec web bash

clean:
	@echo "🧹 Nettoyage..."
	docker-compose down -v
	docker system prune -f
