__author__ = 'Group 2-5'

from django.db import models
from django.contrib.auth.models import AbstractUser
from polymorphic import PolymorphicModel


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


class User(AbstractUser):
    # Inherited attributes:
    # username
    # password
    # first name
    # last name
    # email
    # last login
    # isActive
    # date Joined
    security_question = models.CharField(max_length=100)
    security_answer = models.CharField(max_length=100)
    password_reset = models.BooleanField(default=False)
    phone = models.CharField(max_length=15, blank=True, null=True)


class Address(models.Model):
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=25, choices=STATES)
    zip = models.CharField(max_length=5)
    type = models.CharField(max_length=30, blank=True, null=True)
    user = models.ForeignKey(User, related_name='user')    


class Category(models.Model):
    description = models.CharField(max_length=300)


class Item(models.Model):
    name = models.CharField(max_length=100)
    item_source = models.CharField(max_length=50)
    description = models.CharField(max_length=300, blank=True, null=True)
    notes = models.CharField(max_length=500, blank=True, null=True)
    category = models.ForeignKey(Category)

    def __str__(self):
        return '{} {} {}'.format(self.name, self.description, self.item_source)


class Photograph(models.Model):
    date_taken = models.DateField(auto_now=False)
    place_taken = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    image = models.CharField(max_length=100)
    item = models.ForeignKey(Item)


class Organization(User):
    organization_name = models.CharField(max_length=100)
    organization_type = models.CharField(max_length=50, blank=True, null=True)


class Volunteer(User):
    biographical_sketch = models.CharField(max_length=500, blank=True, null=True)
    # contact_relationship = models.ForeignKey('self')


class Event(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    map_filename = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    address = models.OneToOneField(Address)

    def __str__(self):
        return '{} {} {}'.format(self.start_date, self.map_filename)


class Area(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True, null=True)
    place_number = models.IntegerField(max_length=3)
    coordinator = models.ForeignKey(Volunteer, related_name="Area_coordinator")
    supervisor = models.ForeignKey(Volunteer, related_name="Area_supervisor")
    event = models.ForeignKey(Event)

    def __str__(self):
        return '{} {} {}'.format(self.name, self.description, self.place_number)


class Transaction(models.Model):
    date = models.DateField()
    total_cost = models.DecimalField(max_digits=8, decimal_places=2)
    date_packed = models.DateField(null=True, blank=True)
    date_paid = models.DateField(null=True, blank=True)
    date_shipped = models.DateField(null=True, blank=True)
    shipped_by = models.ForeignKey(Volunteer, related_name="transaction_shipped_by", null=True, blank=True)
    tracking_number = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey(User, )
    volunteer = models.ForeignKey(Volunteer, null=True, blank=True, related_name="transaction_volunteer")

    def __str__(self):
        return '{} {} {}'.format(self.payment_handler, self.user, self.volunteer)


class Payment(models.Model):
    type = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    amount_paid = models.DecimalField(max_digits=8, decimal_places=2)
    Transaction = models.ManyToManyField(Transaction, null=True, blank=True, related_name="payment")


class ShoppingCart(models.Model):
    user = models.OneToOneField(User, primary_key=True)


class NonSaleItem(Item):
    value = models.DecimalField(max_digits=8, decimal_places=2)


class RentableItem(NonSaleItem):
    times_rented = models.IntegerField(default=0)
    rental_price = models.DecimalField(max_digits=6, decimal_places=2)
    price_per_day = models.DecimalField(max_digits=4, decimal_places=2)
    replacement_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return '{} {} {}'.format(self.name, self.price_per_day, self.rental_price)


class WardrobeItem(RentableItem):
    size = models.CharField(max_length=8)
    size_modifier = models.CharField(max_length=20, blank=True, null=True)
    GENDER = (
        ('M', 'Men'),
        ('W', 'Women'),
        ('U', 'Unisex'),
    )
    gender = models.CharField(max_length=1, choices=GENDER)
    color = models.CharField(max_length=20)
    pattern = models.CharField(max_length=20, null=True, blank=True)
    start_year = models.DateField(max_length=4, blank=True, null=True)
    end_year = models.DateField(max_length=4, blank=True, null=True)


class RentalLineItem(models.Model):
    date_out = models.DateField()
    date_due = models.DateField()
    discount_percent = models.IntegerField(null=True, blank=True)
    rentable_item = models.ForeignKey(RentableItem, null=True, blank=True, related_name="rentable_item")
    wardrobe_item = models.ForeignKey(WardrobeItem, null=True, blank=True, related_name="wardrobe_item")


class ReturnLineItem(models.Model):
    date_in = models.DateTimeField()
    damage_fee = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    damage_note = models.CharField(max_length=200, blank=True, null=True)
    days_late = models.IntegerField()
    late_fee = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    rental_line_item = models.ForeignKey(RentalLineItem)


class Product(Item):
    price = models.DecimalField(max_digits=8, decimal_places=2)
    qty_on_hand = models.IntegerField()
    date_made = models.DateField()
    area = models.ForeignKey(Area, null=True, blank=True)

    def __str__(self):
        return '{} {} {}'.format(self.id, self.name, self.price)


class PersonalizedProduct(Product):
    production_time = models.TimeField()
    order_form = models.CharField(max_length=250)
    volunteer = models.ForeignKey(Volunteer)


class LineItem(models.Model):
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(max_length=6)
    # A save for later feature would be a cool add on, but for now we will hold off on it.
    # save_for_later = models.BooleanField(default=False)
    transaction = models.ForeignKey(Transaction, null=True, blank=True)
    shopping_cart = models.ForeignKey(ShoppingCart, null=True, blank=True)

    # Changed the OneToOne fields to Foreign key fields
    product = models.ForeignKey(Product, null=True, blank=True, related_name='LineItem_Product')
    personalized_product = models.ForeignKey(PersonalizedProduct, null=True,
                                                blank=True, related_name='PersonalizedProduct'),
    rental_line_item = models.ForeignKey(RentalLineItem, null=True, blank=True, related_name='RentalLineItem')
    return_line_item = models.ForeignKey(ReturnLineItem, null=True, blank=True, related_name='ReturnLineItem')

    def product_id(self):
        product = self.product
        id = product.id
        return id

    def product_name(self):
        product = self.product
        name = product.name
        return name

    def product_price(self):
        product = self.product
        price = product.price
        return price

    def rental_item_name(self):
        rentalitem = self.rental_line_item
        name = rentalitem.rentable_item.name
        return name

    def rental_item_price(self):
        rentalitem = self.rental_line_item
        price = rentalitem.rentable_item.rental_price
        return price


class HistoricalFigure(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    birth_place = models.CharField(max_length=100)
    death_place = models.CharField(max_length=100)
    biographical_note = models.CharField(max_length=1000)
    is_fictional = models.BooleanField(default=False)


class VolunteerRole(models.Model):
    volunteer_type = models.CharField(max_length=80)
    volunteer = models.ForeignKey(Volunteer)
    area = models.ForeignKey(Area)
    historical_figure = models.ForeignKey(HistoricalFigure, null=True, blank=True)