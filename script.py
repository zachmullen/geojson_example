import json
from girder_worker_utils import Input, Output, docker_task, task_cli


@docker_task(
    image='zachmullen/geojson_example:latest', name='Largest county extraction',
    description='Extract the largest county in each state', inputs=[
        Input('infile', name='Input file', description='GeoJSON file with county info', type='file')
    ], outputs=[
        Output('outfile', name='Output file', description='GeoJSON containing largest county in each state',
               type='new-file')
    ]
)
def largest_counties(infile, outfile):
    with open(infile) as f:
        data = json.load(f)

    # Iterate over all features, keeping track of max for each state by area
    states = {}
    for feature in data['features']:
        state = feature['properties']['STATE']
        states[state] = max(
            states.get(state), feature,
            key=lambda f: None if f is None else f['properties']['CENSUSAREA'])

    with open(outfile, 'w') as f:
        json.dump({
            'features': states.values(),
            'type': 'FeatureCollection'
        }, f)


if __name__ == '__main__':
    task_cli(largest_counties)
