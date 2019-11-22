import pytest

from django_mock_queries.query import MockSet

from jarbas.chamber_of_deputies.models import Reimbursement
from jarbas.chamber_of_deputies.tests import sample_reimbursement_data
from .utils import ExtendableMockSet


@pytest.fixture
def reimbursement_data():
    return sample_reimbursement_data


class TestSuspicious:

    def test_count_suspicions(
        self,
        mocker,
        reimbursement_data,
    ):
        data = reimbursement_data.copy()
        data['document_id'] = 42 * 2
        del data['suspicions']
        del data['probability']

        mock_queryset = ExtendableMockSet(
            Reimbursement(**reimbursement_data),
            Reimbursement(**data),
            model=Reimbursement,
        )
        mocker.patch(
            'jarbas.chamber_of_deputies.models.Reimbursement'
            '.objects',
            mock_queryset,
        )

        assert Reimbursement.objects.suspicions(True).count() == 1

    def test_count_not_suspicions(
        self,
        mocker,
        reimbursement_data,
    ):
        data = reimbursement_data.copy()
        data['document_id'] = 42 * 2
        del data['suspicions']
        del data['probability']

        mock_queryset = ExtendableMockSet(
            Reimbursement(**reimbursement_data),
            Reimbursement(**data),
            model=Reimbursement,
        )
        mocker.patch(
            'jarbas.chamber_of_deputies.models.Reimbursement'
            '.objects',
            mock_queryset,
        )

        assert Reimbursement.objects.suspicions(False).count() == 1
