from peewee import *



db_psql = PostgresqlDatabase(database='postgres', user='postgres', password='password', host='postgres_host', port=5432)
class Emails(Model):
    email = CharField()
    password = CharField()

    class Meta:
        database = db_psql


def save_email(email, password):
    obj = Emails(email=email, password=password)
    obj.save()


def get_all_emails():
    count = Emails.select().count()
    return count


def get_email(id=id):
    email = Emails.get(Emails.id == id)
    return (email.email, email.password)


def create_table():
    try:
        with db_psql.atomic():
            db_psql.create_tables([Emails])
    except:
        pass

def drop_table():
    try:
        with db_psql.atomic():
            db_psql.drop_tables([Emails])
    except:
        pass



if __name__ == '__main__':
    drop_table()
    create_table()





    with open('data.txt', 'r+') as file:
        lines = file.readlines()
        for line in lines:
            string = line.replace('\n', '')
            lst = string.split(' ')
            res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst)-1)}
            for email, password in res_dct.items():
                save_email(email, password)



#
# valerija.korolevat2nd0@gmail.com W6r4YejgMoRh7vu
# yeziluxaxug@gmail.com 5LvRmDBUKThEdhr
# supeloviwusis@gmail.com w896JL0m3c460VG
# aspleyyostcr1037@gmail.com ftjbobmi8
# goyaverdinezq389@gmail.com ekeraduzw
# mclellancartonzv4481@gmail.com oamiznaxfa
# crittendonaugensteinib7005@gmail.com ybhxvrexiv
# spitznoglemedawarkb7972@gmail.com n41cpbvdw
# lozowskifuentezte145@gmail.com 7vepl8i4t
# wootanstolarzue5057@gmail.com nlojfrvx6
# sirnaparmentierva8341@gmail.com	7ljnvtitvl7
# mehtaboeversjt6914@gmail.com gkmcmvttfw
# manzaymorattobg8302@gmail.com cwsnkctsm9
# adelinastephaniema2743@gmail.com ko2i8riuu
# ilaganpoortingaym6983@gmail.com	qlbj31fkg
# delbridgeconferrr3286@gmail.com	eea3db0dm
# pietrowskineislerzb142@gmail.com qgdi3xbj9m
# dragnajeffriswu3581@gmail.com 8w4wknimf1
# wojtanikmihokxr6446@gmail.com gexbotfjpr
# voitierknoblochey972@gmail.com hjdhbg1h0
