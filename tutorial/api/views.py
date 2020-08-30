from rest_framework import status
import datetime
from django.utils.timezone import utc

from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.http import JsonResponse

from tutorial.models import Movie,Ticket,User
from tutorial.api.serializers import MovieSerializer,TicketSerializer,UserSerializer


# Delete a ticket as expired if there is a diff of 8 hours between the ticket timing and current time
def expire_ticket():
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    tickets = Ticket.objects.all()
    for ticket in tickets:
        movie = Movie.objects.get(id=ticket.time_id)
        if (now-movie.time).total_seconds() > 28800:
            ticket.delete()


# 1 . An endpoint to book a ticket using a user’s name, phone number, and timings.
@api_view(['POST', ])
def api_book_ticket(request):
    expire_ticket()
    data=request.data
    udata = {'name' : data['name'], 'phone' : data['phone']}

    # Availability of Seats
    tickets = Ticket.objects.filter(time_id=data['time'])
    cnt=0
    for i in tickets:
        cnt += i.no_of_tickets
    if cnt + int(data['no_of_tickets']) > 20:
        error_data ={
            'message' : 'Seat Unavailable(Only '+str(20-cnt)+' seats left)..'
        }
        return Response(error_data)

    try:
        user = User.objects.get(phone=udata['phone'])
        tdata = {'user': user.id, 'time': data['time'], 'no_of_tickets': data['no_of_tickets']}
        serializer = TicketSerializer(data=tdata)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    except:
        serializer = UserSerializer(data=udata)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(phone=udata['phone'])
            tdata = {'user' : user.id, 'time' : data['time'], 'no_of_tickets' : data['no_of_tickets']}
            serializer = TicketSerializer(data=tdata)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        return Response(serializer.errors)


# 2. An endpoint to update a ticket timing.
@api_view(['PUT',])
def api_update_ticket_time(request,id):
    expire_ticket()
    context=request.data

    # Availability of Seats
    tickets = Ticket.objects.filter(time_id=context['time'])
    cnt = 0
    for i in tickets:
        cnt += i.no_of_tickets
    try:
        ticket = Ticket.objects.get(id=id)
        if cnt + int(ticket.no_of_tickets) > 20:
            error_data = {
                'message': 'Seat Unavailable(Only ' + str(20 - cnt) + ' seats left)..'
            }
            return Response(error_data)
        ticket.time_id = context['time']
        ticket.save()
        serializer = TicketSerializer(ticket)
        return Response(serializer.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


# 3. An endpoint to view all the tickets for a particular time.
@api_view(['GET',])
def api_get_all_tickets_for_a_time(request,id):
    expire_ticket()
    try:
        tickets = Ticket.objects.filter(time_id=id)
        serializer = TicketSerializer(tickets,many=True)
        # return JsonResponse(serializer_ticket.data)
        return JsonResponse({'status': 'success', 'tickets': serializer.data})
    except:
        return JsonResponse({'status': 'failed'})


# 4. An endpoint to delete a particular ticket.
@api_view(['DELETE',])
def api_delete_ticket(request,id):
    expire_ticket()
    try:
        ticket = Ticket.objects.get(id=id)
        ticket.delete()
        data = {
            'status': "success",
            'message': "Ticket deleted"
        }
        return JsonResponse({'status': 'success', 'data': data})
    except:
        return JsonResponse({'status': 'failed', 'message' : 'Ticket not found'})


# 5. An endpoint to view the user’s details based on the ticket id.
@api_view(['GET',])
def api_get_user_detail_from_ticket(request,id):
    expire_ticket()
    try:
        ticket = Ticket.objects.get(id=id)
        user=User.objects.get(id=ticket.user_id)
        if request.method == 'GET':
            serializer = UserSerializer(user)
            return JsonResponse({'status': 'success', 'data': serializer.data})
    except:
        return JsonResponse({'status': 'failed', 'message': 'Ticket not found'})



@api_view(['GET',])
def api_get_all_movies(request):
    expire_ticket()
    movies = Movie.objects.all()
    if request.method == 'GET':
        serializer = MovieSerializer(movies, many=True)
        # return Response(serializer.data)
        return JsonResponse({'status': 'success', 'movies': serializer.data})


@api_view(['GET',])
def api_get_all_tickets(request):
    expire_ticket()
    tickets = Ticket.objects.all()
    if request.method == 'GET':
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)

@api_view(['GET',])
def api_get_movie_detail_from_ticket(request,id):
    expire_ticket()
    try:
        ticket = Ticket.objects.get(id=id)
        movie = Movie.objects.get(id=ticket.time_id)
        serializer_movie = MovieSerializer(movie)
        return Response(serializer_movie.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)











