from datetime import datetime

from app import pco_client


def get_online_type():
    types = pco_client.get('/services/v2/service_types')
    type_id = None
    for service_type in types['data']:
        if service_type['attributes']['name'] == 'Online Service Filming':
            return service_type['id']


# date should be the date of rehearsal.
# this might be fragile, won't work if rehearsal isn't first date of the Plan
def get_songs_for_date(type_id, date):
    plans = pco_client.get('/services/v2/service_types/{}/plans'.format(type_id), filter='future', include='plan_times')

    for plan in plans['data']:
        rehearsal_date = datetime.strptime(plan['attributes']['sort_date'], '%Y-%m-%dT%H:%M:%SZ')
        if rehearsal_date.strftime('%Y-%m-%d') == date.strftime('%Y-%m-%d'):
            items = _get_items_for_plan(type_id, plan)
            plan_id = plan['id']
            return plan_id, items


def _get_items_for_plan(type_id, plan):
    song_list = []

    items = pco_client.get('/services/v2/service_types/{}/plans/{}/items'.format(type_id, plan['id']),
                       include='song,key')
    for item in items['included']:

        if item['type'] == 'Song':
            title = item['attributes']['title']
            if title != 'Walk Out Slideshow':
                song_list.append(title)

        elif item['type'] == 'Key':
            start_key = item['attributes']['starting_key']
            end_key = item['attributes']['ending_key']
            if end_key:
                key = '{}-{}'.format(start_key, end_key)
            else:
                key = start_key
            song_list[-1] = '{} - {}'.format(song_list[-1], key)

    return song_list


# todo fix this once the block has an ID for the datepick field 
def get_rehearsal_date_from_block(payload):
    blocks = payload['message']['blocks']
    for block in blocks:
        try:
            if block['elements'][0]['type'] == 'datepicker':
                return block['elements'][0]['initial_date']
        except:
            continue
