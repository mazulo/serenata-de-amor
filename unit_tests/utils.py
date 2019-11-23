from datetime import date
from django_mock_queries.query import MockSet

from jarbas.chamber_of_deputies.querysets import ReimbursementQuerySet


class ExtendableMockSet(MockSet, ReimbursementQuerySet):
    pass


suspicions = {
    'over_monthly_subquota': {'is_suspect': True, 'probability': 1.0}
}

sample_reimbursement_data_1 = dict(
    pk=1,
    applicant_id=13,
    batch_number=9,
    cnpj_cpf='11111111111111',
    congressperson_document=2,
    congressperson_id=1,
    congressperson_name='Roger That',
    document_id=42,
    document_number='6',
    document_type=7,
    document_value=8.90,
    installment=7,
    issue_date=date(1970, 1, 1),
    leg_of_the_trip='8',
    month=1,
    party='Partido',
    passenger='John Doe',
    numbers=[10, 11],
    remark_value=1.23,
    state='UF',
    subquota_description='Subquota description',
    subquota_group_description='Subquota group desc',
    subquota_group_id=5,
    subquota_number=4,
    supplier='Acme',
    term=1970,
    term_id=3,
    total_net_value=4.56,
    total_value=None,
    year=1970,
    probability=0.5,
    suspicions=suspicions
)

sample_reimbursement_data_2 = dict(
    pk=2,
    applicant_id=14,
    batch_number=9,
    cnpj_cpf='11111111111112',
    congressperson_document=3,
    congressperson_id=2,
    congressperson_name='Roger That 2',
    document_id=43,
    document_number='6',
    document_type=7,
    document_value=18.60,
    installment=7,
    issue_date=date(1970, 1, 1),
    leg_of_the_trip='8',
    month=1,
    party='Partido',
    passenger='John Doe',
    numbers=[10, 11],
    remark_value=1.23,
    state='UF',
    subquota_description='Subquota description',
    subquota_group_description='Subquota group desc',
    subquota_group_id=5,
    subquota_number=4,
    supplier='Acme',
    term=1970,
    term_id=3,
    total_net_value=4.56,
    total_value=None,
    year=1970,
    probability=0.5,
    suspicions=suspicions
)

sample_reimbursement_data_3 = dict(
    pk=3,
    applicant_id=15,
    batch_number=9,
    cnpj_cpf='11111111111111',
    congressperson_document=2,
    congressperson_id=1,
    congressperson_name='Roger That',
    document_id=44,
    document_number='6',
    document_type=7,
    document_value=12.90,
    installment=7,
    issue_date=date(1970, 1, 1),
    leg_of_the_trip='8',
    month=1,
    party='Partido',
    passenger='John Doe',
    numbers=[10, 11],
    remark_value=1.23,
    state='UF',
    subquota_description='Subquota description',
    subquota_group_description='Subquota group desc',
    subquota_group_id=5,
    subquota_number=4,
    supplier='Acme',
    term=1970,
    term_id=3,
    total_net_value=4.56,
    total_value=None,
    year=1970,
    probability=0.5,
    suspicions=suspicions
)
