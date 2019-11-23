import pytest
from django_mock_queries.query import MockSet
from model_mommy.mommy import prepare

from jarbas.chamber_of_deputies.views import (
    ReimbursementListView,
)
from jarbas.chamber_of_deputies.models import Reimbursement


@pytest.fixture(autouse=True)
def reimbursement_qs(mocker):
    queryset_mock = MockSet(
        prepare(Reimbursement, 3)
    )

    mocker.patch(
        'jarbas.chamber_of_deputies.views.ReimbursementListView.queryset',
        queryset_mock,
    )
    serializer = mocker.Mock()
    serializer.data = {}

    mocker.patch(
        'jarbas.chamber_of_deputies.views.ReimbursementListView'
        '.serializer_class',
        serializer,
    )


class TestGet:

    def test_status_code_200(self, mocker, rf):

        list_view = ReimbursementListView()
        request = rf.get('')
        request.user = mocker.Mock()
        request.query_params = {}
        list_view.format_kwarg = {}
        list_view.request = request

        response = list_view.get(request)

        assert response.status_code == 200
