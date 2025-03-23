#!/bin/bash
echo "🛠️  Levantando contenedor de PostgreSQL con pgvector..."
sudo docker compose up -d



echo "🌐 Exponiendo puerto 5432 con ngrok (modo TCP)..."
ngrok tcp 5432
