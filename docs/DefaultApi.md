# pybloodsclient.DefaultApi

All URIs are relative to *http://127.0.0.1:5000/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**note_group_id_get**](DefaultApi.md#note_group_id_get) | **GET** /note_group/{id} | Return a list of notes
[**note_groups_get**](DefaultApi.md#note_groups_get) | **GET** /note_groups | Return a list of all available note groups
[**observations_get**](DefaultApi.md#observations_get) | **GET** /observations | Return a list of all observations
[**observations_post**](DefaultApi.md#observations_post) | **POST** /observations | Create a new observation
[**providers_get**](DefaultApi.md#providers_get) | **GET** /providers | Return a list of all available healthcare providers
[**samples_get**](DefaultApi.md#samples_get) | **GET** /samples | Return a list of all available samples
[**sources_get**](DefaultApi.md#sources_get) | **GET** /sources | Return a list of all available sources
[**units_get**](DefaultApi.md#units_get) | **GET** /units | Return a list of all available units
[**units_post**](DefaultApi.md#units_post) | **POST** /units | Create a new unit

# **note_group_id_get**
> InlineResponse200 note_group_id_get(id)

Return a list of notes

### Example
```python
from __future__ import print_function
import time
import pybloodsclient
from pybloodsclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pybloodsclient.DefaultApi()
id = 56 # int | Numeric ID of the Note Group

try:
    # Return a list of notes
    api_response = api_instance.note_group_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->note_group_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Numeric ID of the Note Group | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **note_groups_get**
> list[NoteGroup] note_groups_get()

Return a list of all available note groups

### Example
```python
from __future__ import print_function
import time
import pybloodsclient
from pybloodsclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pybloodsclient.DefaultApi()

try:
    # Return a list of all available note groups
    api_response = api_instance.note_groups_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->note_groups_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[NoteGroup]**](NoteGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **observations_get**
> list[Observation] observations_get()

Return a list of all observations

### Example
```python
from __future__ import print_function
import time
import pybloodsclient
from pybloodsclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pybloodsclient.DefaultApi()

try:
    # Return a list of all observations
    api_response = api_instance.observations_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->observations_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Observation]**](Observation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **observations_post**
> Observation observations_post(body)

Create a new observation

### Example
```python
from __future__ import print_function
import time
import pybloodsclient
from pybloodsclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pybloodsclient.DefaultApi()
body = pybloodsclient.NewObservation() # NewObservation | A new Observation

try:
    # Create a new observation
    api_response = api_instance.observations_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->observations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NewObservation**](NewObservation.md)| A new Observation | 

### Return type

[**Observation**](Observation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_get**
> list[Provider] providers_get()

Return a list of all available healthcare providers

### Example
```python
from __future__ import print_function
import time
import pybloodsclient
from pybloodsclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pybloodsclient.DefaultApi()

try:
    # Return a list of all available healthcare providers
    api_response = api_instance.providers_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->providers_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Provider]**](Provider.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **samples_get**
> list[Sample] samples_get()

Return a list of all available samples

### Example
```python
from __future__ import print_function
import time
import pybloodsclient
from pybloodsclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pybloodsclient.DefaultApi()

try:
    # Return a list of all available samples
    api_response = api_instance.samples_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->samples_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Sample]**](Sample.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_get**
> list[Source] sources_get()

Return a list of all available sources

### Example
```python
from __future__ import print_function
import time
import pybloodsclient
from pybloodsclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pybloodsclient.DefaultApi()

try:
    # Return a list of all available sources
    api_response = api_instance.sources_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->sources_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Source]**](Source.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **units_get**
> list[Unit] units_get(name=name)

Return a list of all available units

### Example
```python
from __future__ import print_function
import time
import pybloodsclient
from pybloodsclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pybloodsclient.DefaultApi()
name = 'name_example' # str |  (optional)

try:
    # Return a list of all available units
    api_response = api_instance.units_get(name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->units_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 

### Return type

[**list[Unit]**](Unit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **units_post**
> Unit units_post(body)

Create a new unit

### Example
```python
from __future__ import print_function
import time
import pybloodsclient
from pybloodsclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pybloodsclient.DefaultApi()
body = pybloodsclient.NewUnit() # NewUnit | A new Unit

try:
    # Create a new unit
    api_response = api_instance.units_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->units_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NewUnit**](NewUnit.md)| A new Unit | 

### Return type

[**Unit**](Unit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

