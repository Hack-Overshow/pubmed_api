from django.http import JsonResponse
from .study_search import StudySearch

def search_view(request):
    # Get query and num_results from request parameters
    query = request.GET.get('query', '')
    num_results = int(request.GET.get('num_results', 10))
    
    # Create an instance of StudySearch and perform the search
    study_search = StudySearch(query=query, num=num_results)
    search_results = study_search.search_to_df().to_dict(orient='records')
    
    # Return the search results as a JSON response
    return JsonResponse({'results': search_results})
