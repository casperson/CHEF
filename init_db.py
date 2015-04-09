# !/usr/bin/env python

# initialize django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'chef.settings'
import django
django.setup()

# normal imports
import sys
import homepage.models as hmod
from django.contrib.auth.models import Group, Permission, ContentType
from django.db import connection
import subprocess

# drop the database or truncate it
# delete all migrations directories
# recreate the database
cursor = connection.cursor()
cursor.execute("DROP SCHEMA PUBLIC CASCADE")
cursor.execute("CREATE SCHEMA PUBLIC")
subprocess.call([sys.executable, "manage.py", "migrate"])

# ######### CREATE PERMISSIONS/GROUPS #####################

Permission.objects.all().delete()
Group.objects.all().delete()

permission1 = Permission()
permission1.codename = 'admin_rights'
permission1.content_type = ContentType.objects.get(id=27)
permission1.name = 'Has Admin Rights'
permission1.save()

permission2 = Permission()
permission2.codename = 'manager_rights'
permission2.content_type = ContentType.objects.get(id=27)
permission2.name = 'Has Manager Rights'
permission2.save()

permission3 = Permission()
permission3.codename = 'guest_rights'
permission3.content_type = ContentType.objects.get(id=27)
permission3.name = 'Has Guest Rights'
permission3.save()

group = Group()
group.name = "Admins"
group.save()
group.permissions.add(permission1)

group2 = Group()
group2.name = "Managers"
group2.save()
group2.permissions.add(permission2)

group3 = Group()
group3.name = "Guests"
group3.save()
group3.permissions.add(permission3)

# ###### create all the tables (python manage.py migrate) ###########

for data in [
    ["sTracy", 'Sterling', 'Tracy', 'sterling.tracy.4@gmail.com', 'whodis',
     'What is your favorite animal', 'Dog', False, '480-999-5555'],
    ["DanTheMan", 'Daniel', 'Friebe', 'danielfriebe11@gmail.com', 'whodis',
     'What is your favorite animal', 'Dog', False, '461-999-5555'],
]:
    u = hmod.User()
    u.username = data[0]
    u.first_name = data[1]
    u.last_name = data[2]
    u.email = data[3]
    u.set_password(data[4])
    u.security_question = data[5]
    u.security_answer = data[6]
    u.password_reset = data[7]
    u.phone = data[8]
    u.save()

for data in [
    ['350 N 200 W', 'Provo', 'UT', '84606', 'shipping', hmod.User.objects.get(id=2)],
    ['400 State Street', 'Provo', 'UT', '84604', 'shipping', hmod.User.objects.get(id=1)],
]:
    x = hmod.Address()
    x.address = data[0]
    x.city = data[1]
    x.state = data[2]
    x.zip = data[3]
    x.type = data[4]
    x.user = data[5]
    x.save()


for data in [
    ["Clothing"],
    ["Weapons"],
    ["Culinary"],
    ["Toys"],
    ["Artifacts"],
]:
    i = hmod.Category()
    i.description = data[0]
    i.save()


for data in [
    ['We Are Colonial', 'Profit', 'Colonial', 'colonial@WeAreColonial.org', 'whodis',
     'What is your favorite animal', 'Dog', False, '420-989-5544'],
    ['Map Makers Unlimited', 'Non-Profit', 'MapMaker', 'MapMaker@MMU.com', 'whodis',
     'What is your favorite animal', 'Dog', False, '433-978-5345'],
]:

    o = hmod.Organization()
    o.organization_name = [0]
    o.organization_type = [1]
    o.username = data[2]
    o.email = data[3]
    o.set_password(data[4])
    o.security_question = data[5]
    o.security_answer = data[6]
    o.password_reset = data[7]
    o.phone = data[8]
    o.save()

for data in [
    ["uncleb", "winner123", "Braden", "Casperson", "bradencasperson@gmail.com", "2015-3-4", True, "2015-2-28",
     "What is the name of your dog?", "Sadie", False, "801-571-6625", "Born in Utah, raised in Idaho"],
    ["vader", "lordvader", "Darth", "Vader", "vader@gmail.com", "2015-3-4", True, "2015-2-18",
     "What is the name of your planet of destruction?", "Deathstar", False, "208-999-9999",
     "Once was good, but now is evil. Want to conquer the galaxy."],
]:
    v = hmod.Volunteer()
    v.username = data[0]
    v.set_password(data[1])
    v.first_name = data[2]
    v.last_name = data[3]
    v.email = data[4]
    v.last_login = data[5]
    v.is_active = data[6]
    v.date_joined = data[7]
    v.security_question = data[8]
    v.security_answer = data[9]
    v.password_reset = data[10]
    v.phone = data[11]
    v.biographical_sketch = data[12]
    # v.contact_relationship = data[13]
    v.save()

