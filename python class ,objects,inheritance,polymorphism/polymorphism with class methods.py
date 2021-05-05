class india:
    def language(self):
        print('hindi')
    def capital(self):
        print('delhi')
class england:
    def language(self):
        print('english')
    def capital(self):
        print('london')
ind=india()
eng=england()
for country in (ind,eng):
    country.language()
    country.capital()
