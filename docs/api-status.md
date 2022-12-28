<!--
20/12/2022.
# Status: Open
-->

# ResultData class

Provides ability to dynamically add and access data as either dictionaries or lists during 
processing.

Final data can be serialised as a dictionary, and converted into JSON and returned to web
clients.

## Data requirements

<code>ResultData</code> recognises dictionaries, lists of dictionaries and nested dictionaries.

### Dictionaries

For example:

```python
{
    'first_name': 'Be Hai',
    'surname': 'Nguyen',
}
```

### Lists of dictionaries

For example:

```python
[{'CONTRACTOR_ID': 1,
  ...
  'EMAIL': 'behai_nguyen@hotmail.com',
  'GIVENNAME': 'Van Be Hai',
  'SURNAME': 'NGUYEN'},
  {'CONTRACTOR_ID': 20,
    ...
   'SURNAME': 'ABC'}]
```

### Nested dictionaries

For example:

```python
{'clientName': 'ACME IT Recruitment',
 'contractorName': 'NGUYEN Van Be Hai',
 'periodEnd': 'April 20 2003',
 'periodStart': 'April 14 2003',
 'timesheetTotal': '005 hrs 00 mins',
 'entries': [{'breakTime': '00:00',
              'chargeable': 'Yes',
              'dailyTotal': '05:00',
              'endTime': '01:00 PM',
              'periodDate': 'April 14 2003',
              'shortDayName': 'Mon',
              'startTime': '08:00 AM'},
             {'breakTime': '00:00',
              'chargeable': '',
              'dailyTotal': '00:00',
              'endTime': '00:00 PM',
              'periodDate': 'April 20 2003',
              'shortDayName': 'Sun',
              'startTime': '00:00 AM'}]}
```

### Glossary

Dictionaries, lists of dictionaries and nested structure are simply **data**. And the term **data** will be used to mean any one of them.

## Data Storage and Data Access

Data can be stored with an associated attribute or name, or without one. As a result, later access for each are different, depending on how they are stored originally.

### Limitations

To allow for the most intuitive usages, and also constraint to the most common ones, the following limitations are put in place:

1. Each <code>ResultData</code> instance should have only one list of dictionaries stored with no attribute. If there is already one, the later one will overwrite the existing one.

2. Each <code>ResultData</code> instance can have multiple different dictionaries stored with no attributes. Dictionaries' attributes become the instance's attributes. Duplicate attribute names from later dictionaries will be suffixed with a unique non-leading zero (0) number. That means all dictionaries are flattened out to form a single larger dictionary.

