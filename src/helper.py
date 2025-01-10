from langchain.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings

# Extract data from the pdf 
def load_pdf_file(data):
    loader = DirectoryLoader(data, 
                             glob="*.pdf", 
                             loader_cls=PyPDFLoader)
    
    documents = loader.load() 
    return documents

# Split the data into Text chunks
def text_split(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 20)
    text_chunks = text_splitter.split_documents(extracted_data)
    return text_chunks

