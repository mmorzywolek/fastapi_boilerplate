run-db:
	docker run --name article_postgres -p 5432:5432 -e POSTGRES_PASSWORD=password -e POSTGRES_DB=article -v ${PWD}/db_data:/var/lib/postgresql/data -d postgres

