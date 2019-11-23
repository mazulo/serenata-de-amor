```python
from jarbas.chamber_of_deputies.models import Reimbursement

from unit_tests.utils import sample_reimbursement_data_1, sample_reimbursement_data_2, sample_reimbursement_data_3

r1 = Reimbursement(**sample_reimbursement_data_1)

r2 = Reimbursement(**sample_reimbursement_data_2)

r3 = Reimbursement(**sample_reimbursement_data_3)

from django_mock_queries.query import MockSet

queryset = MockSet(r1, r2, r3)

print([x for x in queryset.filter(congressperson_id=2)])

print([x for x in queryset.filter(congressperson_id=1)])

print([x for x in queryset.filter(congressperson_document=3)])

from django.db.models import Avg

print(queryset.all().aggregate(Avg('document_value')))

print([x for x in queryset.filter(congressperson_name__iexact='Mazulo')])

print([x for x in queryset.filter(congressperson_name__iexact='Roger')])

print([x for x in queryset.filter(congressperson_name__iexact='Roger That')])

from django.db.models import Q

print([x for x in queryset.filter(Q(congressperson_name__iexact='Roger That') | Q(congressperson_name__iexact='Roger That 2'))])
```
