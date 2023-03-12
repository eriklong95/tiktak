import json

# This script generates view functions for all operations in the OpenAPI definition
# Run the script from the root directory of the project with 'python src/tool/view_generator.py'
print('Generating view functions based on OpenAPI definition...')
print('\n')
# write to a file
file_location = 'src/flaskr/api.py'
with open(file_location, 'w') as f:
    f.write('# This is generated source code. DO NOT EDIT!\n')
    f.write('from flask import Blueprint, request')
    f.write('\n')
    f.write('import flaskr.controllers.users_controller as users_controller')
    f.write('\n')
    f.write('import flaskr.controllers.rank_controller as rank_controller')
    f.write('\n')
    f.write('import flaskr.controllers.games_controller as games_controller')
    f.write('\n')
    f.write('\n')
    f.write('bp = Blueprint(\'api\', __name__)')

    # parse JSON in flaskr/static/openapi.json
    with open('src/flaskr/static/openapi.json') as json_file:
        api_def = json.load(json_file)
        # iterate over paths
        for path in api_def['paths']:
            # extract path parameters
            path_params = []
            if 'parameters' in api_def['paths'][path]:
                for param in api_def['paths'][path]['parameters']:
                    if param.get('in') != None and param['in'] == 'path':
                        path_params.append(param['name'])

            print(f'{path}')
            print(f'    Path parameters: {path_params}')
            print(f'    Writing view functions for operations on this path...')
            print('\n')
            # iterate over methods
            for method in api_def['paths'][path]:
                if method == 'parameters':
                    continue

                print(f'        {method}...')
                operation_def = api_def['paths'][path][method]
                
                # get operationId
                operation_id = operation_def['operationId']
                description = operation_def['description']
                tag = operation_def['tags'][0]
                
                # write to file
                f.write('\n')
                f.write(f'@bp.{method}(\'{path}\')')
                f.write('\n')
                
                
                f.write(f'def {operation_id}():')
                f.write('\n')
                f.write(f'    """{description}"""')
                f.write('\n')

                # pass request to controller
                f.write(f'    return {tag}_controller.{operation_id}(request)')
                f.write('\n\n')

                print(f'        Successfully wrote view function!')
                print('\n')
    
    print(f'Successfully wrote all view functions to {file_location}!')
                