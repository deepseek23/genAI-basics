from langchain_community.retrievers import WikipediaRetriever

retriver = WikipediaRetriever(top_k_results=5,lang='en')

query = "who is current champions league winner ?"

result = retriver.invoke(query)
# Print retrieved content
for i, doc in enumerate(result):
    print(f"\n--- Result {i+1} ---")
    print(f"Content:\n{doc.page_content}...")  # truncate for display12`