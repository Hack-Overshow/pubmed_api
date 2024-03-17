# PubMed Scraper API

The PubMed Scraper API is a web service that allows you to search for academic studies related to specific keywords on PubMed and retrieve the search results in JSON format.

## Usage

The API endpoint is the homepage itself. To search for academic studies, you need to provide the search query and optionally specify the number of results to retrieve.

### Request

- **Method:** GET
- **Parameters:**
  - `query`: The search query, specifying the keyword(s) to search for.
  - `num_results`: (Optional) The number of results to retrieve. Defaults to 10 if not provided.

#### Example Request:

```http
GET /?query=common+cold&num_results=20
```

This request searches for information related to "common cold" and requests 20 results.

### Response

The response contains JSON data with the search results.

#### Example Response:

```json
{
  "results": [
    {
      "Title": "Study Title",
      "Authors": "Author 1, Author 2",
      "Abstract": "Abstract text...",
      "Citation": "Journal Citation",
      "URL": "https://example.com/study"
    },
    {
      "Title": "Another Study Title",
      "Authors": "Author 3, Author 4",
      "Abstract": "Another abstract text...",
      "Citation": "Another Journal Citation",
      "URL": "https://example.com/another-study"
    },
    ...
  ]
}
```

### Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/pubmed-scraper-api.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Django development server:

   ```bash
   python manage.py runserver
   ```

### Dependencies

- Django
- BeautifulSoup4
- pandas
- tqdm

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
