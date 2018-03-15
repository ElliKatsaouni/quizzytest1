# TO DO:
# Change the population data according to the new models
# Check / add the methods which actually add the data
# Set up the database (incl. admin superuser) and migrate
# [Get the server properly running. Problem should be in the User model]

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quizzy_project.settings')

import django
django.setup()
from quizzy.models import City, Pub, Quiz
from django.template.defaultfilters import slugify


def populate():

    # These are the dictionaries for the quizzes.
    admiral_quizzes = [
        {"categories": "General Knowledge, Music, History & Politics, Sports, TV & Film",
         # we still have to find out how to pass data to the next two:
         "weekday": 'Tuesday',
         "time": '18:30',
         "prize": "£50 food and drink tab, plus a rolling cash jackpot for 100% correct answers",
         "entry_fee": 0,
         "upVotes": 70,
         "downVotes": 30}]

    bankstreet_quizzes = [
        {"categories": "General Knowledge, Music, History & Politics, Sports, TV & Film",
         # we still have to find out how to pass data to the next two:
         "weekday": 'Sunday',
         "time": '20:00',
         "prize": "£20 bar/food tab for winners; pizza voucher for La Favorita for runners-up. "
                  "There is also a cash jackpot which rolls over if not won",
         "entry_fee": 1,
         "upVotes": 80,
         "downVotes": 20}]

    craftypig_quizzes = [
        {"categories": "General Knowledge, Music, History & Politics, Sports, TV & Film",
         # we still have to find out how to pass data to the next two:
         "weekday": 'Thursday',
         "time": '20:00',
         "prize": "£40 voucher; also, there is a rolling jackpot which starts off as a £25 voucher and "
                  "increases by £25 each week if not won",
         "entry_fee": 0,
         "upVotes": 40,
         "downVotes": 60}]

    lansdowne_quizzes = [
        {"categories": "General Knowledge, Music, History & Politics, Sports, TV & Film",
         # we still have to find out how to pass data to the next two:
         "weekday": 'Tuesday',
         "time": '18:30',
         "prize": "£50 food and drink tab, plus a rolling cash jackpot for 100% correct answers",
         "entry_fee": 0,
         "upVotes": 70,
         "downVotes": 30}]

    butterflypig_quizzes = [
        {"categories": "General Knowledge, Music, History & Politics, Sports, TV & Film",
         # we still have to find out how to pass data to the next two:
         "weekday": 'Tuesday',
         "time": '18:30',
         "prize": "£50 food and drink tab, plus a rolling cash jackpot for 100% correct answers",
         "entry_fee": 0,
         "upVotes": 70,
         "downVotes": 30}]

    amberrose_quizzes = [
        {"categories": "General Knowledge, Music, History & Politics, Sports, TV & Film",
         # we still have to find out how to pass data to the next two:
         "weekday": 'Monday',
         "time": '19:30',
         "prize": "£30 bar tab for winners",
         "entry_fee": 0,
         "upVotes": 45,
         "downVotes": 55}]

    threesisters_quizzes = [
        {"categories": "General Knowledge, Music, History & Politics, Sports, TV & Film",
         # we still have to find out how to pass data to the next two:
         "weekday": 'Tuesday',
         "time": '22:00',
         "prize": "£50 voucher",
         "entry_fee": 0,
         "upVotes": 80,
         "downVotes": 20}]

    skylark_quizzes = [
        {"categories": "General Knowledge, Music, History & Politics, Sports, TV & Film",
         # we still have to find out how to pass data to the next two:
         "weekday": 'Thursday',
         "time": '20:00',
         "prize": "£20 voucher, bottle of wine, selection of beers",
         "entry_fee": 0,
         "upVotes": 95,
         "downVotes": 5}]

    fountain_quizzes = [
        {"categories": "General Knowledge, Music, History & Politics, Sports, TV & Film",
         # we still have to find out how to pass data to the next two:
         "weekday": 'Sunday',
         "time": '20:00',
         "prize": "1st - £50 bar tab; 2nd - bottle of wine; 3rd - bag of sweets",
         "entry_fee": 0,
         "upVotes": 65,
         "downVotes": 35}]

    harmonium_quizzes = [
        {"categories": "General Knowledge, Music, History & Politics, Sports, TV & Film",
         # we still have to find out how to pass data to the next two:
         "weekday": 'Wednesday',
         "time": '20:00',
         "prize": "£30 bar tab for winners of main quiz; "
                  "there is also a jackpot round for a cash prize of £30 which rolls up if not won",
         "entry_fee": 0,
         "upVotes": 75,
         "downVotes": 25}]

    bobbin_quizzes = [
        {"categories": "General Knowledge, Music, History & Politics, Sports, TV & Film",
         # we still have to find out how to pass data to the next two:
         "weekday": 'Sunday',
         "time": '21:00',
         "prize": "Various",
         "entry_fee": 1,
         "upVotes": 60,
         "downVotes": 40}]

    foundry_quizzes = [
        {"categories": "General Knowledge, Music, History & Politics, Sports, TV & Film",
         # we still have to find out how to pass data to the next two:
         "weekday": 'Sunday',
         "time": '20:00',
         "prize": "Varies from week to week - usually food/drink vouchers",
         "entry_fee": 0,
         "upVotes": 70,
         "downVotes": 30}]

    redlion_quizzes = [
        {"categories": "General Knowledge, Music, History & Politics, Sports, TV & Film",
         # we still have to find out how to pass data to the next two:
         "weekday": 'Sunday',
         "time": '19:00',
         "prize": "Cash prize for winners, bar tab for runners-up plus other random prizes",
         "entry_fee": 1,
         "upVotes": 30,
         "downVotes": 70}]

    globeinn_quizzes = [
        {"categories": "General Knowledge, Music, History & Politics, Sports, TV & Film",
         # we still have to find out how to pass data to the next two:
         "weekday": 'Monday',
         "time": '20:30',
         "prize": "1st - £25 voucher, 2nd - £15 voucher",
         "entry_fee": 0,
         "upVotes": 80,
         "downVotes": 20}]

    gaslamp_quizzes = [
        {"categories": "General Knowledge, Music, History & Politics, Sports, TV & Film",
         # we still have to find out how to pass data to the next two:
         "weekday": 'Wednesday',
         "time": '20:00',
         "prize": "Various",
         "entry_fee": 2,
         "upVotes": 60,
         "downVotes": 40}]

    # These are the dictionaries for the pubs.
    glasgow_pubs = [
        {"name": "The Admiral",
         "street": "Waterloo Street",
         "street_number": "72a",
         "postcode": "G2 7DA",
         "url": "http://www.theadmiralbar.com/",
         "telephone": "0141 221 7705",
         "quizzes": admiral_quizzes},

        {"name": "Bank Street Cafe",
         "street": "Bank Street",
         "street_number": "52",
         "postcode": "G12 8LZ",
         "url": "http://bankst.co.uk/",
         "telephone": "0141 334 4343",
         "quizzes": bankstreet_quizzes},

        {"name":"The Crafty Pig",
         "street": "Great Western Road",
         "street_number": "508",
         "postcode": "G12 8EL",
         "url": "http://www.crafty-pig.com/",
         "telephone": "0141 237 4040",
         "quizzes": craftypig_quizzes},

        {"name": "The Lansdowne",
         "street": "Lansdowne Crescent",
         "street_number": "7a",
         "postcode": "G20 6NQ",
         "url": "http://www.lansdownebar.co.uk/",
         "telephone": "0141 334 4653",
         "quizzes": lansdowne_quizzes},

        {"name": "The Butterfly and the Pig",
         "street": "Bath Street",
         "street_number": "153",
         "postcode": "G2 4SQ",
         "url": "http://www.thebutterflyandthepig.com/",
         "telephone": "0141 221 7711",
         "quizzes": butterflypig_quizzes},
    ]

    edinburgh_pubs = [
        {"name": "The Amber Rose",
         "street": "Castle Street",
         "street_number": "22-26",
         "postcode": "EH2 4LS",
         "url": "http://www.theamberroseedinburgh.co.uk/",
         "telephone": "0131 226 1224",
         "quizzes": amberrose_quizzes},

        {"name": "The Three Sister",
         "street": "Cowgate",
         "street_number": "139",
         "postcode": "EH1 1JS",
         "url": "http://www.thethreesistersbar.co.uk/",
         "telephone": "0131 622 6801",
         "quizzes": threesisters_quizzes},

        {"name": "The Skylark",
         "street": "Portobello High Street",
         "street_number": "241",
         "postcode": "EH15 2AW",
         "url": "http://www.theskylarkportobello.com/",
         "telephone": "0131 629 3037",
         "quizzes": skylark_quizzes},

        {"name": "The Fountain",
         "street": "Dundee Street",
         "street_number": "131",
         "postcode": "EH11 1AX",
         "url": "http://www.fountainbar.co.uk/",
         "telephone": "0131 229 1899",
         "quizzes": fountain_quizzes},

        {"name": "Harmonium",
         "street": "Henderson Street",
         "street_number": "60",
         "postcode": "EH6 6DE",
         "url": "N/A",
         "telephone": "0131 555 3160",
         "quizzes": harmonium_quizzes},
    ]

    aberdeen_pubs = [
        {"name": "The Bobbin",
         "street": "King Street",
         "street_number": "500",
         "postcode": "AB24 5ST",
         "url": "http://www.screampubs.co.uk/thebobbinaberdeen",
         "telephone": "01224 495318",
         "quizzes": bobbin_quizzes},

        {"name": "Foundry",
         "street": "Holburn Street",
         "street_number": "41-43",
         "postcode": "AB10 6BR",
         "url": "http://www.foundryaberdeen.co.uk/",
         "telephone": "01224 585364",
         "quizzes": foundry_quizzes},

        {"name": "The Red Lion",
         "street": "Spital",
         "street_number": "130",
         "postcode": "AB24 3JU",
         "url": "N/A",
         "telephone": "01224 634400",
         "quizzes": redlion_quizzes},

        {"name": "The Globe Inn",
         "street": "North Silver Street",
         "street_number": "13",
         "postcode": "AB10 1RJ",
         "url": "http://theglobeinn-aberdeen.co.uk/",
         "telephone": "01224 624258",
         "quizzes": globeinn_quizzes},

        {"name": "The Gaslamp",
         "street": "Market Street",
         "street_number": "42-44",
         "postcode": "AB11 5PL",
         "url": "N/A",
         "telephone": "01224 588773",
         "quizzes": gaslamp_quizzes},
    ]

    # These are the dictionaries for the cities.
    cities = {"Glasgow": {"pubs": glasgow_pubs},
              "Edinburgh": {"pubs": edinburgh_pubs},
              "Aberdeen": {"pubs": aberdeen_pubs}}

    for city in cities:
        c = add_city(city)
        for pub in cities[city]['pubs']:
            p = add_pub(c, pub["name"], pub["street"], pub["street_number"], pub["postcode"], pub["url"], pub["telephone"])
            for quiz in pub['quizzes']:
                add_quiz(p, quiz["categories"], quiz["weekday"], quiz["time"],
                         quiz["prize"], quiz["entry_fee"], quiz["upVotes"], quiz["downVotes"])

    # for c in City.objects.all():
    #     for p in Pub.objects.filter(city=c):
    #         print("- {0} - {1}".format(str(c), str(p)))
    #
    # for p in Pub.objects.all():
    #     for q in Quiz.objects.filter(pub=p):
    #         print("- {0} - {1}".format(str(p), str(q)))


def add_city(name):
    c = City.objects.get_or_create(name=name)[0]
    c.slug = slugify(name)
    c.save()
    return c


def add_pub(city, name, street, street_number, postcode, url, telephone):
    p = Pub.objects.get_or_create(city=city, name=name)[0]
    p.street = street
    p.street_number = street_number
    p.postcode = postcode
    p.url = url
    p.telephone = telephone
    p.slug = slugify(name)
    p.save()
    return p


def add_quiz(pub, categories, weekday, time, prize, entry_fee, upVotes, downVotes):
    q = Quiz.objects.get_or_create(pub=pub, weekday=weekday)[0]
    q.time = time
    q.prize = prize
    q.categories = categories
    q.entry_fee = entry_fee
    q.upVotes = upVotes
    q.downVotes = downVotes
    q.save()
    return q


if __name__ == '__main__':
    print("Starting Quizzy_Project population script...")
    populate()

