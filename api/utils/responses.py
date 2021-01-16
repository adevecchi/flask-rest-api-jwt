from flask import make_response, jsonify

def response_with(response, value=None, message=None, error=None, headers={}, pagination=None):
    result = {}
    if value is not None:
        result.update(value)
    
    if response.get('message', None) is not None:
        result.update({'message': response['message']})
    
    result.update({'code': response['code']})

    if error is not None:
        result.update({'errors': error})
    
    if pagination is not None:
        result.update({'pagination': pagination})
    
    headers.update({'Access-Control-Allow-Origin': '*'})
    headers.update({'server': 'Flask REST API'})

    return make_response(jsonify(result), response['http_code'], headers)

INVALID_FIELD_NAME_SENT_422 = {
    'http_code': 422,
    'code': 'invalid_field',
    'message': 'Invalid fields found'
}

INVALID_INPUT_422 = {
    'http_code': 422,
    'code': 'invalid_input',
    'message': 'Invalid input'
}

MISSING_PARAMETERS_422 = {
    'http_code': 422,
    'code': 'missing_parameter',
    'message': 'Missing parameters'
}

DUPLICATE_EMAIL_422 = {
    'http_code': 422,
    'code': 'duplicate_email',
    'message': 'This email is already linked to an existing client'
}

DUPLICATE_FAVORITE_PRODUCT_422 = {
    'http_code': 422,
    'code': 'duplicate_product',
    'message': 'This product is already linked to your favorite list'
}

BAD_REQUEST_400 = {
    'http_code': 400,
    'code': 'bad_request',
    'message': 'Bad request'
}

SERVER_ERROR_500 = {
    'http_code': 500,
    'code': 'server_error',
    'message': 'Server error'
}

SERVER_ERROR_404 = {
    'http_code': 404,
    'code': 'not_found',
    'message': 'Resource not found'
}

SERVER_ERROR_PRODUCT_404 = {
    'http_code': 404,
    'code': 'not_found',
    'message': 'Product not found'
}

UNAUTHORIZED_401 = {
    'http_code': 401,
    'code': 'not_authorized',
    'message': 'You are not authorized'
}

SUCCESS_200 = {
    'http_code': 200,
    'code': 'success'
}

SUCCESS_201 = {
    'http_code': 201,
    'code': 'success'
}

SUCCESS_204 = {
    'http_code': 204,
    'code': 'success'
}