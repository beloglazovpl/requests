import requests


class SuperHero:

    def get_intelligience(self, name):
        url = 'https://superheroapi.com/api/2619421814940190/search/' + name
        response = requests.get(url=url)
        character = response.json()
        description = character['results']
        for stats in description:
            if stats['name'] == name:
                hero_intelligence = int(stats['powerstats']['intelligence'])
                return hero_intelligence


if __name__ == '__main__':
    hero = SuperHero()
    hulk = hero.get_intelligience('Hulk')
    cap = hero.get_intelligience('Captain America')
    thanos = hero.get_intelligience('Thanos')
    if hulk > cap and hulk > thanos:
        print('Самый умный супергерой Hulk')
    elif cap > hulk and cap > thanos:
        print('Самый умный супергерой Captain America')
    else:
        print('Самый умный супергерой Thanos')