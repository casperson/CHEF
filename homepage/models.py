__author__ = 'Sterling'

from django.db import models


class LegalEntity(models.Model):
    legal_entity_id = models.IntegerField(primary_key=True)
    given_name = models.CharField(max_length=20, blank=False)
    creation_date = models.DateField()
    address1 = models.CharField(max_length=50, blank=False)
    address2 = models.CharField(max_length=50)
    city = models.CharField(max_length=20, blank=False)
    state = models.CharField(max_length=2, blank=False, choices=STATES)
    zip = models.IntegerField(max_length=12, blank=False)
    email = models.CharField(max_length=40, blank=False)


class Person(LegalEntity):
    person_id = models.IntegerField(primary_key=True)
    family_name = models.CharField(max_length=20, blank=False)
    user_id = models.OneToOneField(DjangoUser)


class Organization(LegalEntity):
    organization_id = models.IntegerField(primary_key=True)
    organization_type = models.CharField(max_length=20, blank=False)


class Agent(Person):
    agent_id = models.IntegerField(primary_key=True)
    appointment_date = models.DateTimeField(auto_now=False, blank=False)


class Participant(Person):
    participant_id = models.IntegerField(primary_key=True)
    biographical_sketch = models.CharField(max_length=300, blank=False)
    contact_relationship = models.CharField(max_length=30, blank=False)
    photo = models.CharField(max_length=100, blank=False)
    emergency_contact = models.IntegerField(Person, blank=False)
    areas = models.ManyToManyField(Area)


class Phone(object):
    phone_id = models.IntegerField(primary_key=True)
    number = models.IntegerField(max_length=12, blank=False)
    extension = models.IntegerField(max_length=5)
    TYPE = (
        ('Cell', 'Cellular'),
        ('Home', 'Home'),
        ('Business', 'Business'),
        ('Other', 'Other'),
    )
    type = models.CharField(max_length=20, blank=False)
    legal_entity_id = models.IntegerField(LegalEntity)


class Item(models.Model):
    item_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=False)
    description = models.CharField(max_length=20)
    value = models.DecimalField(max_length=8, decimal_places=2, blank=False)
    standard_rental_price = models.DecimalField(max_length=8, decimal_places=2, blank=False)
    legal_entity_id = models.IntegerField(LegalEntity)
    rentals = models.ManyToManyField(Rental)


class Picture(models.Model):
    picture_id = models.IntegerField(primary_key=True)
    picture = models.CharField(max_length=100, blank=False)
    caption = models.CharField(max_length=75)
    item_id = models.IntegerField(Item)
    product_id = models.IntegerField(Product)


class WardrobeItem(Item):
    wardrobe_item_id = models.IntegerField(primary_key=True)
    size = models.CharField(max_length=8, blank=False)
    size_modifier = models.CharField(max_length=20)
    GENDER = (
        ('M','Men'),
        ('W', 'Women'),
        ('U', 'Unisex'),
    )
    gender = models.CharField(max_length=1, blank=False, choices=GENDER)
    color = models.CharField(max_length=20, blank=False)
    pattern = models.CharField(max_length=20)
    start_year = models.IntegerField(max_length=4, blank=False)
    end_year = models.IntegerField(max_length=4, blank=False)
    note = models.CharField(max_length=300)


class RentedItem(object):
    rented_item_id = models.IntegerField(primary_key=True)
    CONDITION = (
        ('Poor', 'Poor'),
        ('OK', 'OK'),
        ('Good', 'Good'),
        ('Like-New', 'Like-New'),
    )
    condition = models.CharField(max_length=20, blank=False, choices=CONDITION)
    new_damage = models.CharField(max_length=20)
    damage_fee = models.DecimalField(max_length=8, decimal_places=2)
    late_fee = models.DecimalField(max_length=8, decimal_places=2)
    return_id = models.IntegerField(Return)


class Rental(object):
    rental_id = models.IntegerField(primary_key=True)
    rental_time = models.DateTimeField(auto_now=False, blank=False)
    due_date = models.DateField(auto_now=False, blank=False)
    discount_percent = models.DecimalField(max_length=3, decimal_places=2)
    item_id = models.IntegerField(Item)
    organization_id = models.IntegerField(Organization)
    person_id = models.IntegerField(Person)
    agent_id = models.IntegerField(Agent)
    items = models.ManyToManyField(Item)


