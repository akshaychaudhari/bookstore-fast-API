# Online Bookstore API

## A bookstore-fast-API

This project is an online bookstore API built using FastAPI and MongoDB. It allows users to view, search, and purchase books. The API includes various features such as data validation, aggregation, indexing, search functionality, and asynchronous programming.

<h2> Team Members </h2>

    [Akshay Chaudhari]
    [Sambhaji Ippar]

<h2> Prerequisites </h2>

    Python 3.8 or higher
    MongoDB
    FastAPI
    PyMongo

<h2> Installation </h2>

    Clone the GitHub repository:
    git clone https://github.com/your-username/bookstore-api.git

    Change to the project directory:
    cd bookstore-api

    Install the required dependencies:
    pip install -r requirements.txt

    Configure the MongoDB connection settings in api_constants.py.

<h3> Commands for virtual environment </h3>

    python3 -m venv venv --system-site-packages
    source venv/bin/activate
    deactivate

<h2> Usage </h2>

    Start the API server:
    python3 -m uvicorn main:app --port 8090 --reload  

    Access the API documentation in your browser at http://localhost:8090/docs.

<h2> API Endpoints </h2> 
    
    GET /books
    
    Retrieves a list of all books in the store.
    
    GET /books/{book_id}
    
    Retrieves a specific book by ID.
    
    POST /books
    
    Adds a new book to the store.
    
    PUT /books/{book_id}
    
    Updates an existing book by ID.
    
    DELETE /books/{book_id}
    
    Deletes a book from the store by ID.
    
    GET /search?title={}&author={}&min_price={}&max_price={}
    
    Searches for books by title, author, and price range.

<h2> Data Model </h2>

The book data model includes the following fields:

    title (string): The title of the book.
    author (string): The author of the book.
    description (string): A description of the book.
    price (float): The price of the book.
    stock (integer): The available stock of the book.

<h2> MongoDB Connection </h2>

    The API establishes an asynchronous connection to MongoDB using PyMongo.
    Data Validation
    
    Pydantic is used to validate the incoming book data before it is stored in MongoDB. 
    The API returns an appropriate error message if the data fails validation.
    
<h2> Aggregation </h2>

    The API uses MongoDB's aggregation framework to retrieve the following data:

    The total number of books in the store.
    The top 5 bestselling books.
    The top 5 authors with the most books in the store.

<h2> Indexing </h2>

    Appropriate indexes are created for the MongoDB collection to optimize query performance.
    Operators
    
    MongoDB's query operators are used to implement the following search functionality:

    Search for books by title.
    Search for books by author.
    Search for books by price range.

<h2> Asynchronous Programming </h2>

    All database operations are done asynchronously to ensure the API remains responsive and performant.
