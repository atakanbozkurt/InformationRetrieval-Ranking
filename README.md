# Information Retrieval-Ranking
Contributors: Ahmet Atakan Bozkurt, Yaodong Yang


Usage: python main.py
Place your query inside main.py into query variable if you want to search different documents.

In this application, we indexed 200 documents related with economics.
Every documents received scores based on the content, no authoritive assesments made for documents.

Implemented "vector based cosinus similarity" and "probabilistic based okapi similarity" function to calculate similarity between each document and query.

Document at A Time approach used calculate similiarties.

Relevance feedback was made for top10k documents for test queries which are "Europe", "stock rally", "debt crisis" and "stock future higher"