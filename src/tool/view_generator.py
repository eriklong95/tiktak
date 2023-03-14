import json, re

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
    f.write('import src.flaskr.controllers.users_controller as users_controller')
    f.write('\n')
    f.write('import src.flaskr.controllers.rank_controller as rank_controller')
    f.write('\n')
    f.write('import src.flaskr.controllers.games_controller as games_controller')
    f.write('\n')
    f.write('\n')
    f.write('bp = Blueprint(\'api\', __name__)\n')

    # parse JSON in flaskr/static/openapi.json
    with open('src/flaskr/static/openapi.json') as json_file:
        api_def = json.load(json_file)
        # iterate over paths
        for path in api_def['paths']:
            print(f'{path}')
            print(f'    Writing view functions for operations on this path...')
            print('\n')

            # convert path to flask format with <path_param> instead of {pathParam}
            path_params = re.findall(r'{([a-zA-Z]*)}', path)
            path_params_in_snake_case = [re.sub(r'([A-Z])', r'_\1', param).lower() for param in path_params]

            path_in_flask_format = path
            for i in range(len(path_params)):
                path_in_flask_format = path_in_flask_format.replace('{' + path_params[i] + '}', '<' + path_params_in_snake_case[i] + '>')

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
                f.write(f'@bp.{method}(\'{path_in_flask_format}\')')
                f.write('\n')
                
                
                f.write(f'def {operation_id}(')
                # pass parameters to view function
                for param in path_params_in_snake_case:
                    f.write(f'{param}, ')
                        
                f.write('):')
                f.write('\n')
                f.write(f'    """{description}"""')
                f.write('\n')

                # pass request to controller
                f.write(f'    return {tag}_controller.{operation_id}(request')
                for param in path_params_in_snake_case:
                    f.write(f', {param}')
            
                f.write(')')
                f.write('\n\n')

                print(f'        Successfully wrote view function!')
                print('\n')
    
    print(f'Successfully wrote all view functions to {file_location}!')
                