from django.utils.translation import gettext as _
from django.shortcuts import render
from .models import Article
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import openai

def query_gpt3(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Modèle GPT-3 de OpenAI
        prompt=prompt,
        max_tokens=150  # Nombre maximal de tokens dans la réponse générée
    )
    return response.choices[0].text.strip()

def article_list(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
        'title': _('List of Articles'),  # Exemple de chaîne à traduire
    }
    return render(request, 'main/article_list.html', context)

@csrf_exempt  # Permet les requêtes POST sans CSRF token (à ajuster en fonction de vos besoins de sécurité)
def chatbot_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('input_text', '')

        # Utiliser GPT-3 pour générer une réponse
        #response = query_gpt3(user_input)

        return JsonResponse({'response': user_input})

    return render(request, 'main/chatbot.html')

@csrf_exempt  # Permet les requêtes POST sans CSRF token (à ajuster en fonction de vos besoins de sécurité)
def rag_search_view(request):
    if request.method == 'POST':
        user_query = request.POST.get('query', '')

        # Utiliser RAG pour la recherche
        response = search_with_rag(user_query)

        return JsonResponse({'response': response})

    return render(request, 'main/rag_search.html')