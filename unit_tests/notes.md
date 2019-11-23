```python
from unittest.mock import Mock
mock = Mock()
mock

mock.some_attribute

mock.do_something()

json = Mock()
json.dumps()
json.loads('{"k": "v"}').get('k')

json.loads('{"key": "value"}')


# Number of times you called loads():
json.loads.call_count

# The last loads() call:
json.loads.call_args

# List of loads() calls:
json.loads.call_args_list

# List of calls to json's methods (recursively):
json.method_calls

```

```python
from unittest.mock import Mock

# Create a mock object
json = Mock()

json.loads('{"key": "value"}')


# You know that you called loads() so you can
# make assertions to test that expectation
json.loads.assert_called()
json.loads.assert_called_once()
json.loads.assert_called_with('{"key": "value"}')
json.loads.assert_called_once_with('{"key": "value"}')

json.loads('{"key": "value"}')


# If an assertion fails, the mock will raise an AssertionError
json.loads.assert_called_once()

     


json.loads.assert_called_once_with('{"key": "value"}')

     


json.loads.assert_not_called()
```


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
