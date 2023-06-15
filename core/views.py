from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(http_method_names=["GET"])
def health_check(request):
    return Response({"status": "OK", "message": "Working!"}, status=200)