for data in [
    ['2015-6-4', '2015-6-10', " ", "Colonial Heritage Festival", "The largest colonial festival in the world",
     hmod.Address.objects.get(id=1)],
    ['2016-6-4', '2016-6-10', " ", "Colonial Heritage Festival", "The largest colonial festival in the world",
     hmod.Address.objects.get(id=2)],
]:

    u = hmod.Event()
    u.start_date = data[0]
    u.end_date = data[1]
    u.map_filename = data[2]
    u.name = data[3]
    u.description = data[4]
    u.address = data[5]
    u.save()

for data in [
    ["Printing Press", "Learn how to print in colonial times", 1, hmod.Volunteer.objects.get(id=5),
     hmod.Volunteer.objects.get(id=6), hmod.Event.objects.get(id=1)],
    ["Blacksmith", "See the blacksmith at work", 2, hmod.Volunteer.objects.get(id=5),
     hmod.Volunteer.objects.get(id=6), hmod.Event.objects.get(id=1)],
]:
    u = hmod.Area()
    u.name = data[0]
    u.description = data[1]
    u.place_number = data[2]
    u.coordinator = data[3]
    u.supervisor = data[4]
    u.event = data[5]
    u.save()


for data in [
    ["2015-3-4", 892.15, "2015-3-5", "2015-3-4", hmod.Volunteer.objects.get(id=5), "2015-3-6",
     hmod.Volunteer.objects.get(id=5), "80708", hmod.User.objects.get(id=1), hmod.Volunteer.objects.get(id=5)],
    ["2015-3-2", 226.54, "2015-3-3", "2015-3-2", hmod.Volunteer.objects.get(id=5), "2015-3-4",
     hmod.Volunteer.objects.get(id=5), "77878", hmod.User.objects.get(id=1), hmod.Volunteer.objects.get(id=5)],
]:
    t = hmod.Transaction()
    t.date = data[0]
    t.total_cost = data[1]
    t.date_packed = data[2]
    t.date_paid = data[3]
    t.payment_handler = data[4]
    t.date_shipped = data[5]
    t.shipped_by = data[6]
    t.tracking_number = data[7]
    t.user = data[8]
    t.volunteer = data[9]
    t.save()


for data in [
    ['Cash', '2015-05-20', 20.25],
    ['Credit', '2015-05-21', 10.00],
]:

    p = hmod.Payment()
    p.type = data[0]
    p.date = data[1]
    p.amount_paid = data[2]
    p.save()

for data in [
    [hmod.User.objects.get(id=1)],
    [hmod.User.objects.get(id=2)]
]:

    s = hmod.ShoppingCart()
    s.user = data[0]
    s.save()

for data in [
    ["Life-size Replica of canon", "Revolutionary War Style Canon", "Gove owns everything",
     hmod.Category.objects.get(id=2), 5425.00],
    ["Replica of Juno's Wrath", "Replica Ship, half size", "Gove Allen... duh!", hmod.Category.objects.get(id=4),
     3675.00],
]:
    ns = hmod.NonSaleItem()
    ns.name = data[0]
    ns.description = data[1]
    ns.item_source = data[2]
    ns.category = data[3]
    ns.value = data[4]
    ns.save()

for data in [
    ["Top Hat", "comes in Small, Medium, Large", "Hat Suiter", hmod.Category.objects.get(id=2),
     20.00, 50, "2014-01-02"],
    ["Toy Sword", "For the kiddies", "Toys-R-Us", hmod.Category.objects.get(id=4), 10.00, 100, "2014-03-04"],
]:
    p = hmod.Product()
    p.name = data[0]
    p.description = data[1]
    p.item_source = data[2]
    p.category = data[3]
    p.price = data[4]
    p.qty_on_hand = data[5]
    p.date_made = data[6]
    p.save()

for data in [
    ["Custom Ship Replica", "Tom Burton's request", "Gove Allen Store", hmod.Category.objects.get(id=1), 250.00, 2,
     "2015-2-6", '10:00:00',
     "this/is/the/file/path.pdf", hmod.Volunteer.objects.get(id=5)],
    ["Custom Top Hat", "Uncle B wants a sick top hat", "Hat Shop", hmod.Category.objects.get(id=2), 65.00, 1,
     "2015-3-5", '5:45:00',
     "uncle/b/file/path.pdf", hmod.Volunteer.objects.get(id=5)],
]:
    p = hmod.PersonalizedProduct()
    p.name = data[0]
    p.description = data[1]
    p.item_source = data[2]
    p.category = data[3]
    p.price = data[4]
    p.qty_on_hand = data[5]
    p.date_made = data[6]
    p.production_time = data[7]
    p.order_form = data[8]
    p.volunteer = data[9]
    p.save()

