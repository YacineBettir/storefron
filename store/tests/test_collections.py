from store.models import Collection
from rest_framework import status
import pytest
from model_bakery import baker

@pytest.fixture
def create_collection(client_api):
    def do_create_collection(collection):
        return client_api.post('/store/collections/',collection)
    return do_create_collection

@pytest.mark.django_db
class TestCreateCollection():
    
    def test_if_user_annonymous_returns_401(self,create_collection):
        
        
        response=create_collection({'title':'a'})
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        
    def test_if_user_is_not_admin_returns_403(self,authenticate_users,create_collection):
        authenticate_users()

        response=create_collection({'title':'a'})
        
        assert response.status_code ==status.HTTP_403_FORBIDDEN
            
    def test_if_data_is_invalid_returns_400(self,create_collection,authenticate_users):
        authenticate_users(True)
        
        response=create_collection({'title':''})
        
        assert response.status_code==status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None 
        
    def test_if_data_is_valid_retuns_201(self,authenticate_users,create_collection):
        authenticate_users(True)
        
        response=create_collection({'title':'a'})        
        
        assert response.status_code==status.HTTP_201_CREATED
        assert response.data['id'] >0
        
        
@pytest.mark.django_db
class TestRetrieveCollection():
    
    def test_if_collection_exsists_returns_200(self,client_api):
            
        collection=baker.make(Collection)
        response=client_api.get(f'/store/collections/{collection.id}/')
        
        
        assert response.status_code==status.HTTP_200_OK
        assert response.data=={
            'id':collection.id,
            'title':collection.title,
            'products_count':0
        }
        
    def test_if_collection_deleted_returns_404(self,
                                               authenticate_users,
                                               client_api):
        authenticate_users(is_staff=True)
        
        
        collection=baker.make(Collection)
        response=client_api.delete(f'/store/collections/{collection.id}/')
        
        assert response.status_code==status.HTTP_204_NO_CONTENT
        