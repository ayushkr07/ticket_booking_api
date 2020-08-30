import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db

from django.test import RequestFactory
from tutorial.api.views import *

import json

def test_get_all_movies():
    mixer.blend('tutorial.Movie', name='Dil bechara')
    request=RequestFactory().get('/api/get_all_movies/')
    response= api_get_all_movies(request)
    a = json.loads(response.content.decode('utf-8'))
    print(a)
    assert a['status'] == "success"
    assert a['movies'][0]['name'] == 'Dil bechara'

def test_get_all_tickets_for_a_time():
    time=mixer.blend('tutorial.Movie', id=1, name='Dil bechara' , time="2020-08-30T07:29:49.773300Z")
    user=mixer.blend('tutorial.User', id=1)
    print(user.__dict__)
    c=mixer.blend('tutorial.Ticket', user_id=user.id, time_id=time.id, no_of_tickets=4)
    print(c.__dict__)
    request=RequestFactory().get('/api/get_all_tickets_for_a_time/',{'id':1})
    response= api_get_all_tickets_for_a_time(request,id=1)
    a = json.loads(response.content.decode('utf-8'))
    print(a)
    assert a['status'] == "success"


# def test_delete_ticket_when_ticket_found():
#     time=mixer.blend('tutorial.Movie', id=1, name='Dil bechara' , time="2020-08-30T07:29:49.773300Z")
#     user=mixer.blend('tutorial.User', id=1)
#     mixer.blend('tutorial.Ticket', id=2, user=user, time=time, no_of_tickets=4)
#     request=RequestFactory().delete('/api/delete_ticket/')
#     response= api_delete_ticket(request,id=2)
#     a = json.loads(response.content.decode('utf-8'))
#     print(a)
#     assert a['status'] == "success"

# def test_delete_ticket_when_ticket_not_found():
#     time=mixer.blend('tutorial.Movie', id=1, name='Dil bechara' , time="2020-08-30T07:29:49.773300Z")
#     user=mixer.blend('tutorial.User', id=1)
#     mixer.blend('tutorial.Ticket', id=2, user=user, time=time, no_of_tickets=4)
#     request=RequestFactory().delete('/api/delete_ticket/')
#     response= api_delete_ticket(request,id=1)
#     a = json.loads(response.content.decode('utf-8'))
#     print(a)
#     assert a['status'] == "failed"
#     assert a['message'] == "Ticket not found"

# def test_get_user_detail_from_ticket():
#     time=mixer.blend('tutorial.Movie', id=1, name='Dil bechara' , time="2020-08-30T07:29:49.773300Z")
#     user=mixer.blend('tutorial.User', id=1, name="ABC", phone="1234567890")
#     mixer.blend('tutorial.Ticket', id=2, user=user, time=time, no_of_tickets=4)
#     request=RequestFactory().get('/api/get_user_detail_from_ticket/')
#     response= api_get_user_detail_from_ticket(request,id=2)
#     a = json.loads(response.content.decode('utf-8'))
#     assert a['status'] == "success"
#     assert a['data']['name'] == "ABC"

# def test_get_user_detail_from_ticket_when_ticket_not_found():
#     time=mixer.blend('tutorial.Movie', id=1, name='Dil bechara' , time="2020-08-30T07:29:49.773300Z")
#     user=mixer.blend('tutorial.User', id=1, name="ABC", phone="1234567890")
#     mixer.blend('tutorial.Ticket', id=2, user=user, time=time, no_of_tickets=4)
#     request=RequestFactory().get('/api/get_user_detail_from_ticket/')
#     response= api_get_user_detail_from_ticket(request,id=1)
#     a = json.loads(response.content.decode('utf-8'))
#     assert a['status'] == "success"
#     assert a['data']['name'] == "ABC"