for data in [
    ["Pistol", "Old Pistol", "Revolutionary War", hmod.Category.objects.get(id=2), 500.00, 10.00, 3.00, 400.00],
    ["Moonshine Bottle", "Bottles used for getting drunk", "Unknown: since is was illegal ;)",
     hmod.Category.objects.get(id=3), 20.00, 3.00, 1.00, 30.00],
]:
    u = hmod.RentableItem()
    u.name = data[0]
    u.description = data[1]
    u.item_source = data[2]
    u.category = data[3]
    u.value = data[4]
    u.rental_price = data[5]
    u.price_per_day = data[6]
    u.replacement_price = data[7]
    u.save()

for data in [
    ['2015-04-15', '2015-04-20', 10, hmod.RentableItem.objects.get(id=7)],
    ['2015-04-26', '2015-04-28', 5, hmod.RentableItem.objects.get(id=8)],
]:

    rr = hmod.RentalLineItem()
    rr.date_out = data[0]
    rr.date_due = data[1]
    rr.discount_percent = data[2]
    rr.rentable_item = data[3]
    rr.save()

for data in [
    ["2015-2-15", 2.50, "Pee stain", 1, 1.00, hmod.RentalLineItem.objects.get(id=1)],
    ["2015-2-15", 0.00, "", 5, 5.50, hmod.RentalLineItem.objects.get(id=1)]
]:
    ret = hmod.ReturnLineItem()
    ret.date_in = data[0]
    ret.damage_fee = data[1]
    ret.damage_note = data[2]
    ret.days_late = data[3]
    ret.late_fee = data[4]
    ret.rental_line_item = data[5]
    ret.save()

for data in [
    [8.00, 1, None, hmod.ShoppingCart.objects.get(user_id=1), hmod.Product.objects.get(id=3), None, None, None, hmod.User.objects.get(id=1)],
    [10.00, 2, None, hmod.ShoppingCart.objects.get(user_id=1), None, None, hmod.RentalLineItem.objects.get(id=1), None, hmod.User.objects.get(id=1)],
]:

    l = hmod.LineItem()
    l.amount = data[0]
    l.quantity = data[1]
    l.transaction = data[2]
    l.shopping_cart = data[3]
    l.product = data[4]
    l.personalized_product = data[5]
    l.rental_line_item = data[6]
    l.return_line_item = data[7]
    l.user = data[8]
    l.save()


for data in [
    ["Breeches", "Pants for Gove", "Gove's Closet", hmod.Category.objects.get(id=1), 30.00, 3.00, 2.00, 25.00, 32, "M",
     "Gray", "1750-01-01", "1790-01-01"],
    ["Boots", "Buckle Boots", "Antique Shop", hmod.Category.objects.get(id=1), 25.00, 2.00, 2.00, 30.00, 11, "M",
     "Black", "1770-01-01", "1785-01-01"],
]:
    n = hmod.WardrobeItem()
    n.name = data[0]
    n.description = data[1]
    n.item_source = data[2]
    n.category = data[3]
    n.value = data[4]
    n.rental_price = data[5]
    n.price_per_day = data[6]
    n.replacement_price = data[7]
    n.size = data[8]
    n.gender = data[9]
    n.color = data[10]
    n.start_year = data[11]
    n.end_year = data[12]
    n.save()


for data in [
    ['2014-1-3', "The backyard", "James Harden for MVP", " ", hmod.Item.objects.get(id=1)],
    ['2013-1-7', "The backyard", "Stephen Curry for MVP", " ", hmod.Item.objects.get(id=1)],
]:
    u = hmod.Photograph()
    u.date_taken = data[0]
    u.place_taken = data[1]
    u.description = data[2]
    u.image = data[3]
    u.item = data[4]
    u.save()


for data in [
    ["George Washington", "1772-2-22", "Westmoreland, VA", "Mount Vernon, VA", "Had wooden teeth", False, ],
    ["Johnny Appleseed", "1774-9-26", "Leominster, MA", "Fort Wayne, IN", "Spread love through apples", False, ]
]:
    h = hmod.HistoricalFigure()
    h.name = data[0]
    h.birth_date = data[1]
    h.birth_place = data[2]
    h.death_place = data[3]
    h.biographical_note = data[4]
    h.is_fictional = data[5]
    h.save()

for data in [
    ["Coordinator", hmod.Volunteer.objects.get(id=5), hmod.Area.objects.get(id=1), None],
    ["Historical Figure", hmod.Volunteer.objects.get(id=5), hmod.Area.objects.get(id=1),
     hmod.HistoricalFigure.objects.get(id=1)]
]:
    v = hmod.VolunteerRole()
    v.volunteer_type = data[0]
    v.volunteer = data[1]
    v.area = data[2]
    v.historical_figure = data[3]
    v.save()

    user = hmod.User.objects.get(id=1)
    user.user_permissions.add(permission1)
    user.groups.add(group)
    # user.user_permissions.add(permission2)
    # user.user_permissions.add(permission3)

    user = hmod.User.objects.get(id=2)
    user.user_permissions.add(permission3)