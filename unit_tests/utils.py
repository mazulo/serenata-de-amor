from django_mock_queries.query import MockSet

from jarbas.chamber_of_deputies.querysets import ReimbursementQuerySet


class ExtendableMockSet(MockSet, ReimbursementQuerySet):
    pass