The following examples serve as usage cases for [ResultData](#resultdata-class). Each example represents a possible use case. They are also test cases implemented in module <code>tests/test_result_data.py</code>.

### Example 1: a dictionary with no name storage and access

```python
person = {
    'first_name': 'Be Hai',
    'surname': 'Nguyen',
}
```

```python
data = ResultData(data=person)
```

As object:

```python
assert data.first_name == 'Be Hai'
assert data.surname == 'Nguyen'
```

As dictionary:

```python
data_dict = data.as_dict()
assert data_dict['data']['first_name'] == 'Be Hai'
assert data_dict['data']['surname'] == 'Nguyen'
```

### Example 2: a list of dictionaries with no name storage and access

```python
contractor = [{'CONTRACTOR_ID': 1,
  ...
  'EMAIL': 'behai_nguyen@hotmail.com',
  'GIVENNAME': 'Van Be Hai',
  'SURNAME': 'NGUYEN'}]
```

```python
data = ResultData(data=contractor)
```

As object:

```python

assert (len(data) == 1)
assert data[0]['CONTRACTOR_ID'] == 1
...
assert data[0]['SURNAME'] == 'NGUYEN'
```

As dictionary:

```python
data_dict = data.as_dict()
assert (len(data_dict['data']) == 1)
assert data_dict['data'][0]['CONTRACTOR_ID'] == 1
...
assert data_dict['data'][0]['SURNAME'] == 'NGUYEN'
```

### Example 3: a nested dictionary with no name storage and access

```python
report = {'clientName': 'ACME IT Recruitment',
 'contractorName': 'NGUYEN Van Be Hai',
 'periodEnd': 'April 20 2003',
 'periodStart': 'April 14 2003',
 'timesheetTotal': '005 hrs 00 mins',
 'entries': [{'breakTime': '00:00',
              'chargeable': 'Yes',
              'dailyTotal': '05:00',
              'endTime': '01:00 PM',
              'periodDate': 'April 14 2003',
              'shortDayName': 'Mon',
              'startTime': '08:00 AM'},
             {'breakTime': '00:00',
              'chargeable': '',
              'dailyTotal': '00:00',
              'endTime': '00:00 PM',
              'periodDate': 'April 20 2003',
              'shortDayName': 'Sun',
              'startTime': '00:00 AM'}]}
```

```python
data = ResultData(data=report)
```

As object:

```python
assert data.clientName == 'ACME IT Recruitment'
assert data.timesheetTotal == '005 hrs 00 mins'
assert len(data.entries) == 2
assert data.entries[0]['endTime'] == '01:00 PM'
assert data.entries[1]['endTime'] == '00:00 PM'
```

As dictionary:

```python
data_dict = data.as_dict()
assert data_dict['data']['clientName'] == 'ACME IT Recruitment'
assert data_dict['data']['timesheetTotal'] == '005 hrs 00 mins'
assert len(data_dict['data']['entries']) == 2
assert data_dict['data']['entries'][0]['endTime'] == '01:00 PM'
assert data_dict['data']['entries'][1]['endTime'] == '00:00 PM'
```

### Example 4: a dictionary with named storage and access

```python
person = {
    'first_name': 'Be Hai',
    'surname': 'Nguyen',
}
```

```python
data = ResultData(data=person, data_name='person')
```

As object:

```python
assert data.person['first_name'] == 'Be Hai'
assert data.person['surname'] == 'Nguyen'
```

As dictionary:

```python
data_dict = data.as_dict()
assert data_dict['data']['person']['first_name'] == 'Be Hai'
assert data_dict['data']['person']['surname'] == 'Nguyen'
```

### Example 5: a list of dictionaries with named storage and access

```python
contractor = [{'CONTRACTOR_ID': 1,
  ...
  'EMAIL': 'behai_nguyen@hotmail.com',
  'GIVENNAME': 'Van Be Hai',
  'SURNAME': 'NGUYEN'}]
```

```python
data = ResultData(data=contractor, data_name='contractor')
```

As object:

```python
assert data.contractor[0]['CONTRACTOR_ID'] == 1
...
assert data.contractor[0]['SURNAME'] == 'NGUYEN'
```

As dictionary:

```python
data_dict = data.as_dict()
assert data_dict['data']['contractor'][0]['CONTRACTOR_ID'] == 1
...
assert data_dict['data']['contractor'][0]['SURNAME'] == 'NGUYEN'
```

### Example 6: a nested dictionary with no name storage and access

```python
report = {'clientName': 'ACME IT Recruitment',
 'contractorName': 'NGUYEN Van Be Hai',
 'periodEnd': 'April 20 2003',
 'periodStart': 'April 14 2003',
 'timesheetTotal': '005 hrs 00 mins',
 'entries': [{'breakTime': '00:00',
              'chargeable': 'Yes',
              'dailyTotal': '05:00',
              'endTime': '01:00 PM',
              'periodDate': 'April 14 2003',
              'shortDayName': 'Mon',
              'startTime': '08:00 AM'},
             {'breakTime': '00:00',
              'chargeable': '',
              'dailyTotal': '00:00',
              'endTime': '00:00 PM',
              'periodDate': 'April 20 2003',
              'shortDayName': 'Sun',
              'startTime': '00:00 AM'}]}
```

```python
data = ResultData(data=report, data_name='report')
```

As object:

```python
assert data.report['clientName'] == 'ACME IT Recruitment'
assert data.report['timesheetTotal'] == '005 hrs 00 mins'
assert len(data.report['entries']) == 2
assert data.report['entries'][0]['endTime'] == '01:00 PM'
assert data.report['entries'][1]['endTime'] == '00:00 PM'
```

As dictionary:

```python
data_dict = data.as_dict()
assert data_dict['data']['report']['clientName'] == 'ACME IT Recruitment'
assert data_dict['data']['report']['timesheetTotal'] == '005 hrs 00 mins'
assert len(data_dict['data']['report']['entries']) == 2
assert data_dict['data']['report']['entries'][0]['endTime'] == '01:00 PM'
assert data_dict['data']['report']['entries'][1]['endTime'] == '00:00 PM'
```

### Example 7: multiple dictionaries with no name storage and access

Dictionaries all have unique attribute names.

```python
customer = {
    'first_name': 'Be Hai',
    'surname': 'Nguyen',
}

order = {
    'date': '2022-10-23',
    'item': 'A Book',
}
```

```python
data = ResultData(data=customer)
data.add(data=order)
```

As object:

```python
assert data.first_name == 'Be Hai'
assert data.surname == 'Nguyen'
assert data.date == '2022-10-23'
assert data.item == 'A Book'
```

As dictionary:

```python
data_dict = data.as_dict()
assert data_dict['data']['first_name'] == 'Be Hai'
assert data_dict['data']['surname'] == 'Nguyen'    
assert data_dict['data']['date'] == '2022-10-23'
assert data_dict['data']['item'] == 'A Book'
```

### Example 8: Multiple dictionaries and list of dictionaries with no name storage and access

Realistically, the usage illustrated in this example makes no sense. But according to the requirements and the limitations, it must be satisfied.

```python
customer = {
    'first_name': 'Be Hai',
    'surname': 'Nguyen',
}

order = {
    'date': '2022-10-23',
    'item': 'A Book',
}

order_histories = [
    {'date': '2000-12-23'},
    {'date': '2020-01-23'}
]
```

```python
data = ResultData(data=customer)
data.add(data=order)
data.add(data=order_histories)
```

See also [Example 2: a list of dictionaries with no name storage and access](#example-2-a-list-of-dictionaries-with-no-name-storage-and-access)

As object:

```python
assert data.first_name == 'Be Hai'
assert data.surname == 'Nguyen'
assert data.date == '2022-10-23'
assert data.item == 'A Book'

# Accessing order_histories which was stored with no attribute name.

assert len(data) == 2
assert data[0]['date'] == '2000-12-23'
assert data[1]['date'] == '2020-01-23'
```

As dictionary:

```python
data_dict = data.as_dict()
assert data_dict['data']['first_name'] == 'Be Hai'
assert data_dict['data']['surname'] == 'Nguyen'    
assert data_dict['data']['date'] == '2022-10-23'
assert data_dict['data']['item'] == 'A Book'

# Accessing order_histories which was stored with no attribute name.
# As a dictionary, it must have a attribute. The default is 'items'.

assert len(data_dict['data']['items']) == 2
assert data_dict['data']['items'][0]['date'] == '2000-12-23'
assert data_dict['data']['items'][1]['date'] == '2020-01-23'
```

Very confusing!

It is so counter-intuitive. Even though it is possible to do this, for the sake of programming clarity, this usage should be avoided. As noted before, this is possible because it is a side effect of enabling the usage illustrated in
[Example 2: a list of dictionaries with no name storage and access](#example-2-a-list-of-dictionaries-with-no-name-storage-and-access).

### Example 9: No name and named multiple dictionaries and list of dictionaries storage and access

This example illustrates how [Example 8: Multiple dictionaries and list of dictionaries with no name storage and access](#example-8-multiple-dictionaries-and-list-of-dictionaries-with-no-name-storage-and-access) should be refactored.

```python
customer = {
    'first_name': 'Be Hai',
    'surname': 'Nguyen',
}

order = {
    'date': '2022-10-23',
    'item': 'A Book',
}

order_histories = [
    {'date': '2000-12-23'},
    {'date': '2020-01-23'}
]
```

```python
data = ResultData(data=customer)
data.add(order, 'order')
data.add(order_histories, 'order_histories')
```

As object:

```python
assert data.first_name == 'Be Hai'
assert data.surname == 'Nguyen'

assert data.order['date'] == '2022-10-23'
assert data.order['item'] == 'A Book'

assert len(data.order_histories) == 2
assert data.order_histories[0]['date'] == '2000-12-23'
assert data.order_histories[1]['date'] == '2020-01-23'
```

As dictionary:

```python
data_dict = data.as_dict()
assert data_dict['data']['first_name'] == 'Be Hai'
assert data_dict['data']['surname'] == 'Nguyen'    

assert data_dict['data']['order']['date'] == '2022-10-23'
assert data_dict['data']['order']['item'] == 'A Book'

assert len(data_dict['data']['order_histories']) == 2
assert data_dict['data']['order_histories'][0]['date'] == '2000-12-23'
assert data_dict['data']['order_histories'][1]['date'] == '2020-01-23'
```

### Example 10: Multiple dictionaries with overlapped attribute names with no name storage and access

```python
customer = {
    'first_name': 'Be Hai',
    'surname': 'Nguyen',

sale_staff = {
    'first_name': 'John',
    'surname': 'Smith',    
}
```

```python
data = ResultData(data=customer)
data.add(data=sale_staff)
```

As object:

```python
assert data.first_name == 'Be Hai'
assert data.surname == 'Nguyen'

assert data.first_name_1 == 'John'
assert data.surname_1 == 'Smith'
```

As dictionary:

```python
data_dict = data.as_dict()
assert data_dict['data']['first_name'] == 'Be Hai'
assert data_dict['data']['surname'] == 'Nguyen'

assert data_dict['data']['first_name_1'] == 'John'
assert data_dict['data']['surname_1'] == 'Smith'
```

Needless to say, the final data makes very little sense. It is up to users' discretion to use this feature.

### Example 11: Multiple lists of dictionaries with no name storage and access

Recall from the [Limitations](#limitations) section, the later list of dictionaries will overwrite the existing one: **multiple lists of dictionaries with no name are not possible**!

```python
order_histories = [
    {'date': '2000-12-23'},
    {'date': '2020-01-23'}
]

enquiry_histories = [
    {'subject': 'Credit Card Payment', 'date': '2019-03-08'},
    {'subject': 'Missed Delivery', 'date': '2020-12-21'},
    {'subject': 'Other...', 'date': '2021-04-18'}
]
```

```python
data = ResultData(data=order_histories)
data.add(data=enquiry_histories)
```

As object:

```python
assert len(data) == 3
assert data[0]['subject'] == 'Credit Card Payment'
assert data[2]['subject'] == 'Other...'
```

As dictionary:

```python
data_dict = data.as_dict()
assert len(data_dict['data']) == 3
assert data_dict['data'][0]['subject'] == 'Credit Card Payment'
assert data_dict['data'][2]['subject'] == 'Other...'
```

Recall [Example 8: Multiple dictionaries and list of dictionaries with no name storage and access](#example-8-multiple-dictionaries-and-list-of-dictionaries-with-no-name-storage-and-access), accessing the list items as a dictionary is as follows:

```python
"""
Accessing order_histories which was stored with no attribute name.
As a dictionary, it must have a attribute. The default is 'items'.
"""
assert len(['data']) == 2
assert ['data']['items'][0]['date'] == '2000-12-23'
assert ['data']['items'][1]['date'] == '2020-01-23'
```

**While in this example**, there is no <code>['items']</code>: *because there is only a single list of dictionaries with no name, this is basically identical to* [Example 2: a list of dictionaries with no name storage and access](#example-2-a-list-of-dictionaries-with-no-name-storage-and-access).

These examples have been extracted from test cases in module <code>tests/test_result_data.py</code>.

# ResultStatus class

It has two (2) primary properties:

1. code: <code>int</code>. Compulsory. An HTTP status code defined in [http — HTTP modules](https://docs.python.org/3/library/http.html#module-http).

2. text: <code>str</code>. Optional: can be blank. A free text message.

And two (2) auxiliary properties:

1. session_id: <code>str</code>. A web session identifier. It is assumed that, at the server-side, this identifier also gets logged for web requests. In case of errors, users can include this identifier in their reports, it helps to identify the web session that generates the returned error. It should get set when the <code>code</code> is <code>HTTPStatus.INTERNAL_SERVER_ERROR.value</code>.

2. data: [ResultData](#resultdata-class). Optionally gets set when needed to return data.

The following examples serve as illustrations of usage cases. The test cases implemented in module <code>tests/test_result_status.py</code> should further illustrate more use cases.

## Example 1

```python
status = ResultStatus(text="I am okay...")
```

As object:

```python
assert status.code == HTTPStatus.OK.value
assert status.text == "I am okay..."
assert status.session_id == None
assert status.data == None
assert status.has_data == False
```

As dictionary:

```python
status_dict = status.as_dict()
assert status_dict['status']['code'] == HTTPStatus.OK.value
assert status_dict['status']['text'] == "I am okay..."
assert ('session_id' not in status_dict['status']) == True
assert ('data' not in status_dict) == True
```

<code>status_dict</code> can then be converted into JSON and returned to (web) clients.

## Example 2

```python
person = {
    'first_name': 'Be Hai',
    'surname': 'Nguyen',
}
```

```python
status = ResultStatus(text="Data retrieved successfully.", data=person, data_name='person')
```

As object:

```python
assert status.code == HTTPStatus.OK.value
assert status.text == "Data retrieved successfully."
assert status.session_id == None
assert status.data != None
assert status.has_data == True
assert status.data.person['first_name'] == 'Be Hai'
assert status.data.person['surname'] == 'Nguyen'
```

As dictionary:

```python
status_dict = status.as_dict()
assert status_dict['status']['code'] == HTTPStatus.OK.value
assert status_dict['status']['text'] == "Data retrieved successfully."
assert ('session_id' not in status_dict['status']) == True
assert ('data' in status_dict) == True
assert status_dict['data']['person']['first_name'] == 'Be Hai'
assert status_dict['data']['person']['surname'] == 'Nguyen'
```

## Example 3

```python
from http import HTTPStatus

text = "I am not okay..."
session_id = "7578f4d3-353a-4de6-b080-317ddbbc512f.9LJkQNW9FW7wGPukgvN-lBMeySA"

status = ResultStatus(HTTPStatus.INTERNAL_SERVER_ERROR.value, text, session_id)
```

As object:

```python
assert status.code == HTTPStatus.INTERNAL_SERVER_ERROR.value
assert status.text == text
assert status.session_id == session_id
assert status.data == None
assert status.has_data == False
```

As dictionary:

```python
status_dict = status.as_dict()
assert status_dict['status']['code'] == HTTPStatus.INTERNAL_SERVER_ERROR.value
assert status_dict['status']['text'] == text
assert status_dict['status']['session_id'] == session_id
assert ('data' not in status_dict) == True
```

Please note, the test cases implemented in module <code>tests/test_result_status.py</code> should further illustrate more use cases.