class Return(object):
    return_id = models.IntegerField(primary_key=True)
    return_time = models.DateTimeField(blank=False)
    fees_paid = models.DecimalField(max_length=8, decimal_places=2)
    agent_id = models.IntegerField(Agent)


class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=30, blank=False)
    current_price = models.DecimalField(decimal_places=2, max_digits=8, blank=False)
    legal_entity_id = models.IntegerField(LegalEntity)
    picture_id = models.IntegerField(Picture)


class BulkProduct(Product):
    bulk_product_id = models.IntegerField(primary_key=True)
    quantity_on_hand = models.IntegerField(max_length=8)
    orders = models.ManyToManyField(Order)


class IndividualProduct(Product):
    individual_product_id = models.IntegerField(primary_key=True)
    date_made = models.DateField(auto_now=False)
    order_id = models.IntegerField(Order)


class PersonalProduct(Product):
    personal_product_id = models.IntegerField(primary_key=True)
    order_form_name = models.CharField(max_length=30)
    production_time = models.TimeField(auto_now=False)
    order_file = models.CharField(max_length=100)
    orders = models.ManyToManyField(Order)


class DjangoUser(object):
    user_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=15, blank=False)
    last_name = models.CharField(max_length=20, blank=False)
    email = models.CharField(max_length=30, blank=False)
    password = models.CharField(max_length=20, blank=False)
    address = models.CharField(max_length=50, blank=False)
    city = models.CharField(max_length=30, blank=False)
    state = models.CharField(max_length=2, choices=STATES)
    zip = models.IntegerField(max_length=10, blank=False)
    country = models.CharField(max_length=40, blank=False)
    security_question = models.CharField(max_length=100, blank=False)
    security_answer = models.CharField(max_length=20, blank=False)
    role = models.CharField(max_length=20, blank=False)
    record_creation_date = models.DateTimeField(auto_now=False)
    phone_number = models.CharField(max_length=12, blank=False)
    person_id = models.OneToOneField(Person)
    order_id = models.OneToOneField(Order)


class Order(object):
    order_id = models.IntegerField(primary_key=True)
    order_date = models.DateTimeField(auto_now=False, blank=False)
    date_packed = models.DateTimeField(auto_now=False)
    date_paid = models.DateTimeField(auto_now=False)
    date_shipped = models.DateTimeField(auto_now=False)
    tracking_number = models.CharField(max_length=30)
    packed_by = models.IntegerField(Agent)
    processed_by = models.IntegerField(Agent)
    shipped_by = models.IntegerField(Agent)
    bulk_products = models.ManyToManyField(BulkProduct)
    personal_products = models.ManyToManyField(PersonalProduct)
    user_id = models.OneToOneField(DjangoUser)


class Area(object):
    area_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=False)
    description = models.CharField(max_length=300)
    place_number = models.IntegerField(max_length=20, blank=False)
    coordinator_id = models.IntegerField(Agent, blank=False)
    supervisor_id = models.IntegerField(Agent, blank=False)
    event_id = models.IntegerField(Event, blank=False)
    participants = models.ManyToManyField(Participant)


class SaleItem(object):
    sale_item_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=300)
    low_price = models.DecimalField(max_length=8, decimal_places=2)
    high_price = models.DecimalField(max_length=8, decimal_places=2)
    area_id = models.IntegerField(Area, blank=False)


class Event(object):
    event_id = models.IntegerField(primary_key=True)
    start_date = models.DateTimeField(auto_now=False, blank=False)
    end_date = models.DateTimeField(auto_now=False, blank=False)
    map_file_name = models.CharField(max_length=100)
    name = models.CharField(max_length=20, blank=False)
    description = models.CharField(max_length=300)


class Venue(object):
    venue_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=False)
    address = models.CharField(max_length=50, blank=False)
    city = models.CharField(max_length=20, blank=False)
    state = models.CharField(max_length=2, blank=False)
    zip = models.IntegerField(max_length=10, blank=False)
    event_id = models.IntegerField(Event)


STATES = (
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('DC', 'District of Columbia'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming'),
)