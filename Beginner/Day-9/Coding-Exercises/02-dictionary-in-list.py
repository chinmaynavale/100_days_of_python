travel_blog = [
    {
        'country': 'France',
        'visits': 12,
        'cities': ['Paris', 'lille', 'Dijon'],
    },
    {
        'country': 'Germany',
        'visits': 5,
        'cities': ['Berlin', 'Hamburg', 'Stuttgart'],
    },
]


def new_country(country, visits, cities):
    travel_blog.append({
        'country': country,
        'visits': visits,
        'cities': cities,
    })


new_country('Russia', 2, ['moscow', 'Saint Petersburg'])
print(travel_blog, end='\n')
