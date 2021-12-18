file = open("query.sql")
queries = file.read()
file.close()

queries_list = queries.split(";")

print(queries_list)