from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from .models import CreditEntry
from .serializers import CreditEntrySerializer
from django.db.models import Sum
from .models import Customer
from .serializers import CustomerSerializer

@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET', 'POST'])
def credit_entries(request):
    if request.method == 'GET':
        user_id = request.GET.get('user')
        category = request.GET.get('category')

        filters = {}
        if user_id:
            filters['user'] = user_id
        if category:
            filters['category'] = category

        entries = CreditEntry.objects.filter(**filters)
        serializer = CreditEntrySerializer(entries, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CreditEntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET'])
def user_dashboard(request, user_id):
    entries = CreditEntry.objects.filter(user=user_id)
    total_amount = entries.aggregate(Sum('amount'))['amount__sum'] or 0
    count = entries.count()
    latest = entries.order_by('-created_at').first()

    data = {
        "user": user_id,
        "total_credits": total_amount,
        "entry_count": count,
        "latest_entry": CreditEntrySerializer(latest).data if latest else None
    }
    return Response(data)

@api_view(['GET', 'PUT', 'DELETE'])
def credit_entry_detail(request, entry_id):
    try:
        entry = CreditEntry.objects.get(id=entry_id)
    except CreditEntry.DoesNotExist:
        return Response({"error": "Credit entry not found."}, status=404)

    if request.method == 'GET':
        serializer = CreditEntrySerializer(entry)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CreditEntrySerializer(entry, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        entry.delete()
        return Response(status=204)
    
@api_view(['POST'])
def register_customer(request):
    data = request.data.copy()
    try:
        salary = float(data.get('monthly_salary', 0))
        approved_limit = round(salary * 36, -5)  # nearest lakh
        data['approved_limit'] = approved_limit
    except:
        return Response({'error': 'Invalid salary'}, status=400)

    serializer = CustomerSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

def index(request):
    return HttpResponse("Hello from the Users App!")

